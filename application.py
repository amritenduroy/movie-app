from flask import Flask
from flask_restful import Api
from models.trends import Trends
from models.random_movies import RandomMovies
from models.security import authenticate, identity
from resources.get_recommendation import GetMovies
from flask_jwt import JWT

app = Flask(__name__)
app.secret_key = "MySecretKeyIsFunny"
api = Api(app)

jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(Trends, '/trends/top5/<string:genres>')
api.add_resource(RandomMovies, '/user/selection/')
api.add_resource(GetMovies, '/recommendation/<string:user_id>/<string:movie_id>')

app.run(port=5000)