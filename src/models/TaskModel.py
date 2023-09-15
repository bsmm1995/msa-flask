from ..config.database import db


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return f"{self.id}:{self.title}:{self.description}"

    def __str__(self):
        return "TASK: ID = {}, TITLE = {}, DESCRIPTION = {}".format(self.id, self.title, self.description)
