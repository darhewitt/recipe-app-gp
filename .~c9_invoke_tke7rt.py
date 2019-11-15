import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes_app'
app.config["MONGO_URI"] = 'mongodb://dhewitt:Apple1991@myfirstcluster-shard-00-00-t0occ.mongodb.net:27017,myfirstcluster-shard-00-01-t0occ.mongodb.net:27017,myfirstcluster-shard-00-02-t0occ.mongodb.net:27017/recipes_app?ssl=true&replicaSet=myFirstCluster-shard-0&authSource=admin&retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find(),
    cuisines=mongo.db.cuisines.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    cuisines=mongo.db.cuisines.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = mongo.db.cuisines.find()
    return render_template('editrecipe.html', recipe=the_recipe, cuisines=all_cuisine)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'cuisine_name':request.form.get('cuisine_name'),
        'ingredients': request.form.get('ingredients'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time':request.form.get('cooking_time'),
        'method':request.form.get('method'),
        'serving':request.form.get('serving'),
        'tips':request.form.get('tips'),
        'username':request.form.get('username'),
        'recipe_description':request.form.get('recipe_description')
    })
    return redirect(url_for('get_recipes'))
    
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           cuisines=mongo.db.cuisines.find())
                           
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.cuisines.find_one(
                           {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(category_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('get_categories'))




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)