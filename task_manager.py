import task

class TaskManager:

    _task_count, _next_id = 0, 0

    def __init__(self):
        self._tasks = []
        self._next_id += 1

    def create_task(self):
        pass

    def add_task(self, new_task):
        self._tasks.append(new_task)
        print(f"New task added successfully.")

    def remove_task(self, task_id):
        tid = int(task_id)
        task_to_remove = None

        for task_item in self._tasks:
            if task_item.task_id == tid:
                task_to_remove = task_item
                break

        if task_to_remove:
            self._tasks.remove(task_to_remove)
            self._task_count -= 1
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def get_tasks(self):

        if not self._tasks.__len__() == 0:
            print(f"Tasks:")
            for task_item in self._tasks:

                print(f"{task_item}")
                print("-------------------")

        else:
            print("There are no tasks in the list.")

    def __getitem__(self, _id):
        pass