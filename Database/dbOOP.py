import sqlite3

class Users:
    def __init__(self, id=-1, username="", email=""):
        self.id = id
        self.username = username
        self.email = email
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()


    def load_user(self, user_id):
        self.cursor.execute("""
        SELECT * FROM users
        WHERE id = {}
        """.format(id))

        results = self.cursor.fetchone()

        self.id = id
        self.username = results[1]
        self.email = results[2]

    def insert_user(self):
        self.cursor.execute("""
        INSERT INTO users VALUES
        ({},'{}','{}')
        """.format(self.id, self.username, self.email))

        self.conn.commit()
        self.conn.close()

#Load user
# u1 = Users()
# u1.load_user(1)
# print(u1.id)
# print(u1.username)
# print(u1.email)

#Insert new User
u1 = Users(3,"Pete Steele", "pete.steele@email.com")
u1.insert_user()
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
print(results)

conn.close()
