# ---------------------------------------------------------------------------------
#   Imports
# -------------------------------------------------------------------------------*/
from flask import Flask, render_template
from flask_adminlte import AdminLTE
from bigquery import BigQuery
import dateutil.parser
import io
from os import path
from wordcloud import WordCloud
from bigquery import BigQuery


# ---------------------------------------------------------------------------------
#   Configuration
# -------------------------------------------------------------------------------*/

# Application
app = Flask(__name__)
AdminLTE(app)





# ---------------------------------------------------------------------------------
#   Global Functions
# -------------------------------------------------------------------------------*/

# wordmap colour function
def white_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(360, 100%, 100%)"


# ---------------------------------------------------------------------------------
#   Page Routes
# -------------------------------------------------------------------------------*/
@app.route('/')
def index():
    print " --- START ---"
    query = BigQuery()
    most_pop_overall = query.most_popular_overall()
    most_pop_day = query.most_popular_day()
    most_pop_month = query.most_popular_month()
    most_pop_time = query.most_popular_time()

    # ----------------------
    #   Word Cloud
    # --------------------*/
    # pedestrian counts for each location
    frequencies = {'SOUTHERN CROSS': 2000000, 'FLINDERS STREET': 100000, 'SOUTH BANK': 15000, 'KINGS ST': 63202 }

    # create word cloud
    wordcloud = WordCloud(width=1856,
                          height=600,
                          font_path='./static/fonts/Oxygen/Oxygen-Bold.ttf',
                          min_font_size=5,
                          background_color=None,
                          color_func=white_color_func,
                          ).generate_from_frequencies(frequencies, 100)

    # save to image file
    wordcloud.to_file('static/img/wordcloud.png')

    return render_template('index.html', most_pop_overall=most_pop_overall, most_pop_day=most_pop_day,
                           most_pop_month=most_pop_month, most_pop_time=most_pop_time)


if __name__ == '__main__':
    app.run(debug=True)
