from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from routes.TaskRoute import task
from src.config import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
# db.create_all()
app.register_blueprint(task, url_prefix='/tasks')

if __name__ == "__main__":
    app.run()
