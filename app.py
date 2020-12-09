import os
from flask import Flask, flash, render_template, redirect, request
from tasks import add

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', "super-secret")

export TZ="Europe/Paris"

CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "UTC"

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/add', methods=['POST'])
def add_inputs():
    x = int(request.form['x'])
    y = int(request.form['y'])
    add.delay(x, y)
    flash("Your addition job has been submitted.")
    return redirect('/')
