import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO DBNAME"] = os.environ.get("MONGO DBNAME")
app.config["MONGO URI"] = os.environ.get("MONGO URI")
app.secret_key = os.environ.get("SECRET KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/allow_tasks")
def hello():
    tasks = mongo.db.tasks.find()
    return render_template("task.html", tasks=tasks)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)