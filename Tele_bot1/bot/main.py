from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import sysconfig
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config
import keyboard

import logging


storage = MemoryStorage()
bot = Bot(token=config.botkey, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(filename='log.txt', format=u'%(filename)s [Line:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO)

@dp.message_handler(Command('start'), state=None)
async def welcome(message):

    joined_File = open('user.txt', 'r')
    joined_Users = set()
    for line in joined_File:
        joined_Users.add(line.strip())

    if not str(message.chat.id) in joined_Users:
        joined_File = open('user.txt', 'a')
        joined_File.write(str(message.chat.id)+ "\n")
        joined_Users.add(message.chat.id)

    await bot.send_message(message.chat.id, f"Привет, *{message.from_user.first_name},* БОТ РАБОТАЕТ",
                            reply_markup=keyboard.start, parse_mode="Markdown")

@dp.message_handler(commands=['Информация'])
async def info(message):
    await bot.send_message(message.chat.id, f'Шпаргалка для пользователя {message.from_user.first_name} по языку PYTHON',
                           reply_markup=keyboard.info)
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/1.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/2.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/3.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/4.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/5.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/6.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/7.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/8.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/9.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot1/bot/photo/10.jpg'))
    await bot.send_media_group(message.chat.id, media=media)
#
@dp.message_handler(commands=['Статистика'])
async def info(message):
    await bot.send_message(message.chat.id,
                           f'Статистика для {message.from_user.first_name} пока не ведётся',
                           reply_markup=keyboard.stats)


if __name__ == '__main__':
    print('Бот запущен')
    executor.start_polling(dp)


# @bot.message_handlers(commands = ['start'])
# def start(message):
#     bot.send_message(message.chat.id,'')