import mysql.connector
from mysql.connector import errorcode
from bot.bot import Bot
from bot.ban_service import BanService
from data.banned_users_repository import BannedUsersRepository
import configparser

def main():
    # Read settings from settings.ini
    config = configparser.ConfigParser()
    config.read('config/settings.ini')

    bot_settings = config['Bot']
    TOKEN = bot_settings.get('token')
    PREFIX = bot_settings.get('prefix')
    DB_HOST = bot_settings.get('db_host')
    DB_USER = bot_settings.get('db_user')
    DB_PASSWORD = bot_settings.get('db_password')
    DB_DATABASE = bot_settings.get('db_database')

    # Establish database connection
    try:
        db_connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        print("Database connection established.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)

    # Create dependencies
    banned_users_repo = BannedUsersRepository(db_connection)
    ban_service = BanService(banned_users_repo)

    # Create bot
    bot = Bot(PREFIX, TOKEN, ban_service)

    # Run bot
    bot.run(bot.token)

if __name__ == "__main__":
    main()
