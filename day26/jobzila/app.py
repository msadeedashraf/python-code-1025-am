from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


# configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobs.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class JobList(db.Model):
    jobid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    applyLink = db.Column(db.String(100), nullable=True)
    creation_date = db.Column(db.Date, default=datetime.today)

    def __repr__(self) -> str:
        return f"{self.title} - {self.company}"


@app.route("/")
def defaultPage():
    return render_template("index.html")
    # return "<p>Hello, World!</p>"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/jobsearch")
def jobsearch():
    return render_template("jobsearch.html")


@app.route("/joblisting")
def joblisting():
    """
    job = JobList(
        jobid=1,
        title="Front-end Developer",
        company="ABC Company",
        location="New York, NY",
        description="We are seeking a talented Front-end Developer to join our team...",
        applyLink="https://example.com/apply",
    )
    db.session.add(job)
    db.session.commit()
    """
    myalljobslist = JobList.query.all()
    # print(myalljobslist)
    return render_template("joblistingtest.html", myalljobslist=myalljobslist)


@app.route("/addjobs", methods=["GET", "POST"])
def addjobs():

    if request.method == "POST":
        myjobtitle = request.form["jobtitle"]
        mylocation = request.form["location"]
        mycompany = request.form["company"]
        myjobdesc = request.form["jobdesc"]
        job = JobList(
            title=myjobtitle,
            company=mycompany,
            location=mylocation,
            description=myjobdesc,
            applyLink="https://example.com/apply",
        )
        db.session.add(job)
        db.session.commit()

        return redirect("/joblisting")

    return render_template("job_new.html")


@app.route("/delete/<int:jobid>")
def delete(jobid):
    myjob = JobList.query.filter_by(jobid=jobid).first()
    db.session.delete(myjob)
    db.session.commit()

    return redirect("/joblisting")


@app.route("/update/<int:jobid>", methods=["GET", "POST"])
def update(jobid):
    if request.method == "POST":
        myjobtitle = request.form["jobtitle"]
        mylocation = request.form["location"]
        mycompany = request.form["company"]
        myjobdesc = request.form["jobdesc"]

        myjob = JobList.query.filter_by(jobid=jobid).first()
        myjob.title = myjobtitle
        myjob.location = mylocation
        myjob.company = mycompany
        myjob.description = myjobdesc

        db.session.add(myjob)
        db.session.commit()
        return redirect("/joblisting")

    myjob = JobList.query.filter_by(jobid=jobid).first()
    return render_template("updatejob.html", myjob=myjob)


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=6060, debug=True)
