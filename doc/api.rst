Api EasyLog
===========

::

    from flask import Flask

    from flask_easylog import EasyLog, Api 

    app = Flask(__name__)

    EasyLog(app)
    app.register_blueprint(Api(url_prefix='/api'))

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)

You can use url:

- GET http://127.0.0.1/api/logs list of configuration specific log for all endpoints
- GET http://127.0.0.1/api/log/<endpoint> configuration specific log for endpoint
- PUT http://127.0.0.1/api/log/<endpoint> add or change configuration specific log for endpoint
- DELETE http://127.0.0.1/api/log/<endpoint> delete configuration specific log for endpoint

swagger configuration

::

    ---
    swagger: "2.0"
    info:
    description: "API for management log by Flask"
    version: "1.0.0"
    title: "Management Log for Flask"
    contact:
    name: "fraoustin@gmail.com"
    license:
    name: "Apache 2.0"
    url: "http://www.apache.org/licenses/LICENSE-2.0.html"
    host: "127.0.0.1"
    basePath: "/api"
    schemes:
        - "http"
    consumes:
        - "application/json"
    produces:
        - "application/json"
    paths:
        /logs:
            get:
                tags:
                    - "log"
                summary: "list of configuration"
                description: "Returns list of configuration by endpointr"
                operationId: "flask_easy_log.api.get_logs"
                produces:
                    - "application/json"
                responses:
                    200:
                        description: "List of configuration"
                        schema:
                        type: "array"
                        title: "loggers"
                        items:
                            $ref: "#/definitions/logger"
                    400:
                        description: "Invalid logger"
                        schema:
                        $ref: '#/definitions/errorModel'
        /log/{endpoint}:
            get:
                tags:
                    - "log"
                summary: "configuration specific log for endpoint"
                description: "Returns a configuration"
                operationId: "flask_easylog.api.get_log"
                produces:
                    - "application/json"
                parameters:
                    - name: "endpoint"
                        in: "path"
                        required: true
                        type: "string"
                responses:
                    200:
                        description: "successful operation"
                        schema:
                        $ref: "#/definitions/logger"
                    400:
                        description: "Invalid ID supplied"
                        schema:
                        $ref: '#/definitions/errorModel'
            put:
                tags:
                    - "log"
                summary: "Add or Updates configuration specific log for endpoint"
                operationId: "flask_easylog.api.set_log"
                parameters:
                    - name: "endpoint"
                        in: "endpoint"
                        required: true
                        type: "string"
                    - in: "body"
                        name: "body"
                        required: true
                        schema:
                        $ref: "#/definitions/logger"
                responses:
                    200:
                        description: "Logger object updated"
                    400:
                        description: "Invalid logger supplied"
                        schema:
                        $ref: '#/definitions/errorModel'
                    405:
                        description: "Invalid input"
                        schema:
                        $ref: '#/definitions/errorModel'
            delete:
                tags:
                    - "log"
                summary: "delete configuration specific log for endpoint"
                operationId: "flask_easylog.api.rm_log"
                parameters:
                    - name: "endpoint"
                        in: "endpoint"
                        required: true
                        type: "string"
                responses:
                    200:
                        description: "Logger object deleted"
                    400:
                        description: "Invalid logger supplied"
                        schema:
                        $ref: '#/definitions/errorModel'
    definitions:
        logger:
            type: object
            required:
                - endpoint
                - level
            properties:
                endpoint:
                    type: "string"
                    description: "id of endpoint"
                level:
                    level: "string"
                    description: "level of logger"
        errorModel:
            type: object
            properties:
                status:
                type: integer
                format: int32
                type:
                type: string
            title:
                type: string
                detail:
                type: string
                instance:
                type: string       




