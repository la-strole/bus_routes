import os

from telebot import TeleBot

import callback_handler
import command_handler
import message_handler

# Add a bot instance.
token = os.getenv("TELEGRAM_BOT_TOKEN")

assert token
bot = TeleBot(token)

command_handler.command_handler(bot)
message_handler.message_handler(bot)
callback_handler.callback_handler(bot)

if __name__ == "__main__":
    bot.infinity_polling()
