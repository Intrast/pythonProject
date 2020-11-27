import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'safdfsdgf'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'employee.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
