import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_user_name(cls, username):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        sql = 'SELECT * FROM users WHERE user_name=?'
        result = c.execute(sql, (username,))
        record = result.fetchone()
        if record:
            user = cls(*record)
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def find_user_id(cls, _id):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        sql = 'SELECT * FROM users WHERE user_id=?'
        result = c.execute(sql, (_id,))
        record = result.fetchone()
        if record:
            user = cls(*record)
        else:
            user = None
        conn.close()
        return user

