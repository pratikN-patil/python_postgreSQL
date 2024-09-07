import os
from dotenv import load_dotenv

load_dotenv('environment.txt')


DATABASE_CONFIG = {
    'host' : os.getenv("DB_HOST"),
    'dbname' : os.getenv("DB_NAME"),
    'user' : os.getenv("DB_USER"),
    'password' : os.getenv("DB_PASSWORD"),
    'port' : os.getenv("DB_PORT")
}