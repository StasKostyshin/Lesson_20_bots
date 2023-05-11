from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)

info = types.KeyboardButton("/Информация")
stats = types.KeyboardButton("/Статистика")

start.add(stats, info)

# in_start = InlineKeyboardMarkup(row_width=2)
#
# spora = InlineKeyboardButton(text='Шпаргалка')
# shchool = InlineKeyboardButton(text='Школа',
#                               url='https://myitschool.by/')
#
# in_start.add(spora, shchool)
