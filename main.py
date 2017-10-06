# ---------------------------------------------------------------------------------
#   Imports
# -------------------------------------------------------------------------------*/
from flask import Flask, render_template
from flask_adminlte import AdminLTE
import dateutil.parser
import io
from bigquery import BigQuery


# ---------------------------------------------------------------------------------
#   Configuration
# -------------------------------------------------------------------------------*/

# Application
app = Flask(__name__)
AdminLTE(app)


# ---------------------------------------------------------------------------------
#   Routes
# -------------------------------------------------------------------------------*/
@app.route('/')
def index():
    print " --- START ---"
    most_pop = BigQuery().most_popular_overall()

    #cursor = mysql.connection.cursor()


    return render_template('index.html', most_pop=most_pop)




if __name__ == '__main__':
    app.run(debug=True)
