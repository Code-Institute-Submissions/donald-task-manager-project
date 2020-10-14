import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash, safe_str_cmp
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
print(f"DB: {os.environ.get('MONGO_DBNAME')} \n\tURI: {os.environ.get('MONGO_URI')}")
mongo = PyMongo(app)


@app.route("/")
@app.route("/allow_tasks")
def allow_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        first_user = mongo.db.donald_users.find_one(
            {"first_name": request.form.get("first_name")})

        if first_user:
            flash("Please enter new name")
            return redirect(url_for("sign_up"))
        
        sign_up = {
            "first_name": request.form.get("first_name"),
            "second_name": request.form.get("second_name"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.donald_users.insert(sign_up)

        session["first"] = request.form.get("first_name")
        flash("Sign in a success!")
        return redirect(url_for("account", email=session["first"]))

    return render_template("sign_up.html")
    

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        signed_user = mongo.db.donald_users.find_one(
            {"email": request.form.get("email")})
        
        if signed_user:
            if check_password_hash(
                signed_user["password"], request.form.get("password")):
                    session.permanent = True
                    session["first"] = request.form.get("email")
                    flash("Welcome, {}". format(
                        request.form.get("email")))
                    return redirect(url_for(
                        "account", email=session["first"]))

            else:
                flash("wrong email or password")
                return redirect(url_for("sign_in"))
        else:
            flash("wrong email or password")
            return redirect(url_for("sign_in"))
        
    return render_template("sign_in.html")


@app.route("/account/<email>", methods=["GET", "POST"])
def account(email):
    email = mongo.db.donald_users.find_one(
        {"email": session["first"]})["email"]

    if session["first"]:
        return render_template("account.html", email=email)

    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    flash("Succefully signed out")
    session.pop("first")
    return redirect(url_for("sign_in"))


@app.route("/new_file", methods=["GET", "POST"])
def new_file():
    if request.method == "POST":
        urgent_status = "open" if request.form.get("urgent_status") else "close"
        upon = {
            "category_title": request.form.get("category_title"),
            "email": request.form.get("email"),
            "first_name": request.form.get("first_name"),
            "datepicker": request.form.get("datepicker"),
            "input_text": request.form.get("input_text"),
            "textarea2": request.form.get("textarea2"),
            "urgent_status": urgent_status,
            "cookies_by": session["first"]
        }
        mongo.db.tasks.insert_one(upon)
        flash("Food option successfully done!!")
        return redirect(url_for("allow_tasks"))
        
    categories = mongo.db.categories.find()
    return render_template("new_file.html", categories=categories)


@app.route("/change_file/<task_id>", methods=["GET", "POST"])
def change_file(task_id):
    if request.method == "POST":
        urgent_status = "open" if request.form.get("urgent_status") else "close"
        send = {
            "category_title": request.form.get("category_title"),
            "email": request.form.get("email"),
            "first_name": request.form.get("first_name"),
            "datepicker": request.form.get("datepicker"),
            "input_text": request.form.get("input_text"),
            "textarea2": request.form.get("textarea2"),
            "urgent_status": urgent_status,
            "cookies_by": session["first"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, send)
        flash("Food Selection changed!!")
    
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find()
    return render_template("change_file.html", task=task, categories=categories)

@app.route("/remove_file/<task_id>")
def remove_file(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Food selection removed!")
    return redirect(url_for("allow_tasks"))

@app.route("/food_list")
def food_list():
    categories = list(mongo.db.categories.find())
    return render_template("food_list.html", categories=categories)

@app.route("/input_food_title", methods=["GET", "POST"])
def input_food_title():
    if request.method == "POST":
        food = {
            "category_title": request.form.get("category_title")
        }
        mongo.db.categories.insert_one(food)
        flash("New food added")
        return redirect(url_for("food_list"))

    return render_template("input_food_title.html")

@app.route("/change_food_title/<category_id>", methods=["POST", "GET"])
def change_food_title(category_id):
    if request.method == "POST":
        forward = {
            "category_title": request.form.get("category_title")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, forward)
        flash("Food Title changed")
        return redirect(url_for("food_list"))

    food_change = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("change_food_title.html", category=food_change)

@app.route("/remove_food_title/<category_id>")
def remove_food_title(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Food Title removed")
    return redirect(url_for("food_list"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)