from flask_restful import Resource
import sqlite3
from random import sample

class RandomMovies(Resource):
    def get(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        sql = """                  
                SELECT
                    DISTINCT a.title, a.genres
                FROM 
                    movies a,
                    ratings b
                WHERE 
                    a.movie_id = b.movie_id
            """
        results = c.execute(sql)
        records = results.fetchall()
        if records:
            selected = sample(list(range(len(records))), 20)
            result = {'movies':[]}
            i = 0
            for record in records:
                if i in selected:
                    result['movies'].append({
                                        'title': record[0],
                                        'genres': record[1]
                                        })
                i+=1
            return result, 200
        conn.close()
        return {
            'message': 'No movie record found'
        }, 400
