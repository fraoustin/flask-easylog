Plugin EasyLog
==============

::

    from flask import Flask

    from flask_easylog import EasyLog, log
    from logging import DEBUG 

    app = Flask(__name__)

    EasyLog(app)
    
    @app.route("/")
    def hello():
        current_app.logger.critical("critical from hello")
        current_app.logger.error("error from hello")
        current_app.logger.info("info from hello")
        current_app.logger.debug("debug from hello")
        return "Hello World!"

    @app.route("/one")
    @log(DEBUG)
    def one():
        current_app.logger.critical("critical from one")
        current_app.logger.error("error from one")
        current_app.logger.info("info from one")
        current_app.logger.debug("debug from one")
        return "Hello World!"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)

Parameter of **EasyLog**

- app: flask application
- fmt: format de log for your flask application
- werkzeug: enabled or disabled the werkzeug logger (default False)
- afterlog: enabled or disabled sending a message at the end of response (default False)
- aftermsg: if afterlog, format of message sending (default 'END')
- afterlevel: if afterlog, level of message sending (default INFO)
- beforelog: enabled or disabled sending a message at the end of response (default False)
- beforemsg: if beforelog, format of message sending (default 'START')
- beforelevel: if beforelog, level of message sending (default INFO)
- fmtaccesslog: format for logger "access.log" (default FMT_ACCESS_LOG)
- enabledaccesslog: add FileHandler if "FLASK_ENV" is production and path value not null (default None)
    
You can add keyword in message log:

- requestId
- secretKey from app config
- serverName from app config
- serverPort from app config
- cookieName from app config
- cookieDomain from app config
- cookiePath from app config
- args from request
- path from request
- method from request
- remoteAddr from request
- url from request
- user from request
- rule from request
- endpoint from request
- scheme from request
- fullPath from request
- httpHost from request
- queryString from request
- requestUri from request
- serverProtocol from request
- timestamp
- timeRequestReceived
- contentLength from response
- statusCode from response
- status from response


sample of usage

::

    %(remoteAddr)s - %(user)s [%(timeRequestReceived)s] "%(method)s %(path)s %(serverProtocol)s" %(statusCode)s %(message)s %(timestamp).3f second(s)