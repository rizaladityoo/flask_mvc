from flask import Flask
from app.controllers import index, add_task, delete_task

app = Flask(__name__, template_folder='templates')

app.add_url_rule('/', 'index', index)
app.add_url_rule('/add', 'add_task', add_task, methods=['GET', 'POST'])
app.add_url_rule('/delete/<task_id>', 'delete_task', delete_task)

if __name__ == '__main__':
    app.run(debug=True)
