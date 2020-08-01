from foodie.database import db
from flask import render_template, request, redirect, url_for, Request, abort, current_app, Blueprint
from werkzeug.datastructures import ImmutableOrderedMultiDict
from foodie.models import Ingredient, IngredientQuantity, Recipe
from foodie import controllers

Request.parameter_storage_class = ImmutableOrderedMultiDict

recipes = Blueprint('recipes',
                    __name__,
                    static_folder='static',
                    template_folder='templates')


@recipes.route('/recipe/list')
def list_recipes():
    recipes = db.session.query(Recipe).all()
    print(recipes)
    return render_template("recipes/recipe_list.html", recipes=recipes)


@recipes.route('/recipe/<int:recipe_id>')
def get_recipe(recipe_id):
    recipe = db.session.query(Recipe).get(recipe_id)
    if recipe is None:
        abort(404)

    return render_template('/recipes/get_recipe.html', recipe=recipe)


@recipes.route('/recipe/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'GET':
        return render_template('recipes/add_recipe.html')
    elif request.method == 'POST':
        # TODO: validate the recipe
        recipe_id = controllers.add_recipe()

        return redirect(url_for('recipes.get_recipe', recipe_id=recipe_id))


@recipes.route('/recipe/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    controllers.delete_recipe(recipe_id)
    return redirect(url_for('recipes.list_recipes'))


@recipes.route('/list')
def user_list():
    return render_template("list.html", recipes=db.session.query(Recipe).all())
