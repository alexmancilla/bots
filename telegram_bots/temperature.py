import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext


TELEGRAM_API_TOKEN = ''
OPENWEATHERMAP_API_KEY = ''

def weather(city: str) -> str:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        temp = data['main']['temp']
        return f'La temperatura en {city} es de {temp}°C'
    else:
        return f'No se pudo obtener la temperatura para {city}.'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola, soy un bot que te da la temperatura en Tokio, México y San Francisco. Usa los comandos /tokio, /mexico y /sanfrancisco.')

def tokio(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(weather('Tokyo'))

def mexico(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(weather('Mexico City'))

def sanfrancisco(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(weather('San Francisco'))

def main():
    updater = Updater(TELEGRAM_API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('tokio', tokio))
    dp.add_handler(CommandHandler('mexico', mexico))
    dp.add_handler(CommandHandler('sanfrancisco', sanfrancisco))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
