import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Главная страница'


if __name__ == '__main__':
    app.run()