import waitress

from nuts_and_bolts import create_app

waitress.serve(create_app(), host='127.0.0.1', port=5000, url_scheme='https')
