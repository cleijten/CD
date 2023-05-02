# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world...! It works finally again!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')