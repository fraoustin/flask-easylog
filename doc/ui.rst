Ui EasyLog
==========

::

    from flask import Flask

    from flask_easylog import EasyLog, Api, Ui 

    app = Flask(__name__)

    EasyLog(app)
    app.register_blueprint(Api(url_prefix='/api'))
    app.register_blueprint(Ui(url_prefix='/ui'))

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)

You can use url:

- http://127.0.0.1/ui