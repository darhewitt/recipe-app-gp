# **RecipePal App**

**User Stories**
The main user of this website would be anyone of the following

- Someone who likes food and cooking good healthy nutricious meals, easy to cook. 
- A student
- Parents cooking for their kids
- Someone looking to try some new foods
- Someone looking to cook a meal for a special occasion

## **Features**
 
### **Existing Features**
- Friendly,  easy to use UX design with simple navigation
- Routing to relevant pages, after a user undertakes an action/task (ie) when a user logs out, they're thanked with a flash message and redirected to login page (if they wish to login again). 
- Ability for the user to add a recipe to the site
- Ability for the user to edit any recipe on the site
- Add, edit or delete any cuisine category on the website
- Website is responsive across all mobile devices
- Directory of websites allows the user to easily navigate all recipes
- Category of cuisine appearing in the directory to help the user to search through all recipes easier
- A "tips" field that can be used to promote certain products through an Amazon link


### **Features Left to Implement**
- A searh bar that would allow for more detailed serch
- A like button for each recipe
- Login security feature


# **Tech Used**

### **Technologies used includes:**
- **HTML5**, **CSS3**, **JQuery**, **Javascript**, **Materialise CSS**, **Python**, **Flask** **Flask Py_Mongo**, **MongoDB** 

Base languages used to create website.

Used **HTML5** to handle page routing and to build custom directives - [HTML5](https://www.html5rocks.com/en/)

Used **CSS3** for styling and enhancing the look of the website - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

Used **Javascript** (minified versions) added end of document - [JAVASCRIPT](https://developer.mozilla.org/bm/docs/Web/JavaScript)

Used **JQuery** to trigger ready() functions for datepicker, collapsible side nav bar and materialise selection functions - [JQUERY](https://jquery.com/)

Used **Materialise** CSS UI was used throughout this project. -[MATERIALISE CSS](https://materializecss.com/)
 
Used Python 3.6.7 for developing this project - [PYTHON](https://docs.python.org/3/)

Used Flask 1.0.2 for developing this project - [FLASK](https://flask.palletsprojects.com/en/1.0.x/)

Used Flask_Pymongo 2.2.0 for developing this project -[FLASK_PYMONGO](https://flask-pymongo.readthedocs.io/en/latest/)

Used Pymongo 3.7.2 for developing this project - [PYMONGO](https://pypi.org/project/pymongo/)

Used Jinja2.10 for developing this project - [JINJA2](http://jinja.pocoo.org/docs/2.10/)

Used Mongo DB (mLab) for this project - [MONGO DB](https://mlab.com/)

## **Version Control (GitHub)**

I used version control (GitHub) on an ongoing basis to back-up my code to a remote repository at regular intervals throughout development of the RecipePal website project. 

## **Deployment**

This project is developed on Heroku Platform - 

I used Heroku to deploy my project -[Heroku](https://dashboard.heroku.com)
I set the following Configuration Variables in Heroku:-

IP - 0.0.0.0
PORT- 5000


## **How to run the code in this project**

Below is a list of some of the technologies I installed to run RecipePal project. 

To run DumpDinners website:-

1. Clone the repository url link to your workspace- [RecipePal](https://github.com/darhewitt/recipe-app-gp)
2. Install Flask - $pip install flask
3. Install Python - $sudo apt-get install python3.6 (or python 3.7)
4. Install Flask_Pymongo - $pip install flask_pymongo (in some instances, depending on what IDE is being used, it might be necessary to append --user to the end of the command.
5. Install requirements.txt file by using $pip freeze > requirements.txt



## **Testing**
Extensive testing was performed through the development of this aplication.

- Add recipe to website through Add Recipe page, check database to ensure all data was collected correctly
- Edit recipe though the edit button and check the database to confirm changes
- Add category to website through Add Category page, check database to ensure all data was collected correctly
- Edit category though the edit button and check the database to confirm changes
- Test all pages for responsivness for all screen sizes
- Edit recipe to make sure all current data for that recipe populated all the fileds of the edit recipe page
- 



