from flask import Flask
import os

app = Flask(__name__)

# Generate a secure random key
app.secret_key = os.urandom(24)

from routes import *  # Adjust the import statement

if __name__ == '__main__':
    app.run()
