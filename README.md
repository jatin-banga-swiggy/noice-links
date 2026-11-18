# Noice short links (static, GitHub Pages)

A reserved link per pack, such as `<site>/xchr92`, that redirects to the URL `links.json` gives for that code. The home page shows every product with its QR code.

| File | Purpose |
| --- | --- |
| `index.html` | Home page: a grid of every product in `links.json`, numbered One, Two, Three… in file order, with its photo, QR code, short link and label page. |
| `404.html` | The redirect. GitHub Pages serves it for any path without a file, so `/xchr92` lands here and its script redirects to that code's `url`. |
| `links.json` | One entry per code: `name`, `image`, `label` (the label page) and `url` (where the code redirects). Edit it to change where a printed QR goes. |
| `sku/<name>.txt` | Label text an assistant can read, generated from `../products.json` and `imaginary-products.json` by `node tools/build-sku-pages.mjs`. |
| `imaginary-products.json` | Two made-up products (magnesium, omega-3) so the grid has more than one card. Their label pages say they are imaginary. |
| `images/` | Product photos and the logo shown on the home page. The two imaginary products use drawn placeholder bottles marked "Placeholder image". |
| `vendor/qrcode.js` | The [qrcode](https://github.com/soldair/node-qrcode) 1.5.4 library (MIT), bundled for the browser so the site loads nothing from elsewhere. |
| `tools/serve.py` | Local test only, not needed on GitHub Pages: serves `404.html` for unknown paths the way Pages does. `python3 tools/serve.py`, then open `http://localhost:8790/`. |

QR codes are drawn in the browser from the address the page is served on, so they encode the published short link once the site is live (and `localhost` when testing locally).

Each code's `url` points at the label pages on `https://jatin-banga-swiggy.github.io/noice-links/sku/`.

To publish, push this folder's contents to the root of a repository and turn on GitHub Pages (Settings → Pages → deploy from the branch root). On a free account the repository must be public.
