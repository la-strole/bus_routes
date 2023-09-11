import os

from telebot import TeleBot

# Add bot instance
token = os.getenv('TELEGRAM_BOT_TOKEN')
assert token
bot = TeleBot(token)


if __name__ == "__main__":
    bot.infinity_polling()
