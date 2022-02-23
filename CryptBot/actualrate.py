import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

TOKEN = "Your token"

bot = telebot.TeleBot(TOKEN)

class Rate():

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    def actual_rate(self, link, coin):

        while True:

            response = requests.get(link, headers=self.headers)
            soup = BeautifulSoup(response.text, 'lxml')
            rate = soup.findAll("span", {"class": "text-2xl"})
            rate = rate[0].text
            final_rate = 'Курс криптовалюты ' + coin +  ' составляет: ' + '\n' + '➡ ' + str(rate) + " $" + ' ⬅'+ '\n' + 'Удачных вам торгов!'

            return final_rate


    def actual_rate_return(self, call, link, coin):

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=self.actual_rate(link=link, coin=coin))

