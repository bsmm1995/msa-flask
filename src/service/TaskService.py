from flask import request, jsonify

from ..app import db
from ..models.TaskModel import Task
from ..schemas import TaskSchema


def create_task():
    title = request.json['title']
    description = request.json['description']
    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()
    return TaskSchema.jsonify(new_task)


def get_tasks():
    print("get_tasks")
    all_tasks = Task.query.all()
    result = TaskSchema.dump(all_tasks)
    return jsonify(result)


def get_task(id):
    task = Task.query.get(id)
    return TaskSchema.jsonify(task)


def update_task(id):
    task = Task.query.get(id)
    title = request.json['title']
    description = request.json['description']
    task.title = title
    task.description = description
    db.session.commit()
    return TaskSchema.jsonify(task)


def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return TaskSchema.jsonify(task)
