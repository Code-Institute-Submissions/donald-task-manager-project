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
    return render_template("sign_up.html")
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)