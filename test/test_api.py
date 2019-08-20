import unittest
from flask import Flask, request, json, current_app

from flask_easylog import Api

from util import DictHandler

from logging import Logger, DEBUG, INFO, CRITICAL, ERROR, WARNING

def hello():
    current_app.logger.critical("critical from hello")
    current_app.logger.error("error from hello")
    current_app.logger.warning("warning from hello")
    current_app.logger.info("info from hello")
    current_app.logger.debug("debug from hello")
    return "Hello World!"

class TestApi(unittest.TestCase):
    """
        Class for Unitaire Test for flask_easylog.api
    """
    def setUp(self):
        self.app = Flask(__name__)
        for hdl in self.app.logger.handlers:
            self.app.logger.removeHandler(hdl)
        self.hdl = DictHandler()
        self.app.logger.addHandler(self.hdl)
        self.app.testing = True
        self.app.add_url_rule('/hello', 'hello', hello, methods=['GET'])
        self.app.register_blueprint(Api(url_prefix='/api'))

    def test_connection(self):
        with self.app.test_client() as c:
            rv = c.get('/hello')
            self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()