Pour lancer le backend (dans un environnement Python) :
```
pip install -r requirements.txt
uvicorn main:app --reload
```

---

Dans le playground :

Lister la db :
```
query {
  tasks {
    id
    title
    status
  }
}
```

Ajouter une task : 
```
mutation {
  createTask (title : "Nouvelle tache"){
    id
    status
  }
}
```

Modifier une task :
```
mutation {
  updateTaskStatus(id: "1", status: DONE) {
    id
    title
    status
  }
}
```

Supprimer une tache :
```
mutation {
  deleteTask(id : "1")
}
```

le tp : [Workshop_Graphql.pdf](https://github.com/user-attachments/files/25052979/Workshop_Graphql.pdf)
