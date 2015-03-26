# coding: utf-8
from flask import (
    Flask, url_for, render_template, session, redirect, escape, request,
    flash, redirect, current_app
)

from flask_wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
from flask.ext.mail import Message, Mail



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




mail = Mail()

app = Flask(__name__)
app.secret_key = 'test_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

#These fields needs to be filled in production
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_RECIPIENTS'] = ['']

mail.init_app(app)



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
        msg = Message(form.subject.data, sender=app.config['MAIL_USERNAME'],
            recipients=app.config['MAIL_RECIPIENTS'])
        msg.body = """
          From: {0} <{1}>
          {2}
          """.format(form.first_name.data + " " + form.last_name.data,
          form.email.data, form.message.data)

        mail.send(msg)

        return render_template('contact/index.html', form=form, sent=True)
    elif request.method == 'GET':
        return render_template('contact/index.html', form=form)

@app.route('/IRC')
def irc():
    return render_template('irc/index.html')


@app.errorhandler(404)
def blog_redirection(e):
    return redirect('https://blog.mozilla-tunisia.org{0}'.format(request.path))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
