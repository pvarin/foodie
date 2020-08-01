from foodie.database import db
import enum
from flask import request


class Ingredient(db.Model):
    ''' A table of ingredients. This is used to create unique ingredients that can be deduplicated in a grocery list.'''
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)


class IngredientQuantity(db.Model):
    '''
    An association table between recipes and ingredients.
    See https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#association-object
    '''
    __tablename__ = 'ingredient_quantity'

    recipe_id = db.Column(db.Integer,
                          db.ForeignKey("recipe.id"),
                          primary_key=True)
    ingredient_id = db.Column(db.Integer,
                              db.ForeignKey("ingredient.id"),
                              primary_key=True)
    quantity = db.Column(db.String())
    ingredient = db.relationship("Ingredient")
    recipe = db.relationship("Recipe", back_populates="ingredients")

    def __str__(self):
        return "{amt} of {name}".format(amt=self.quantity,
                                               name=self.ingredient.name)

    def __repr__(self):
        return "<IngredientQuantity {}, {}>".format(self.recipe_id,
                                                    self.ingredient_id)


class Recipe(db.Model):
    ''' A table of recipes. Each recipe is associated with many ingredient_quantity-s.'''
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    url = db.Column(db.String())
    image_url = db.Column(db.String())
    instructions = db.Column(db.String())
    ingredients = db.relationship("IngredientQuantity",
                                  back_populates="recipe", cascade="delete")
