#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file, jsonify, request
from list import List
from task import Task
from utils import json_abort

import sys

VERSION =6.0
# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')

# ------------------------------------------------------------------------------
# ---------------------    HTML     --------------------------------------------
# ------------------------------------------------------------------------------
@app.route('/', methods=['GET'])
def front_end():
    return send_file('static/index.html')

# ------------------------------------------------------------------------------
# ---------------------     API     --------------------------------------------
# ------------------------------------------------------------------------------
#   give version
@app.route('/api/version/', methods=['GET'])
def get_api():
    return jsonify({"Version":VERSION})

# JSON lists
@app.route('/api/lists', methods=['GET'])
def get_lists():
    response = {}
    response["lists"] = [l.__dict__ for l in all_lists]
    return jsonify(response)

# JSON tasks
@app.route('/api/lists/<int:list_id>/tasks', methods=['GET'])
def get_tasks(list_id):
    response = {}
    response["tasks"] = [t.__dict__ for t in taskArray if t.list == list_id]
    return jsonify(response)


# POST
@app.route('/api/lists/<int:list_id>/tasks', methods=['POST'])
def add_task(list_id):
    try:
        data = request.get_json()
    except:
        json_abort(400, "no JSON provided")

    if data is None:
        json_abort(404, "Object is empty or no string.")

    if list_id not in ID:
        json_abort(505, "There is no list with such ID.")

    title_new = data.get("title", None)
    if title_new is None:
        json_abort(400, "Invalid Content-Type")

    due_new = data.get("due")

    new_id = max([int(t.id) for t in taskArray] + [-1]) + 1

    task_new = Task(title_new, list=list_id, id=str(new_id), due=due_new,
                    status=Task.NORMAL)

    taskArray.append(task_new)

    return jsonify(task_new.__dict__)


# DELETE
@app.route('/api/lists/<int:list_id>/tasks/<int:task_id>', methods=['DELETE'])
def del_task(list_id, task_id):
    if list_id not in ID:
        json_abort(404, "No list with given ID")

    tasks_with_id = [t for t in taskArray if t.id == task_id and t.list == list_id]
    if len(tasks_with_id) < 1:
        json_abort(404, "no such task with given task_id")

    for t in tasks_with_id:
        taskArray.remove(t)

    return jsonify({"result":True})

# Update
@app.route('/api/lists/<int:list_id>/tasks/<int:task_id>', methods=['PUT'])
def update_task(list_id, task_id):
    try:
        data = request.get_json()
    except:
        json_abort(404, "no JSON provided")

    tasks_with_id = [t for t in taskArray if t.id == task_id and t.list == list_id]
    if len(tasks_with_id) < 1:
        json_abort(404, "no such task with given task_id")

    for t in tasks_with_id:
        t.update_json_task(data)

    return jsonify(taskArray[0].__dict__)


# ------------------------------------------------------------------------------
# ---------------------   LISTS & TASKS   --------------------------------------
# ------------------------------------------------------------------------------
inbox = List(id=0, title="Inbox", rev=1)
all_lists = [inbox]

# INDEX of all lists
ID = []
for l in all_lists:
    ID.append(l.id)


taskArray = [
    Task(title="aufraeumen", list=inbox.id, status = Task.NORMAL, due="2016-12-23"),
    Task(title="Geschenke", list=inbox.id, status = Task.NORMAL, due="2016-12-31")
]

# ------------------------------------------------------------------------------
# ---------------------     MAIN    --------------------------------------------
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)

