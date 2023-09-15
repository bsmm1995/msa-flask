from flask import Flask

from src.config import config
from src.config.database import db
from src.routes.TaskRoute import task
from src.schemas.TaskSchema import ma

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(task, url_prefix='/tasks/')
db.init_app(app)
ma.init_app(app)

if __name__ == "__main__":
    app.run()
