import telebot
import config
import pyowm

owm = pyowm.OWM('28a717f1c5551693eef123d9da545025', language="ru")  # you MUST provide a valid API key

bot = telebot.TeleBot(config.TOKEN)

# start
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!')

# weather
@bot.message_handler(content_types=['text'])
def weather(message):
    place = message.text
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    # weather details
    # wind
    wind = w.get_wind()['speed']
    wind = round(wind)
    # temperature
    temp = w.get_temperature('celsius')['temp']
    temp = round(temp)
    # humidity
    humidity = w.get_humidity()
    bot.send_message(message.chat.id, 'В городе ' + place + ' сейчас ' + w.get_detailed_status())
    bot.send_message(message.chat.id, 'Температура воздуха:  ' + str(temp))
    bot.send_message(message.chat.id, 'Скорость ветра:  ' + str(wind))
    bot.send_message(message.chat.id, 'Влажность:  ' + str(humidity) + '%')

    # advices
    if temp <= 10:
        bot.send_message(message.chat.id, 'Капец как холодно! Одевайся теплее или лучше посиди дома, завари чаек и посмотри фильмец😁😁😁')

    if temp <= 20 and temp >= 10:
        bot.send_message(message.chat.id, 'Хмм. Холодновасто! В трусах увы не походишь, придется надеть курточку🤪🤪🤪')

    if temp <= 30 and temp >= 20:
        bot.send_message(message.chat.id, 'Йоу! Жарища! Надевай свои самые крутые трусы, надень самые черные очки и беги покорять женские сердца! (ну или мужские)😎😎😂 ')

bot.polling(none_stop=True)
