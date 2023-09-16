from urllib.error import HTTPError

from flask import request

from ..config.database import db
from ..models.TaskModel import Task
from ..schemas.TaskSchema import task_schema, tasks_schema
from ..util.Constants import RECORD_NOT_FOUND


def create_task():
    title = request.json['title']
    description = request.json['description']
    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)


def get_tasks():
    all_tasks = Task.query.all()
    return tasks_schema.dump(all_tasks)


def get_task(id):
    task = get_task_by_id(id)
    return task_schema.jsonify(task)


def update_task(id):
    task_updated = get_task_by_id(id)
    task_updated.title = request.json['title']
    task_updated.description = request.json['description']
    db.session.commit()
    return task_schema.jsonify(task_updated)


def delete_task(id) -> None:
    task = get_task_by_id(id)
    db.session.delete(task)
    db.session.commit()


def get_task_by_id(id):
    task = Task.query.get(id)
    if task is None:
        raise HTTPError(request.url, 404, RECORD_NOT_FOUND.format(id), None, None)
    return task
