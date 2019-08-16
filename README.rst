Flask-easylog
=============

help log management for flask application


Installation
------------

::

    pip install flask-easylog
        
Or

::

    git clone https://github.com/fraoustin/flask-easylog.git
    cd flask-easylog
    python setup.py install

Usage
-----

::

    from flask import Flask, request, current_app
    from logging import DEBUG, INFO
    from flask_easylog import EasyLog, log 


    app = Flask(__name__)
    app.secret_key = 'super secret string'
    app.logger.setLevel(INFO)
    
    EasyLog(app)

    @app.route("/")
    def hello():
        current_app.logger.critical("critical from hello")
        current_app.logger.error("error from hello")
        current_app.logger.info("info from hello")
        current_app.logger.debug("debug from hello")
        return "Hello World!"
    
    @app.route("/two")
    @log(DEBUG)
    def two():
        current_app.logger.critical("critical from hello")
        current_app.logger.error("error from hello")
        current_app.logger.info("info from hello")
        current_app.logger.debug("debug from hello")
        return "Hello World!"



    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)

