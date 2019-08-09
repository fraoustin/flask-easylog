from flask import Flask, request, current_app
from logging import DEBUG

from flask_easylog import EasyLog, FMT_ACCESS_LOG 

app = Flask(__name__)
app.secret_key = 'super secret string'
app.logger.setLevel(DEBUG)

EasyLog(app, 
    fmt = FMT_ACCESS_LOG,
    afterlog = True,
    beforelog = True)

@app.route("/")
def hello():
    current_app.logger.critical("critical from hello")
    current_app.logger.error("error from hello")
    current_app.logger.info("info from hello")
    current_app.logger.debug("debug from hello")
    return "Hello World!"


if __name__ == "__main__":
    app.logger.info("after run")
    app.run(host="0.0.0.0", port=8080, debug=True)