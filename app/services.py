from .models import db, Task
from typing import List, Optional, Dict

class TaskService:
    @staticmethod
    def get_all_tasks() -> List[Task]:
        return Task.query.all()

    @staticmethod
    def get_task_by_id(task_id: int) -> Optional[Task]:
        return Task.query.get(task_id)

    @staticmethod
    def create_task(data: Dict) -> Task:
        task = Task(
            title=data['title'],
            description=data.get('description'),
            completed=data.get('completed', False)
        )
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def update_task(task: Task, data: Dict) -> Task:
        task.title = data['title']
        task.description = data.get('description')
        task.completed = data.get('completed', False)
        db.session.commit()
        return task

    @staticmethod
    def delete_task(task: Task) -> None:
        db.session.delete(task)
        db.session.commit()