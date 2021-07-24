from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask

from api.controller import speech

app = Flask(__name__, static_url_path='')

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# api routes
app.register_blueprint(speech.app)

# index page
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug = True)
