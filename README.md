# Discord Auto Ban Banned Users

## Description
This Discord bot bans users automatically if they are on a predefined banned users list when they join the server.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PartTimeLegend/discord-auto-ban-banned-users.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `settings.ini` file in the `config/` directory and fill it with your bot token and database connection details. Use `config/settings.ini.example` as a template.
4. Set up your database with the necessary tables. You can use the SQL script provided in `MariaDB/schema.sql`.

## Configuration
The `settings.ini` file in the `config/` directory contains the configuration for the bot. Here's an example of its structure:
```ini
[Bot]
token = YOUR_DISCORD_BOT_TOKEN_HERE
prefix = !
db_host = YOUR_DB_HOST
db_user = YOUR_DB_USER
db_password = YOUR_DB_PASSWORD
db_database = YOUR_DB_NAME
```

## Usage
To run the bot, execute the following command:
```bash
python main.py
```

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
