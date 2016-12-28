from channel2600.settings import *
import dj_database_url

DEBUG=False
ALLOWED_HOSTS = ["https://channel2600.herokuapp.com", "channel2600.herokuapp.com"]
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
