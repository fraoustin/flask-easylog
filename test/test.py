from flask import Flask, request, current_app
from logging import DEBUG, INFO

from flask_easylog import EasyLog, FMT_ACCESS_LOG, log, SpecificLevelLog 

app = Flask(__name__)
app.secret_key = 'super secret string'
app.logger.setLevel(DEBUG)

app.logger.info("before add EasyLog")

EasyLog(app, 
    fmt = FMT_ACCESS_LOG,
    afterlog = True,
    beforelog = True)

app.logger.info("after add EasyLog")

@app.route("/")
def hello():
    current_app.logger.critical("critical from hello")
    current_app.logger.error("error from hello")
    current_app.logger.info("info from hello")
    current_app.logger.debug("debug from hello")
    return "Hello World!"

@app.route("/testone")
@log
def testone():
    return "Test One"

@log(DEBUG)
@app.route("/testtwo")
def testtwo():
    return "Test Two"

print(SpecificLevelLog()['tutu'])
print(SpecificLevelLog()['testtwo'])

if __name__ == "__main__":
    app.logger.info("after run")
    app.run(host="0.0.0.0", port=8080, debug=True)