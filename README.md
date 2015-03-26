Mozilla Tunisia home page
=========================

## Description :
New mozilla tunisia home page
 
## Running :
`pip` and `virtualenv` need to be installed on your machine.

1 - Setting a virtual environment:

     mkdir venv
     virtualenv venv
     source venv/bin/activate


2 - Cloning the project

    cd venv
    git clone https://github.com/moztn/www-moztn.git


3 - Installing dependencies:

    cd www-moztn
    pip install -r requirements.txt


4 - Running the App:

    $ python moztn.py


5 - Init data base :
   Open `http://localhost:5000/`


## Server Deployment :

In order to deploy the app on apache2 server, please follow these steps 

1 - Installing dependencies :

    sudo apt-get install libapache2-mod-wsgi python-dev

2 - Enableling the apache `mod_wsgi` :

    sudo a2enmod wsgi

3 - Locate your apache www/ directory :

In this case, `www-moztn` was cloned in `/var/www/www-moztn` don't forget this path we will need the next steps

4 - Create the wsgi file :

In `/var/www/www-moztn` create a new file : `flaskapp.wsgi` then put this content : 

    #!/usr/bin/python
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0, "/var/www/www-moztn/")

    from moztn import app as application # moztn is moztn.py



5 - Apache config file :
  We will add a `VirtualHost` entry for our app :

    <VirtualHost *:80>
      ServerName www.mozilla-tunisia.org
      ServerAdmin rednaks@mozilla-tunisia.org
      WSGIScriptAlias / /var/www/www-moztn/flaskapp.wsgi
      <Directory /var/www/www-moztn/>
        Order allow,deny
        Allow from all
      </Directory>
      Alias /static /var/www/www-moztn/static
      <Directory /var/www/www-moztn/static/>
        Order allow,deny
        Allow from all
      </Directory>
      ErrorLog ${APACHE_LOG_DIR}/www-moztn-error.log
      LogLevel warn
      CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
