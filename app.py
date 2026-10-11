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
    # Log the address of the direct connection.
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
        <title>My Website</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
      </head>
      <body>
        <h1>Welcome to My Website</h1>
        <p>This website is online.</p>
        <p>Connection logs are used for security and abuse prevention.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
