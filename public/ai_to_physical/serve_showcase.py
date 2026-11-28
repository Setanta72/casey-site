"""
serve_showcase.py
Lightweight HTTP/1.1 static server with full byte-range (206 Partial Content) support
so MP4 and WebM videos stream, seek, and loop reliably in Safari, Chrome, and embedded webviews.

Usage:
  python3 /Users/setanta/Documents/Projects/OpenVis/KumikoTruss/01_standalone_showcase/serve_showcase.py
"""

import os
import re
import mimetypes
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT = "/Users/setanta/Documents/Projects/OpenVis/KumikoTruss"
PORT = 8765

mimetypes.add_type("video/webm", ".webm")
mimetypes.add_type("video/mp4", ".mp4")


class RangeHTTPRequestHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path) or not os.path.exists(path):
            return super().send_head()

        ctype = self.guess_type(path)
        f = open(path, "rb")
        fs = os.fstat(f.fileno())
        size = fs.st_size
        range_hdr = self.headers.get("Range")

        if range_hdr:
            m = re.match(r"bytes=(\d*)-(\d*)", range_hdr)
            if m:
                start = int(m.group(1)) if m.group(1) else 0
                end = int(m.group(2)) if m.group(2) else size - 1
                end = min(end, size - 1)
                if start <= end < size:
                    length = end - start + 1
                    self.send_response(206)
                    self.send_header("Content-Type", ctype)
                    self.send_header("Accept-Ranges", "bytes")
                    self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
                    self.send_header("Content-Length", str(length))
                    self.send_header("Cache-Control", "no-cache")
                    self.end_headers()
                    f.seek(start)
                    self._range_remaining = length
                    return f

        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(size))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self._range_remaining = None
        return f

    def copyfile(self, source, outputfile):
        rem = getattr(self, "_range_remaining", None)
        if rem is None:
            return super().copyfile(source, outputfile)
        bufsize = 64 * 1024
        while rem > 0:
            chunk = source.read(min(bufsize, rem))
            if not chunk:
                break
            outputfile.write(chunk)
            rem -= len(chunk)


if __name__ == "__main__":
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), RangeHTTPRequestHandler)
    print(f"Serving {ROOT} with HTTP/1.1 Range support at http://localhost:{PORT}/01_standalone_showcase/index.html", flush=True)
    httpd.serve_forever()
