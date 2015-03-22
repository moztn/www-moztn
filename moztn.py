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
    return render_template('about/index.html')

@app.route('/contact')
def contact():
    return 'Not yet done'


@app.errorhandler(404)
def blog_redirection(e):
    return redirect('https://blog.mozilla-tunisia.org{0}'.format(request.path))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
