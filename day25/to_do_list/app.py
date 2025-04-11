from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
mytask = ""
mydesc = ""
# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todolist(db.Model):
    taskid = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=True)
    desc = db.Column(db.String(500), nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self) -> str:
    #     return f"{self.taskid} - {self.task} - {self.desc}"


@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":
        # print("Checking the postback")
        # print(request.form["task"])
        # print(mytask = request.form["task"]
        mytask = request.form["task"]
        mydesc = request.form["desc"]
        todo = Todolist(task=mytask, desc=mydesc)
        db.session.add(todo)
        db.session.commit()

    myalltodolist = Todolist.query.all()

    return render_template("index.html", myalltodolist=myalltodolist)


@app.route("/gettodolist")
def gettodo():
    myalltodolist = Todolist.query.all()
    print(myalltodolist)
    return "<p>Get All To Dos</p>"


@app.route("/delete/<int:taskid>")
def delete(taskid):
    mytodo = Todolist.query.filter_by(taskid=taskid).first()
    db.session.delete(mytodo)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:taskid>", methods=["GET", "POST"])
def update(taskid):
    if request.method == "POST":
        mytask = request.form["task"]
        mydesc = request.form["desc"]
        mytodo = Todolist.query.filter_by(taskid=taskid).first()
        mytodo.task = mytask
        mytodo.desc = mydesc
        db.session.add(mytodo)
        db.session.commit()
        return redirect("/")

    mytodo = Todolist.query.filter_by(taskid=taskid).first()
    return render_template("update.html", mytodo=mytodo)


if __name__ == "__main__":
    # Create database tables in an application context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
