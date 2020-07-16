from . import app, db
from flask import render_template, request, redirect, url_for, Request, abort
from werkzeug.datastructures import ImmutableOrderedMultiDict
from foodie.models import Ingredient, IngredientQuantity, Recipe, QuantityType
Request.parameter_storage_class = ImmutableOrderedMultiDict

# TODO: refactor and move the routes to a different file
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/recipe/list')
def list_recipes():
    recipes = db.session.query(Recipe).all()
    return render_template("recipe_list.html", recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def get_recipe(recipe_id):
    recipe = db.session.query(Recipe).get(recipe_id)
    if recipe is None:
        abort(404)
    return render_template('get_recipe.html', recipe=recipe)

@app.route('/recipe/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'GET':
        return render_template('add_recipe.html')
    elif request.method == 'POST':
        # TODO: validate the recipe
        
        # Get or add all of the ingredients.
        ingredients = []
        for name in request.form.getlist("ingredient_name"):
            name = name.lower()
            ingredient = db.session.query(Ingredient).filter_by(name=name).first()
            if ingredient is None:
                ingredient = Ingredient(name=name)
                db.session.add(ingredient)
            ingredients.append(ingredient)
        
        # Build the ingredient quantities.
        ingredient_qtys = []
        for ingredient, qty, qty_type in zip(ingredients,
                                       request.form.getlist("ingredient_qty"),
                                       request.form.getlist("ingredient_qty_type")):
            qty = float(qty)
            qty_type = QuantityType(qty_type)
            
            # Add the ingredient quantity
            ingredient_qty = IngredientQuantity(
                                ingredient=ingredient,
                                quantity=float(qty),
                                quantity_type=qty_type)
            db.session.add(ingredient_qty)
            ingredient_qtys.append(ingredient_qty)
            
        recipe_name = request.form['recipe_name']
        instructions = request.form['recipe_instructions']
        recipe = Recipe(name=recipe_name, instructions=instructions, ingredients=ingredient_qtys)
        db.session.add(recipe)
        db.session.commit()
        
        return redirect(url_for('get_recipe', recipe_id=recipe.id))

@app.route('/list/create')
def create_list():
    return 'create a list on this page'
