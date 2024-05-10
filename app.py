from flask import Flask, render_template, request, redirect, url_for, flash, abort
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
# from flask_migrate import Migrate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prof')
def profile():
    return render_template('prof.html')

@app.route('/guide')
def guide_page():
    return render_template('guide.html')

@app.route('/articleaye')
def content_page():
    return render_template('articleaye.html')

@app.route('/sponge')
def spongebob():
    return render_template('sponge.html')


if __name__ == "__main__":
    app.run(debug=True)