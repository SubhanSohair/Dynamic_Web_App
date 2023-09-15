from sqlalchemy import create_engine, text
import os

#
#
#

db_connection_string =  os.environ['db_con_str']


engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)


col_name = ('id', 'title', 'location', 'salary',
            'currency', 'responsibilties', 'requirements')


def load_jobs_from_db():

    with engine.connect() as conn:
        # col_names = conn.execute(text("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'jobs'"))
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()

        jobs = []
        # list_dict.append(dict(zip(col_name,result_all[0])))
        for row in result_all:
            load_dict = dict(zip(col_name, row))
            jobs.append(load_dict)

        return jobs


def load_job_from_db(id):

    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(zip(col_name, rows[0]))

# print(load_job_from_db(1))


def add_application_to_db(job_id, data):

    with engine.connect() as conn:

        query = text(f"INSERT INTO applications (job_id, full_name, email, GitHub_URL, education, work_experience, resume_url) VALUES ('{job_id}', '{data['full_name']}', '{data['email']}', '{data['GitHub_URL']}', '{data['education']}', '{data['work_experience']}', '{data['resume_url']}')")

        conn.execute(query)


## USER AUTH

def load_admin_from_db():

    with engine.connect() as conn:
        result = conn.execute(text("select * from admin_data"))
        result_all = result.all()

        Admin_data = []
        Admin_data.append(result_all[0][0])
        Admin_data.append(result_all[0][1])
        
        return Admin_data
    

# ADD JOB TO DB 
  
def add_job_to_db(data):

    with engine.connect() as conn:

        query = text(f"INSERT INTO jobs (title, location, salary, currency, responsibilties, requirements)  VALUES ('{data['title']}', '{data['location']}', '{data['salary']}', '{data['currency']}', '{data['responsibilities']}', '{data['requirements']}')")

        conn.execute(query)
  

# DELETE JOB FROM DB 
  
def delete_job_from_db(id):

    with engine.connect() as conn:

        query = text(f"DELETE FROM jobs WHERE (id ={id} );")

        conn.execute(query)


# DELETE FROM jobs WHERE (`id` = '6');

# 
# 
# 

# LOAD APPLICATIONS FORM DB



apps_col_name = ('id', 'job_name', 'full_name', 'email',
            'GitHub_URL', 'education', 'work_experience', 'resume_url', 'approvals')


def load_apps_from_db():

    with engine.connect() as conn:
        result = conn.execute(text("""SELECT applications.id, jobs.title AS job_name, applications.full_name, applications.email, applications.GitHub_URL,  applications.education, applications.work_experience, applications.resume_url, applications.approvals
                                      FROM applications
                                      INNER JOIN jobs ON applications.job_id = jobs.id;
                                      """))
        result_all = result.all()

        apps = []

        for row in result_all:
            load_dict = dict(zip(apps_col_name, row))
            apps.append(load_dict)

        return apps
    

# DELETE APPLICATIONS FROM DB 
  
def delete_app_from_db(id):

    with engine.connect() as conn:

        query = text(f"DELETE FROM applications WHERE (id ={id} );")

        conn.execute(query)


# UPDATE "approvals" COlUMN IN DB TO APPROVE APPLICANTS

  
def approve_app_in_db(id):

    with engine.connect() as conn:

        query = text(f"UPDATE applications SET approvals = 'Approved' WHERE (id = {id});")

        conn.execute(query)

# UPDATES JOB INFO IN DB


def update_job_to_db(id, data):

    with engine.connect() as conn:

        query = text(f"UPDATE jobs SET title = '{data['title']}', location = '{data['location']}' , salary = '{data['salary']}' , currency = '{data['currency']}',  responsibilties = '{data['responsibilties']}' , requirements = '{data['requirements']}' WHERE (id = {id});")

        conn.execute(query)


# UPDATE jobs SET title = 'new', location = 'new', salary = '52222', responsibilties = 'lssmslmslm', requirements = 'mlcmsclmslc' WHERE (id = {id});



# INSERT INTO applications (job_id, full_name, email, GitHub_URL, education, work_experience, resume_url) VALUES ('{data['full_name']}', '{data['email']}', '{data['GitHub_URL']}', '{data['education']}', '{data['work_experience']}', '{data['resume_url']}')