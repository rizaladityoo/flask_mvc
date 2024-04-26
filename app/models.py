class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

class TaskModel:
    tasks = []

    @classmethod
    def add_task(cls, title, description):
        task_id = len(cls.tasks) + 1
        task = Task(task_id, title, description)
        cls.tasks.append(task)

    @classmethod
    def get_tasks(cls):
        return cls.tasks

    @classmethod
    def delete_task(cls, task_id):
        cls.tasks = [task for task in cls.tasks if task.id != task_id]
