import strawberry
from typing import List
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

schema = strawberry.Schema(query=Query, mutation=Mutation)