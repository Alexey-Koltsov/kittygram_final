import os

SECRET_KEY = os.getenv('SECRET_KEY')


# DEBUG = True if 'true' == os.getenv('DEBUG').lower() else False

print(os.getenv('DEBUG'))

# ALLOWED_HOSTS = os.getenv('SECRET_KEY').split()

print(os.getenv('DB_PORT'))
