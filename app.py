# -*- coding: utf-8 -*-#enoding: utf-8 -*-
from flask import Flask, render_template, url_for, g, redirect, request, flash

application = app = Flask(__name__)


# ---------------------------------------------------------------------------------
#   Page Routes
# -------------------------------------------------------------------------------*/

@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html')


if __name__ == "__main__":
    application.run(debug=True)
