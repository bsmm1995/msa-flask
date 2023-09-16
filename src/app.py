from datetime import datetime
from urllib.error import HTTPError

from flask import Flask, jsonify

from src.config import config
from src.config.database import db
from src.routes.TaskRoute import task
from src.schemas.TaskSchema import ma

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(task, url_prefix='/tasks/')
db.init_app(app)
ma.init_app(app)


@app.errorhandler(Exception)
def handle_error(ex):
    code = 500
    if isinstance(ex, HTTPError):
        code = ex.code
    return jsonify(message=str(ex), path=ex.url, datetime=datetime.now()), code


if __name__ == "__main__":
    app.run()
