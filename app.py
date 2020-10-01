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
    tasks = mongo.db.task.find()
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
                    flash("Sign in a success, {}". format(
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
    return render_template("account.html", email=email)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)