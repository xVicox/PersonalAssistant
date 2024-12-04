class Task:

    _number_of_tasks = 0

    def __init__(self, creator, title, description, task_type):
        Task._number_of_tasks += 1
        self._task_id = Task._number_of_tasks
        self._creator = creator
        self._title = title
        self._description = description
        self._task_type = task_type
        self._is_active = True
        print(f"Task #{self._task_id} created.")

    @property
    def task_id(self):
        return self._task_id

    def __str__(self): #Returns a long string containing Task data
        return (f"Task ID: {self._task_id}\n"
                f"Creator: {self._creator}\n"
                f"Title: {self._title}\n"
                f"Description: {self._description}\n"
                f"Type: {self._task_type}\n"
                f"Active: {self._is_active}")
