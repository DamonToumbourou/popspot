
from flask import Flask, render_template
from flask_adminlte import AdminLTE
from google.cloud import bigquery
import dateutil.parser
import uuid
import io



class User(object):
    """
    Example User object.  Based loosely off of Flask-Login's User model.
    """
    full_name = "Ben Diep"
    avatar = "/static/img/user2-160x160.jpg"
    created_at = dateutil.parser.parse("November 12, 2012")
    

app = Flask(__name__)
AdminLTE(app)

# This is a placeholder user object.  In the real-world, this would
# probably get populated via ... something.
current_user = User()

@app.route('/')
def index():
    print " --- START ---"
    client = bigquery.Client()
    query_job = client.run_async_query(str(uuid.uuid4()), """
    #standardSQL
    SELECT corpus AS title, COUNT(*) AS unique_words
    FROM `publicdata.samples.shakespeare`
    GROUP BY title
    ORDER BY unique_words DESC
    LIMIT 10""")

    query_job.begin()
    query_job.result()  # Wait for job to complete.

    destination_table = query_job.destination
    destination_table.reload()
    for row in destination_table.fetch_data():
        print(row)

    return render_template('index.html', current_user=current_user)

@app.route('/login')
def login():
    return render_template('login.html', current_user=current_user)

@app.route('/lockscreen')
def lockscreen():
    return render_template('lockscreen.html', current_user=current_user)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


