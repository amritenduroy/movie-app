from flask_restful import Resource
import sqlite3

class Trends(Resource):
    def get(self, genres):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        sql = """                  
                SELECT
                    a.title,
                    AVG(b.rating) AS avg_rating
                FROM 
                    movies a,
                    ratings b
                WHERE 
                    a.movie_id = b.movie_id
                    AND
                    a.genres LIKE ?
                GROUP BY a.title
                ORDER BY avg_rating DESC
                LIMIT 5
            """
        param = "%" + str(genres) + "%"
        results = c.execute(sql, (param,))
        records = results.fetchall()
        if records:
            result = {'Genre': genres, 'movies': []}
            for record in records:
                result['movies'].append({
                                        'title': record[0], 
                                        'average_rating': record[1]
                                        })
            return result, 200
        conn.close()
        return {
            'message': 'No records corresponding to the genres %s'%(genres,)
        }, 400
