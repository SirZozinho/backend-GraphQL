import strawberry
from typing import List

# 1. Définition du Type (L'Entité Tâche)
@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    status: str

# Simulation de base de données (juste une liste en mémoire)
tasks_db = [
    Task(id=strawberry.ID("1"), title="Faire le workshop", status="TODO")
]

# 2. Les Queries (La lecture)
@strawberry.type
class Query:
    @strawberry.field
    def tasks(self) -> List[Task]:
        return tasks_db

# 3. Les Mutations (L'action - À compléter pour l'exercice)
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_task(self, title: str) -> Task:
        new_task = Task(
            id=strawberry.ID(str(len(tasks_db) + 1)),
            title=title,
            status="TODO"
        )
        tasks_db.append(new_task)
        return new_task

# On assemble le tout dans un Schéma
schema = strawberry.Schema(query=Query, mutation=Mutation)