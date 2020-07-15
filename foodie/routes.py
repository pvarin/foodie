from . import app
from flask import render_template, request, redirect, url_for

# TODO: refactor and move the routes to a different file
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/recipe/list')
def list_recipes():
    return 'List of the recipes'

@app.route('/recipe/<int:recipe_id>')
def get_recipe(recipe_id):
    return render_template('get_recipe.html', recipe_id=recipe_id)

@app.route('/recipe/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'GET':
        return render_template('add_recipe.html')
    elif request.method == 'POST':
        # TODO: validate the recipe
        # TODO: add the recipe to the database
        recipe_id = 0
        return redirect(url_for('get_recipe', recipe_id=recipe_id))

@app.route('/list/create')
def create_list():
    return 'create a list on this page'
