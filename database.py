from sqlalchemy import create_engine, text
import os

# 
# 
# 

db_connection_string = os.environ['db_con_str']

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
