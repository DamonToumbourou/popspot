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
    data = [['Southern Cross', 2000000], ['Flinders Street', 100000], ['Southbank', 15000], ['Kings St', 63202]]

    # create textfile
    fo = open('wordcloud.txt', 'wb')
    for i in range(len(data)):
        location = data[i][0]
        count = data[i][1]
        scale_count = int(count/500)

        for j in range(scale_count):
            fo.write(location + " ")
    fo.close()

    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, 'wordcloud.txt')).read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:

    # lower max_font_size
    wordcloud = WordCloud(width=900,
                          height=600,
                          max_font_size=70,
                          min_font_size=4,
                          background_color=None,
                          mode='RGBA').generate(text)

    # save to image file
    wordcloud.to_file('static/img/wordcloud.png')


    return render_template('index.html', most_pop_overall=most_pop_overall, most_pop_day=most_pop_day,
                           most_pop_month=most_pop_month, most_pop_time=most_pop_time)




if __name__ == '__main__':
    app.run(debug=True)
