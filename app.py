from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)


JOBS = load_jobs_from_db()


@app.route("/")
def hello_world():
    # return "Hello Subhan"
    return render_template("home.html", jobs=JOBS, company_name="Chaynz Tech")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
