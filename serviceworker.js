var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
  './',
  './Home/',
  './Dashboard/',
  './static/css/style-home.css',
  './static/css/style_admin.css',
];

self.addEventListener('install', function (event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {

      return fetch(event.request)
        .catch(function (rsp) {
          return response;
        });

    })
  );
});

//////////////////////////////////////////////////////////

