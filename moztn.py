from flask import (
    Flask, url_for, render_template, session, redirect, escape, request,
    flash, redirect, current_app
)


app = Flask(__name__)



@app.route('/')
def home():
    return '<h1>Mozilla Tunisia New Home Page<h1> <a href="https://github.com/moztn/www-moztn">www-moztn</a>'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
