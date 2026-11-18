# Noice short links (static, GitHub Pages)

Live at https://jatin-banga-swiggy.github.io/noice-links/

A reserved link per pack, such as `<site>/xchr92`, redirects to the URL `links.json` gives for that code. That URL opens ChatGPT with a prompt pointing at the product's guide: a plain-text file with instructions for the assistant, image links and the label facts.

| File | Purpose |
| --- | --- |
| `index.html` | Home page: a grid of every product in `links.json`, numbered One, Two, Three… in file order, with its image, QR code, short link and guide. |
| `404.html` | The redirect. GitHub Pages serves it for any path without a file, so `/xchr92` lands here and its script redirects to that code's `url`. |
| `links.json` | One entry per code: `name`, `image` (home page), `page` (guide) and `url` (where the code redirects). Edit it to change where a printed QR goes. |
| `product/<slug>.txt` | Plain-text guides for assistants: instructions first, then image links, the label, supplement facts and the questions people often ask next. Generated; do not edit by hand. |
| `next-questions.json` | Per product code, the questions the guide offers as follow-up chips (three not yet asked, at the end of each answer). |
| `images/` | Product images used by the pages and the home page. Generated, except the logo. |
| `imaginary-products.json` | Two made-up products (magnesium, omega-3) so the grid has more than one card. Their guides say they are imaginary. |
| `vendor/qrcode.js` | The [qrcode](https://github.com/soldair/node-qrcode) 1.5.4 library (MIT), bundled for the browser. |
| `tools/build_pages.py` | Builds `product/` and `images/` from `../products.json` and `imaginary-products.json`: `../.venv/bin/python tools/build_pages.py`. Real photos are resized from `../images`; products without photos get a placeholder pack and a supplement facts panel drawn from their data. |
| `tools/serve.py` | Local test only: serves the site the way Pages does. `python3 tools/serve.py`, then open `http://localhost:8790/`. |

Assistants read a page without running its scripts, and an image in a chat is loaded straight from its URL, so guides and images are built ahead of time rather than in the browser. The redirect adds a fresh `?v=` to the guide link on every scan so ChatGPT does not reuse a cached copy.

Each `url` opens ChatGPT with a short, customer-style prompt: "Hey, I purchased <product>. Can you tell me more about it using this guide? <guide>".

Presentation guidance in a guide (tables, callouts, follow-up chips) is a request, not a control: ChatGPT treats text on web pages as information, and Intelligent UI chooses its own layout. Images from these links may not display, because ChatGPT does not always show images from addresses it does not recognise.

The repository is public because GitHub Pages on a free account needs that; every file in it is also served on the site.
