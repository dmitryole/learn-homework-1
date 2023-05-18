"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
# Импортируем нужные компоненты
import logging
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import settings


# Конфигурация логов
logging.basicConfig(filename='bot.log',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO,
                    encoding='utf-8')

# Настройки прокси (неактуально)
"""
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}
"""

def talk_to_me(update, context):
  user_text = update.message.text 
  print(user_text)
  logging.info(user_text)
  update.message.reply_text(user_text)

def greet_user(update, context):
  print('Вызван /start')
  logging.info("Call /start")
  update.message.reply_text('Hello user! You called the command /start')

def get_planet(update, context):
  try:
        print('Вызван /planet')
        user_message = update.message.text.split()
        #Получаем now из библиотеки datetime, возможно в переменной context есть дата
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        #Вытаскиваем название планеты из сообщения
        user_planet = user_message[1].capitalize()
        logging.info(f"Call /planet {user_planet}")
        #Присваиваем переменную name planet в атрибут
        ephem_name_planet = getattr(ephem, user_planet)
        #Получить координаты планеты
        planet = ephem_name_planet(now)
        #Запрос созвездия
        constellation = (ephem.constellation(planet))[1]
        update.message.reply_text(f'{user_planet} in the constellation {constellation}')
  except AttributeError:
      update.message.reply_text(f'Check planet name')


def main():
  # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
  mybot = Updater(settings.API_KEY, use_context=True)
  
  # Обработчики
  dp = mybot.dispatcher
  dp.add_handler(CommandHandler("start", greet_user))
  dp.add_handler(CommandHandler("planet", get_planet))
  dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
  # Командуем боту начать ходить в Telegram за сообщениями
  mybot.start_polling()
  # Запускаем бота, он будет работать, пока мы его не остановим принудительно
  mybot.idle()


if __name__ == "__main__":
  main()
