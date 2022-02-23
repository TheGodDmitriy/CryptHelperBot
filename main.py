import telebot
import requests
from telebot import types
import time
from bs4 import BeautifulSoup
from notifications import Notifications
from analytics import Analytics
from random import randint
from actualrate import Rate

TOKEN = "Your token"

bot = telebot.TeleBot(TOKEN)


class Notice:

    @bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "⛽уведомления")
    def creating_button_notifications(message):
        keyboard = types.InlineKeyboardMarkup()
        coin_btc = types.InlineKeyboardButton(text='Bitcoin', callback_data='Bitcoin_Notifications')
        keyboard.add(coin_btc)
        bot.send_message(message.chat.id, '😞Сейчас, мы можем включить уведомления только для монеты Bitcoin😞', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Bitcoin_Notifications'))
    def bitcoin_notifications(call):
        coast = Notifications()
        price = float(coast.get_cryptprice())
        fin_price = str(price) + "$"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отлично, вы запустили уведомления.' + '\n' + 'Курс BTC на данный момент: ' + fin_price)
        coast.check_price(call=call)

class Analysis:

    @bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "👩‍💻аналитика")
    def creating_button_analytics(message):
        keyboard = types.InlineKeyboardMarkup()
        first_coin = types.InlineKeyboardButton(text='Bitcoin', callback_data='Bitcoin_Analytics')
        second_coin = types.InlineKeyboardButton(text='Ethereum', callback_data='Ethereum_Analytics')
        third_coin = types.InlineKeyboardButton(text='XRP', callback_data='XRP_Analytics')
        fourth_coin = types.InlineKeyboardButton(text='Cardano', callback_data='Cardano_Analytics')
        fifth_coin = types.InlineKeyboardButton(text='Tether', callback_data='Tether_Analytics')
        sentence = '''🔻Выбериет одну из 5 криптовалют🔻'''
        keyboard.add(first_coin, second_coin, third_coin, fourth_coin, fifth_coin)
        bot.send_message(message.chat.id, sentence, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Bitcoin_Analytics'))
    def bitcoin_analytics(call):
        Analytics().main_analytics(call=call, link='https://ru.tradingview.com/symbols/BTCUSD/technicals/')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Ethereum_Analytics'))
    def ethereum_analytics(call):
        Analytics().main_analytics(call=call, link='https://ru.tradingview.com/symbols/ETHUSD/technicals/')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('XRP_Analytics'))
    def xrp_analytics(call):
        Analytics().main_analytics(call=call, link='https://ru.tradingview.com/symbols/XRPUSD/technicals/')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Cardano_Analytics'))
    def cardano_analytics(call):
        Analytics().main_analytics(call=call, link='https://ru.tradingview.com/symbols/ADAUSDT/technicals/')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Tether_Analytics'))
    def tether_analytics(call):
        Analytics().main_analytics(call=call, link='https://ru.tradingview.com/symbols/USDTUSD/technicals/')

class Game:

    @bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "🎩мини-игра")
    def game(message):
        keyboard = types.InlineKeyboardMarkup()
        coinflip = types.InlineKeyboardButton(text='Бросок', callback_data='Coin_UP')
        keyboard.add(coinflip)
        bot.send_message(message.chat.id, '💎Подбросьте монету💎', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Coin_UP'))
    def game_start(call):
        coin = randint(1, 2)
        if coin == 1:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='💰У вас орел, можете покупать криптовалюту💰')
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='💀У вас решка, бот не советует сегодня инвестировать.💀')

class Course:

    @bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "📈курс")
    def creating_button_course(message):
        keyboard = types.InlineKeyboardMarkup()
        first_coin = types.InlineKeyboardButton(text='Bitcoin', callback_data='Bitcoin_Course')
        second_coin = types.InlineKeyboardButton(text='Ethereum', callback_data='Ethereum_Course')
        third_coin = types.InlineKeyboardButton(text='XRP', callback_data='XRP_Course')
        fourth_coin = types.InlineKeyboardButton(text='Cardano', callback_data='Cardano_Course')
        fifth_coin = types.InlineKeyboardButton(text='Tether', callback_data='Tether_Course')
        sentence = '''🔻Выбериет одну из 5 криптовалют🔻'''
        keyboard.add(first_coin, second_coin, third_coin, fourth_coin, fifth_coin)
        bot.send_message(message.chat.id, sentence, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Bitcoin_Course'))
    def bitcoin_course(call):
        Rate().actual_rate_return(call=call, link='https://ru.investing.com/crypto/bitcoin/btc-usd', coin='Bitcoin')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Ethereum_Course'))
    def ethereum_course(call):
        Rate().actual_rate_return(call=call, link='https://ru.investing.com/crypto/ethereum/eth-usd', coin='Ethereum')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('XRP_Course'))
    def xrp_course(call):
        Rate().actual_rate_return(call=call, link='https://ru.investing.com/crypto/xrp/xrp-usd', coin='XRP')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Cardano_Course'))
    def cardano_course(call):
        Rate().actual_rate_return(call=call, link='https://ru.investing.com/crypto/cardano/ada-usd', coin='Cardano')

    @bot.callback_query_handler(func=lambda call: call.data.startswith('Tether_Course'))
    def tether_course(call):
        Rate().actual_rate_return(call=call, link='https://ru.investing.com/crypto/tether/usdt-usd', coin='Tether')

class Information:

    @bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "💼информация")
    def main_information(message):
        info = '''👨‍🏫Этот бот создан специально для людей, кто инетерсуется или уже активно работает с криптовалютой.

Бот предоставляет возможность:
    - Получать актуальный курс 5 популярных криптовалют
    - Получить доступ к анализу криптовалют
    - Сыграть в Мини-Игру, если не уверенны в своих действиях с криптовалютой
    - Подключить уведомления и получать их, когда курс повысится или понизиться

⛑Наша основная цель - помочь людям. Бот не дает возможности покупать или продавать криптовалюту, он лишь только помогает людям сделать правильный выбор'''
        bot.send_message(message.chat.id, info)

# Создание объекта и вызов метода
if __name__ == '__main__':

    @bot.message_handler(commands=["start"])
    def first_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        analytics = types.KeyboardButton('👩‍💻Аналитика')
        rate = types.KeyboardButton('📈Курс')
        notifications = types.KeyboardButton('⛽Уведомления')
        game = types.KeyboardButton('🎩Мини-Игра')
        information = types.KeyboardButton('💼Информация')
        markup.add(analytics, rate, notifications, game, information)
        bot.send_message(message.chat.id, '''😀Вас приветствует CryptMoney😀

Этот бот создан для помощи инвесторам, на выбор вам предлагается 5 клавиш. Для начала, советуем вам ознакомиться с 💼Информацией💼.

🤑Удачных вам торгов🤑''', reply_markup=markup)

    bot.polling()
