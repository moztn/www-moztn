from flask import (
    Flask, url_for, render_template, session, redirect, escape, request,
    flash, redirect, current_app
)


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/contribute')
def contribute():
    return 'Please contribute to this page not yet done :('

@app.route('/resources')
def resources():
    return 'Not yet done'

@app.route('/join')
def join():
    return 'Not yet done'

@app.route('/about')
def about():
    return 'Not yet done'

@app.route('/contact')
def contact():
    return 'Not yet done'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
