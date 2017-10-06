# ---------------------------------------------------------------------------------
#   Imports
# -------------------------------------------------------------------------------*/
from flask import Flask, render_template
from flask_adminlte import AdminLTE
import dateutil.parser
import io
from flask_mysqldb import MySQL
# from bigquery import BigQuery


# ---------------------------------------------------------------------------------
#   Configuration
# -------------------------------------------------------------------------------*/

# Application
app = Flask(__name__)
AdminLTE(app)

# mySQL
mysql = MySQL(app)


# ---------------------------------------------------------------------------------
#   Routes
# -------------------------------------------------------------------------------*/
@app.route('/')
def index():
    print " --- START ---"
    #query = BigQuery().most_popular()
    #print 'most pop'
    #print query

    cursor = mysql.connection.cursor()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


