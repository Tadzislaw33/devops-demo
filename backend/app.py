from flask import Flask
import os
from pymongo import MongoClient

app = Flask(__name__)

mongo_host = os.environ.get('MONGODB_HOST', 'localhost')
client = MongoClient(f'mongodb://{mongo_host}:27017/')
db = client.mydatabase

@app.route('/up')
def up():
    return 'Backend is up!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
