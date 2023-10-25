from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    
    @app.route('/pets')
    def pets():
        return 'These are the pets we have for adoption!'

    return app
