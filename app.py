import os

import updater as updater
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, It's IPay API!"


if __name__ == '__main__':
    app.run(debug=True)
