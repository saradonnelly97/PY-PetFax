# config                    
from flask import Flask
app = Flask(__name__)

# index route
@app.route('/')
def index(): 
    return 'Hello, this is PetFax!'

# pet index route 
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption'

