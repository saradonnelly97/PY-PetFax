# config                    
from flask import Flask, render_template
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pr0gr355@localhost:5432/petfacts'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index(): 
        return render_template('home.html')

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app