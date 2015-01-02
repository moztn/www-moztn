from flask import (
    Flask, url_for, render_template, session, redirect, escape, request,
    flash, redirect, current_app
)


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home/index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
