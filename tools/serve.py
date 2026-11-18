#!/usr/bin/env python3
"""Serve the site locally the way GitHub Pages does: unknown paths get 404.html.

    python3 tools/serve.py                      # http://localhost:8790/xchr92
    python3 tools/serve.py --base /noice-links  # http://localhost:8790/noice-links/xchr92, like a project site
"""

import argparse
import functools
import http.server
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent


class Handler(http.server.SimpleHTTPRequestHandler):
    base = ""
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".txt": "text/plain; charset=utf-8"}

    def send_head(self):
        path = self.path.split("?", 1)[0]
        if self.base and not (path == self.base or path.startswith(self.base + "/")):
            return self.not_found()
        self.path = self.path[len(self.base):] or "/"
        target = Path(self.translate_path(self.path))
        if target.is_dir() and not (target / "index.html").is_file():
            return self.not_found()  # GitHub Pages never lists directories
        if not target.exists():
            return self.not_found()
        return super().send_head()

    def not_found(self):
        body = (SITE / "404.html").read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command == "HEAD":
            return None
        self.wfile.write(body)
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--port", type=int, default=8790)
    parser.add_argument("--base", default="", help="Path prefix, e.g. /noice-links for a GitHub project site.")
    args = parser.parse_args()
    Handler.base = "/" + args.base.strip("/") if args.base.strip("/") else ""
    server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), functools.partial(Handler, directory=str(SITE)))
    print(f"Serving {SITE} at http://localhost:{args.port}{Handler.base}/")
    server.serve_forever()


if __name__ == "__main__":
    main()
