"""Personalized DevOps HTTP application using the Python standard library."""
import configparser
import html
import json
import os
import signal
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

DEFAULTS = {
    "name": "Alisher", "surname": "Suyubek",
    "group": "IT2-2306", "student_id": "37773",
}
ENV_KEYS = {
    "name": "STUDENT_NAME", "surname": "STUDENT_SURNAME",
    "group": "STUDENT_GROUP", "student_id": "STUDENT_ID",
}


def student_info(environ=None):
    env = os.environ if environ is None else environ
    return {field: env.get(key, "").strip() or DEFAULTS[field]
            for field, key in ENV_KEYS.items()}


def app_port(environ=None):
    env = os.environ if environ is None else environ
    path = env.get("APP_CONFIG", str(Path(__file__).resolve().parent.parent / "config/app.conf"))
    config = configparser.ConfigParser()
    config.read(path)
    value = env.get("APP_PORT") or config.get("application", "port", fallback="8000")
    port = int(value)
    if not 1 <= port <= 65535:
        raise ValueError("APP_PORT must be between 1 and 65535")
    return port


def make_handler(student):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlsplit(self.path).path
            status, content_type = 200, "text/plain; charset=utf-8"
            if path == "/health":
                body = b"OK\n"
            elif path == "/student":
                body = (json.dumps(student, ensure_ascii=False) + "\n").encode()
                content_type = "application/json; charset=utf-8"
            elif path == "/":
                safe = {key: html.escape(value) for key, value in student.items()}
                page = """<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Suyubek Alisher | DevOps</title>
<style>
body{font:18px/1.6 system-ui,sans-serif;background:#f4f6f8;color:#172332;margin:0}
main{max-width:760px;margin:8vh auto;padding:40px;background:white;border:1px solid #dce2e8;border-radius:16px}
small{letter-spacing:.15em;color:#506078}h1{font-size:42px;line-height:1.15;margin:18px 0}
dl{display:grid;grid-template-columns:140px 1fr;gap:14px;margin:32px 0}dt{color:#526273}dd{margin:0;font-weight:600}
.status{color:#146a3e}nav a{color:#245a9c;margin-right:22px}footer{border-top:1px solid #e3e8ed;padding-top:22px;color:#526273;font-size:15px}
@media(max-width:600px){main{margin:20px;padding:24px}h1{font-size:32px}}
</style><main><small>DEVOPS STUDENT APPLICATION</small>
<h1>{surname} {name}</h1><p class="status">Application is running successfully!</p>
<dl><dt>Name</dt><dd>{name}</dd><dt>Surname</dt><dd>{surname}</dd>
<dt>Group</dt><dd>{group}</dd><dt>Student ID</dt><dd>{student_id}</dd></dl>
<nav><a href="/student">Student JSON</a><a href="/health">Health check</a></nav>
<footer>Linux → Git → GitHub → Jenkins → Docker<br>Live delivery verified by Suyubek Alisher · Course DevOps</footer></main></html>"""
                body = page
                # Replace only the four data placeholders: CSS contains literal braces.
                for key, value in safe.items():
                    body = body.replace("{" + key + "}", value)
                body = body.encode()
                content_type = "text/html; charset=utf-8"
            else:
                status, body = 404, b"Not Found\n"
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    return Handler


def main():
    def stop_server(signum, frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGTERM, stop_server)
    student = student_info()
    print("DevOps Student Application", flush=True)
    for field, value in student.items():
        print(f"{field}: {value}", flush=True)
    server = ThreadingHTTPServer(("0.0.0.0", app_port()), make_handler(student))
    print(f"Application is running successfully on port {server.server_port}!", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
