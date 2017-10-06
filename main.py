# ---------------------------------------------------------------------------------
#   Imports
# -------------------------------------------------------------------------------*/
from flask import Flask, render_template
from flask_adminlte import AdminLTE
from bigquery import BigQuery
import dateutil.parser
import io
import geoplotlib
import geoplot


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
    query = BigQuery()
    most_pop_overall = query.most_popular_overall()
    most_pop_day = query.most_popular_day()
    most_pop_month = query.most_popular_month()
    most_pop_time = query.most_popular_time()

    #cursor = mysql.connection.cursor()



    return render_template('index.html', most_pop_overall=most_pop_overall, most_pop_day=most_pop_day,
                           most_pop_month=most_pop_month, most_pop_time=most_pop_time)




if __name__ == '__main__':
    app.run(debug=True)
