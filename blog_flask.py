from flask import Flask

from config import DebugConfig

app = Flask(__name__)
app.config.from_object(DebugConfig)


@app.route('/')
def index():
    return 'Hello World!alkd 哥斯达黎加slkjaf;ldjf'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
