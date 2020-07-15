# Foodie

A web app for curating recipes, meal planning, and efficiently building grocery lists.

## Database setup.
Setup a Postgresql database.
```bash
createdb foodie_dev
```

Create the tables in the python interactive shell
```python
from foodie import db
db.create_all()
```