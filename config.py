import os

class Config(object):
    # "secret_string" = default hash
    SECRET_KY = os.environ.get('SECRET_KY') or "secret_string"
