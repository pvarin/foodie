from flask import request
from foodie.database import db
from foodie.models import Ingredient, IngredientQuantity, Recipe

def add_recipe():
    # Get or add all of the ingredients.
    ingredients = []
    for name in request.form.getlist("ingredient_name"):
        name = name.lower()
        ingredient = db.session.query(Ingredient).filter_by(
            name=name).first()
        if ingredient is None:
            ingredient = Ingredient(name=name)
            db.session.add(ingredient)
        ingredients.append(ingredient)

    # Build the ingredient quantities.
    ingredient_qtys = []
    for ingredient, qty in zip(
            ingredients, request.form.getlist("ingredient_qty")):

        # Add the ingredient quantity
        ingredient_qty = IngredientQuantity(ingredient=ingredient,
                                            quantity=qty)
        db.session.add(ingredient_qty)
        ingredient_qtys.append(ingredient_qty)

    recipe_name = request.form['recipe_name']
    instructions = request.form['recipe_instructions']
    recipe = Recipe(name=recipe_name,
                    instructions=instructions,
                    ingredients=ingredient_qtys)
    db.session.add(recipe)
    db.session.commit()
    
    return recipe.id

def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    