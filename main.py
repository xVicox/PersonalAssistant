from task_manager import TaskManager
from task import Task

task1 = Task("Joe",
            "Shopping",
            "Need to go shopping",
            "Errands")
task2 = Task("Pipin",
            "Learn to code",
            "Daily coding routine",
            "Education")


task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)

task_manager.remove_task("1")

task_manager.get_tasks()







