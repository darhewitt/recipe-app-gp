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
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)