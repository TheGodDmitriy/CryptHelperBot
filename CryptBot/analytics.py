import telebot
from telebot import types

TOKEN = "Your token"

bot = telebot.TeleBot(TOKEN)

class Analytics():

    def main_analytics(self, call, link):

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=link)
