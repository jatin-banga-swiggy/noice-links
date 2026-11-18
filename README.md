# Noice short links (static, GitHub Pages)

Live at https://jatin-banga-swiggy.github.io/noice-links/

A reserved link per pack, such as `<site>/xchr92`, redirects to the URL `links.json` gives for that code. That URL opens ChatGPT with a prompt pointing at the product's page, which carries the label facts, the product images and how Noice Labs asks answers to be presented.

| File | Purpose |
| --- | --- |
| `index.html` | Home page: a grid of every product in `links.json`, numbered One, Two, Three… in file order, with its image, QR code, short link and product page. |
| `404.html` | The redirect. GitHub Pages serves it for any path without a file, so `/xchr92` lands here and its script redirects to that code's `url`. |
| `links.json` | One entry per code: `name`, `image` (home page), `page` (product page) and `url` (where the code redirects). Edit it to change where a printed QR goes. |
| `product/<slug>.html` | Product pages for assistants, served at `<site>/product/<slug>`: plain paragraphs, image tags and image links, presentation guidance, likely next questions, answering rules, then the label text and supplement facts. Generated; do not edit by hand. |
| `images/` | Product images used by the pages and the home page. Generated, except the logo. |
| `imaginary-products.json` | Two made-up products (magnesium, omega-3) so the grid has more than one card. Their pages say they are imaginary. |
| `vendor/qrcode.js` | The [qrcode](https://github.com/soldair/node-qrcode) 1.5.4 library (MIT), bundled for the browser. |
| `tools/build_pages.py` | Builds `product/` and `images/` from `../products.json` and `imaginary-products.json`: `../.venv/bin/python tools/build_pages.py`. Real photos are resized from `../images`; products without photos get a placeholder pack and a supplement facts panel drawn from their data. |
| `tools/serve.py` | Local test only: serves the site the way Pages does. `python3 tools/serve.py`, then open `http://localhost:8790/`. |

Assistants read a page's HTML without running its scripts, and an image in a chat is loaded straight from its URL, so pages and images are built ahead of time rather than in the browser.

Each `url` opens ChatGPT with a short, customer-style prompt: "Hey, I purchased <product>. Can you tell me more about it using this guide? <product page>".

Presentation guidance on a page (carousel, callouts, follow-up buttons) is a request, not a control: ChatGPT treats text on web pages as information, and Intelligent UI chooses its own layout.

The repository is public because GitHub Pages on a free account needs that; every file in it is also served on the site.
