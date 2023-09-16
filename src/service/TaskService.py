from urllib.error import HTTPError

from flask import request, Response

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
    return Response(task_schema.jsonify(new_task), 201, mimetype='application/json')


def get_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return Response(result)


def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)


def update_task(id):
    task_updated = Task.query.get(id)
    task_updated.title = request.json['title']
    task_updated.description = request.json['description']
    db.session.commit()
    return task_schema.jsonify(task_updated)


def delete_task(id):
    task = Task.query.get(id)
    if task is None:
        raise HTTPError(request.url, 404, RECORD_NOT_FOUND.format(id), None, None)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)
