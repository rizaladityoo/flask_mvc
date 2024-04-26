from flask import render_template, request, redirect, url_for
from app.models import TaskModel

def index():
    tasks = TaskModel.get_tasks()
    return render_template('index.html', tasks=tasks)

def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        TaskModel.add_task(title, description)
        return redirect(url_for('index'))

def delete_task(task_id):
    TaskModel.delete_task(int(task_id))
    return redirect(url_for('index'))
