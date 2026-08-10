import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";

const scope = "https://example.test/CalcBoy/";
const listeners = new Map();
const writes = [];
const fetched = [];

const self = {
  registration: { scope },
  location: { origin: "https://example.test" },
  addEventListener(type, listener) { listeners.set(type, listener); },
  skipWaiting() {},
  clients: { claim() {} },
};

const caches = {
  async open() {
    return { put: async (request) => writes.push(request.url) };
  },
  async match() { return undefined; },
  async keys() { return []; },
  async delete() { return true; },
};

const source = await readFile(new URL("../sw.js", import.meta.url), "utf8");
vm.runInNewContext(source, {
  URL,
  Promise,
  Response,
  self,
  caches,
  fetch: async (request) => {
    fetched.push(request.url);
    return new Response("ok", { status: 200 });
  },
});

const fetchListener = listeners.get("fetch");
assert.ok(fetchListener, "service worker must register a fetch handler");

async function dispatch(request) {
  let response;
  fetchListener({ request, respondWith(value) { response = value; } });
  if (response) await response;
  return response;
}

const allowedUrls = [
  scope,
  `${scope}index.html`,
  `${scope}apple-touch-icon.png`,
  `${scope}icon-512.png`,
];

for (const url of allowedUrls) {
  assert.ok(await dispatch(new Request(url)), `${url} is handled`);
}
assert.deepEqual(fetched, allowedUrls);
assert.deepEqual(writes, allowedUrls);

for (const request of [
  new Request(`${scope}?cache-bust=1`),
  new Request(`${scope}unknown-file.png`),
  new Request("https://other.example/asset.png"),
  { method: "POST", url: `${scope}index.html` },
]) {
  assert.equal(await dispatch(request), undefined, `${request.url} is not cached`);
}

assert.deepEqual(writes, allowedUrls);
console.log("Service worker cache allowlist verified.");
