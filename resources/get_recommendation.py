from flask_restful import Resource
import sqlite3
from random import sample
from models.ml import getRatings
from flask_jwt import JWT, jwt_required

class GetMovies(Resource):
    @jwt_required()
    def get(self, user_id, movie_id):
        try:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            sql = """                  
                    SELECT
                        a.movie_id,
                        a.title,
                        b.user_id,
                        b.rating
                    FROM 
                        movies as a 
                        LEFT JOIN 
                        (SELECT movie_id, user_id, rating from ratings WHERE user_id = ?) as b
                        ON a.movie_id = b.movie_id
                    WHERE 
                        a.movie_id = ?
                """
            results = c.execute(sql, (user_id, movie_id))
            record = results.fetchone()
            if record:
                result = {  'user_id':user_id,
                            'movie_id':movie_id,
                            'title':record[1],
                            'rating':record[3],
                            'predicted_rating': getRatings(int(user_id), int(movie_id))}
                conn.close()
                return result, 200
            conn.close()
            return {
                'message': 'Invalid user id or movie id!'
            }, 400
        except:
            return {
                'message': 'Invalid user id or movie id!'
            }, 400
