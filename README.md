# channel2600 // 2600chan

In an effort to stop myself going to dumb sites on the internet, I decided to make my own dumb site.

It's built with Django. [Try it out!](https://channel2600.herokuapp.com/)

![thread](http://i.imgur.com/zDmvFHX.png)

![index](http://i.imgur.com/dqAS4hZ.png)

## Local Install

### Requirements

* python2
* virtualenv
* virtualenvwrapper (optional)
* Cloudinary account
* ReCaptcha account

Set up the virtualenv, with virtualenvwrapper:
````
    mkvirtualenv 2600chan -p /path/to/python2
````    
Checkout the local branch so requirements.txt doesn't bring in postgres module, dev uses sqlite3.
````
    git checkout local
````
Install requirements.
````
    pip install -r requirements.txt
````
Run the migrations.
````
    python manage.py migrate
````
Set up the seed boards (optional, or you can adjust them in boards.json).
````
    python manage.py loaddata boards.json
````
Set up environment variables for your Cloudinary and ReCaptcha accounts.
````
    export CLOUDINARY_URL=
    export RECAPTCHA_PRIVATE_KEY=
    export RECAPTCHA_PUBLIC_KEY=
````
Run the server and navigate to localhost:8000 (or address:port as specified).
````
    python manage.py runserver
````

## Heroku Install

### Requirements

* Cloudinary account
* ReCaptcha account
* Heroku dyno setup

Assuming you've already cloned the repository, branch is set to master, and you've also set up heroku-cli for this repository:

Change the `ALLOWED_HOSTS` file in production to match your Heroku app's url.
Commit and push.
````
    git add channel2600/production.py
    git commit -m "Change ALLOWED_HOSTS to match Heroku app url"
    git push heroku master
````
Set up the environment variables in the Config Variables section of the app's settings (in the Heroku dashboard). You can generate a secret key [here](http://www.miniwebtool.com/django-secret-key-generator/).
````
    CLOUDINARY_URL
    RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_PRIVATE_KEY
    SECRET_KEY
````
Run the migrations.
````
    heroku run python manage.py migrate --settings=channel2600.production
````
Load the fixtures
````
    heroku run python manage.py loaddata boards.json --settings=channel2600.production
````
Check it out!
