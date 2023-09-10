import telebot
import os
import time
import wikipedia as wk
import requests
from telebot import types
from strings import *
from bs4 import BeautifulSoup

bot = telebot.TeleBot(token='6528475302:AAFNSkqcJcCMD6rOWVBl9qK6GnRa3v6dCYc')

@bot.message_handler(commands=['start'])
def Start(message):
    bot.send_message(message.chat.id, info)

@bot.message_handler(commands=['getid'])
def GetId(message):
    bot.send_message(message.chat.id, f'Ваш айди: {message.from_user.id}\n Спасибо за использование :)')

@bot.message_handler(commands=['translate'])
def Translate(message):
    bot.send_message(message.chat.id, text='Временно недоступен')

@bot.message_handler(commands=['wiki'])
def Wikipedia(message):
    bot.send_message(message.chat.id, 'Ваш запрос обрабатывается! Пожалуйста подождите...')
    try:
        argument = message.text.split(' ', 1)[1]
        wk.set_lang('ru')
        answer = wk.summary(argument)
        bot.send_message(message.chat.id, answer)
    except: bot.send_message(message.chat.id, 'Ваш запрос пустой! Пример запроса /wiki Илон Маск')
        
@bot.message_handler(commands=['inst'])
def InstDownloader(message):
    bot.send_message(message.chat.id, 'Ваш запрос обрабатывается! Пожалуйста подождите...')
    url = message.text.split(' ', 1)[1]
    from instdownloader import inst
    inst(url=url)
    openedimg = open(f"img.jpeg", 'rb')
    bot.send_document(message.chat.id, openedimg)
    openedimg.close()

def Main():
    bot.infinity_polling()

if __name__ == '__main__':
    Main()