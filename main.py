from google.cloud import vision
import dateutil.parser

from flask import Flask, render_template
from flask_adminlte import AdminLTE

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

    vision_client = vision.Client()
    
    file_name = 'cat.jpg'
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)

    labels = image.detect_labels()
    for label in labels:
        print '1: '
        print(label.description)



    return render_template('index.html', current_user=current_user)

@app.route('/login')
def login():
    return render_template('login.html', current_user=current_user)

@app.route('/lockscreen')
def lockscreen():
    return render_template('lockscreen.html', current_user=current_user)




if __name__ == '__main__':
    app.run(debug=True)


