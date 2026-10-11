import os
import logging
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.before_request
def log_request():
    # Render supplies the client address in this header.
    # Only trust this when the app is deployed behind Render.
    ip = request.headers.get("X-Forwarded-For", "").split(",")[0].strip()

    if not ip:
        ip = request.remote_addr or "unknown"

    logging.info(
        "Visitor request: ip=%s method=%s path=%s",
        ip,
        request.method,
        request.path
    )

@app.route("/")
def home():
    return """
    <!doctype html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            html, body {
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                background: black;
            }
            iframe {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border: 0;
            }
        </style>
    </head>
    <body>
        <iframe
            src="https://streamable.com/e/b555lx?quality=highest"
            allow="autoplay; fullscreen"
            allowfullscreen>
        </iframe>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
