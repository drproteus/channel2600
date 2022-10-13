# channel2600 // 2600chan

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
