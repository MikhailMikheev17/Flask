from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello, world'

@app.route('/index')
def index():
    return "It's my first project"


if __name__ == '__main__':
    app.run()