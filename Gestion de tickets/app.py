from flask import Flask
from requests import Flask

app = Flask(__name__)
app.run= debug=True

if __name__ == '__main__':
    app.run()