import mysql.connector

class BannedUsersRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def load_banned_users(self):
        banned_users = []
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT user_id FROM banned_users")
            banned_users = [user_id[0] for user_id in cursor.fetchall()]
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error loading banned users: {err}")
        return banned_users
