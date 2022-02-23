import telebot
import requests
from telebot import types
import requests
import time
from bs4 import BeautifulSoup



TOKEN = "Your token"

bot = telebot.TeleBot(TOKEN)

class Notifications():

    BTCUSD = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&sxsrf=APq-WBuUzmrykcgJA6jUTKg1Qyw3uBnvOQ%3A1643979885956&ei=bST9YYryOduVjgb6vIXICw&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYATIHCCMQsAMQJzIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIKCAAQRxCwAxDJAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQzIHCAAQsAMQQzISCC4QxwEQ0QMQyAMQsAMQQxgAMhIILhDHARDRAxDIAxCwAxBDGAAyEgguEMcBENEDEMgDELADEEMYADISCC4QxwEQowIQyAMQsAMQQxgAMhIILhDHARDRAxDIAxCwAxBDGABKBAhBGABKBAhGGAFQAFgAYPQIaAFwAngAgAEAiAEAkgEAmAEAyAERwAEB2gEGCAAQARgI&sclient=gws-wiz'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    current_price = 0
    difference = 10 # Разница после которой будет отправлено сообщение на почту

    def __init__ (self):
			# Установка курса валюты при создании объекта
        self.current_price = float(self.get_cryptprice())

	# Метод для получения курса валюты
    def get_cryptprice(self):
		# Парсим всю страницу
        page = requests.get(self.BTCUSD, headers=self.headers)

		# Разбираем через BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')

		# Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "pclqee"})

        course = convert[0].text
        first_step = course.replace("\xa0", " ")
        second_step = first_step.replace(" ", "")
        third_step = second_step.replace(",", ".")
        final_rate = float(third_step)

        return final_rate

    def get_percents(self):
        full_page = requests.get(self.BTCUSD, headers=self.headers)

        		# Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        		# Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"jsname": "rfaVEf"})

        final_percents = convert[0].text

        return final_percents

    def check_price(self, call):
        currency = float(self.get_cryptprice())
        percents = self.get_percents()
        if currency >= self.current_price + self.difference:
            bot.send_message(call.message.chat.id, '⬆ Курс монеты Bitcoin вырос ⬆' + '\n' + 'Сейчас он составляет: ' + str(currency) + '$')
            self.current_price = currency
        elif currency <= self.current_price - self.difference:
            bot.send_message(call.message.chat.id, '⬇ Курс монеты Bitcoin упал ⬇' + '\n' +  'Сейчас он составляет: ' + str(currency) + '$')
            self.current_price = currency

        time.sleep(60)
        self.check_price(call=call)
