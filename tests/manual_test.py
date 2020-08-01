import os
import sys

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
from foodie import create_app
from foodie.database import db
from foodie.models import Ingredient, Recipe, IngredientQuantity

# assert app.testing

create_app()

db.drop_all()
db.create_all()

try:
    salt = Ingredient(name='Salt')
    pepper = Ingredient(name='Pepper')
    ingredients = [
        IngredientQuantity(ingredient=salt, quantity="1/4 tsp"),
        IngredientQuantity(ingredient=pepper, quantity="1/2 tbsp")
    ]
    test_recipe = Recipe(
        name='Test Recipe',
        url="example.com",
        instructions=
        "This is a test set of instructions.\nDo this\nThen this\n",
        ingredients=ingredients)
    db.session.add(salt)
    db.session.add(pepper)
    db.session.add(test_recipe)
    db.session.commit()

    # Test that the tables have the right sizes.
    assert len(Ingredient.query.all()) == 2
    assert len(Recipe.query.all()) == 1
    assert len(IngredientQuantity.query.all()) == 2

finally:
    db.session.commit()  # Stop all transactions before dropping the tables.
    db.drop_all()
