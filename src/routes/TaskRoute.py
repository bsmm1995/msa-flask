from flask import Blueprint

from ..service.TaskService import create_task, get_tasks, get_task, update_task, delete_task

task = Blueprint('task', __name__)


@task.route('', methods=['POST'])
def create():
    return create_task()


@task.route('', methods=['GET'])
def get_all():
    return get_tasks()


@task.route('/<id>', methods=['GET'])
def get_by_id(id):
    return get_task(id)


@task.route('/<id>', methods=['PUT'])
def update(id):
    return update_task(id)


@task.route('/<id>', methods=['DELETE'])
def delete_by_id(id):
    return delete_task(id)
