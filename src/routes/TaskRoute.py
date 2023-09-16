from flask import Blueprint, Response, current_app

from ..service.TaskService import create_task, get_tasks, get_task, update_task, delete_task

task = Blueprint('task', __name__)


@task.route('', methods=['POST'])
def create():
    response = create_task()
    response.status = 201
    return response


@task.route('', methods=['GET'])
def get_all():
    current_app.logger.info("API: Obtener todas las tareas.")
    return get_tasks()


@task.route('/<id>', methods=['GET'])
def get_by_id(id):
    return get_task(id)


@task.route('/<id>', methods=['PUT'])
def update(id):
    return update_task(id)


@task.route('/<id>', methods=['DELETE'])
def delete_by_id(id):
    return Response(delete_task(id), 204)
