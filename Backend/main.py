from twitch_bot import Bot
from flask_server import app



# start flask in flask.py

if __name__ == '__main__':
    bot = Bot()
    bot.run()
    app.run()