import strawberry
from typing import List, Optional
from enum import Enum

@strawberry.enum
class TaskStatus(Enum):
    TODO = "TODO"
    DOING = "DOING"
    DONE = "DONE"

@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    status: TaskStatus

tasks_db = [
    Task(id=strawberry.ID("1"), title="Faire le workshop", status=TaskStatus.DOING)
]

@strawberry.type
class Query:
    @strawberry.field
    def tasks(self) -> List[Task]:
        return tasks_db

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_task(self, title: str) -> Task:
        new_task = Task(
            id=strawberry.ID(str(len(tasks_db) + 1)),
            title=title,
            status=TaskStatus.TODO
        )
        tasks_db.append(new_task)
        return new_task

    @strawberry.mutation
    def update_task_status(self, id: strawberry.ID, status: TaskStatus) -> Optional[Task]:
        for task in tasks_db:
            if task.id == id:
                task.status = status
                return task
        
        return None

    @strawberry.mutation
    def delete_task(self, id: strawberry.ID) -> bool:
        global tasks_db
        initial_len = len(tasks_db)
        tasks_db = [t for t in tasks_db if t.id != id]
        return len(tasks_db) < initial_len


schema = strawberry.Schema(query=Query, mutation=Mutation)