# channel2600 // 2600chan

In an effort to stop myself going to dumb sites on the internet, I decided to make my own dumb site.

It's built with Django. Try it out!

## Local Install

### Requirements

* python2
* virtualenv
* virtualenvwrapper (optional)
* Cloudinary account
* ReCaptcha account

1. Set up the virtualenv, with virtualenvwrapper:
    mkvirtualenv 2600chan -p /path/to/python2
2. Checkout the local branch so requirements.txt doesn't bring in postgres module, dev uses sqlite3.
    git checkout local
3. Install requirements.
    pip install -r requirements.txt
4. Run the migrations.
    python manage.py migrate
5. Set up the seed boards (optional, or you can adjust them in boards.json).
    python manage.py loaddata boards.json
6. Set up environment variables for your Cloudinary and ReCaptcha accounts.
    export CLOUDINARY_URL=
    export RECAPTCHA_PRIVATE_KEY=
    export RECAPTCHA_PUBLIC_KEY=
7. Run the server and navigate to localhost:8000 (or address:port as specified).
    python manage.py runserver

## Heroku Install

### Requirements

* Cloudinary account
* ReCaptcha account
* Heroku dyno setup

Assuming you've already cloned the repository, branch is set to master, and you've also set up heroku-cli for this repository:

1. Change the `ALLOWED_HOSTS` file in production to match your Heroku app's url.
2. Commit and push.
    git add channel2600/production.py
    git commit -m "Change ALLOWED_HOSTS to match Heroku app url"
    git push heroku master
3. Set up the environment variables in the Config Variables section of the app's settings (in the Heroku dashboard). You can generate a secret key [here](http://www.miniwebtool.com/django-secret-key-generator/).
    CLOUDINARY_URL
    RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_PRIVATE_KEY
    SECRET_KEY
4. Run the migrations.
    heroku run python manage.py migrate --settings=channel2600.production
5. Load the fixtures
    heroku run python manage.py loaddata boards.json --settings=channel2600.production
6. Check it out!

