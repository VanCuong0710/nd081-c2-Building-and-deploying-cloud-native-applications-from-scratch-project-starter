#--------- Flask settings
SERVER_HOST = '127.0.0.1' # Update this for the appropriate front-end website when up
SERVER_PORT = 5000
FLASK_DEBUG = True # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'


API_URL = "https://cuongnv93funcapp.azurewebsites.net/api"
