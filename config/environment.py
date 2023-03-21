
# ! This is the URI we use to talk to the database.
# ! Not: sqlalchemy does not make gifts_db for us,
# ? we need to run the command "createdb gifts_db".

from os import environ
# import load_env, this function loads an env file from a path.
from dotenv import load_dotenv

# Here we get a filepath from either the ENV_FILE passed through, or .env as a default. 
ENVIRONMENT_FILE = environ.get('ENV_FILE') or '.env'

# Here we are passing through the env file to load from. override=True means the env file will override .env, if .env exists. 
load_dotenv(ENVIRONMENT_FILE, override=True)

# Now, environ.get will retrieve variables from the file we provided.
db_URI = environ.get('DB_URI')
secret = environ.get('SECRET')
# db_URI = 'postgresql://localhost:5432/gifts_db'
# secret = 'correcthorsebatterystaple'
