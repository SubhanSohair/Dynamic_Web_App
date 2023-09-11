from flask import Flask, render_template, jsonify, request, session, redirect, url_for 
from database import load_jobs_from_db, load_job_from_db, add_application_to_db,  load_admin_from_db

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def hello_world():
    JOBS = load_jobs_from_db()
    # return "Hello Subhan"
    return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)


@app.route("/job/<id>")
def show_job(id):
    JOB = load_job_from_db(id)
    if not JOB:
        return "Not Found", 404
    return render_template("jobpage.html", job=JOB)

@app.route("/job/<id>/apply", methods = ['POST','GET'])
def apply_to_job(id):
    data = request.form
    JOB = load_job_from_db(id)

    add_application_to_db(id, data)

    return render_template("application_submitted.html", application = data, job = JOB)
    # return jsonify(data)



# ADMIN AUTH 

@app.route("/admin", methods = ['POST','GET'])
def signin():
    if request.method == "POST":

        ##
        Admin_data = load_admin_from_db()
        if Admin_data[0] == request.form['email'] and Admin_data[1] == request.form['password']:

        ##

            user = request.form['email']
            session['user'] = user
            return redirect('/dashboard')
        
        #
        else:
            return render_template('signin.html')
        
        #
    else:
        if 'user' in session:
            return redirect('/dashboard')
        return render_template('signin.html')
        

#ADMIN DASHBOARD

@app.route("/dashboard",methods = ['POST','GET'])
def admin():
    if 'user' in session:
        name = session['user']
        JOBS = load_jobs_from_db()
        return render_template("Admin.html", name = name, jobs=JOBS)
    else:
        return redirect('/admin')


#LOGOUT FROM ADMIN


@app.route("/logout",methods = ['POST','GET'])
def logout():
        session.pop('user',None)
        return redirect('/admin')





@app.route("/operations",methods = ['POST','GET'])
def operations():
    name = session['user']
    return render_template("operations.html", name = name)



##RUN
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)