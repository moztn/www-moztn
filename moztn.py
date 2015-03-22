# coding: utf-8
from flask import (
    Flask, url_for, render_template, session, redirect, escape, request,
    flash, redirect, current_app
)

from flask_wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError



class ContactForm(Form):

  first_name = TextField("Nom",
      [validators.Required("Le nom est obligatoire.")])
  last_name = TextField("Prenom",
      [validators.Required("Le Prénom est obligatoire.")])


  email = TextField("Email",
      [validators.Required("L'adresse email est obligatoire."),
      validators.Email("Il faut entrer une adresse email correcte")])
  subject = TextField("Sujet",
      [validators.Required("Le sujet est obligatoire.")])
  message = TextAreaField("Message", 
      [validators.Required("Veuillez entrer votre message.")])
  submit = SubmitField("Envoyer")




app = Flask(__name__)



# routes

@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/contribute')
def contribute():
    return 'Please contribute to this page not yet done :('

@app.route('/resources')
def resources():
    return render_template('resources/index.html')

@app.route('/join')
def join():
    return 'Not yet done'

@app.route('/about')
def about():
    return render_template('about/index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
      if form.validate() == False:
        flash("Error")
        return render_template('contact/index.html', form=form)
      else:
        return render_template('contact/index.html', status=True)
    elif request.method == 'GET':
        return render_template('contact/index.html', form=form)


@app.errorhandler(404)
def blog_redirection(e):
    return redirect('https://blog.mozilla-tunisia.org{0}'.format(request.path))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
