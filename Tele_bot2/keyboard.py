from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='school',
                           url='https://myitschool.by/')
ib2 = InlineKeyboardButton(text='python',
                           url='https://www.python.org/?hl=RU')
ikb.add(ib1).add(ib2)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
b = KeyboardButton(text='/links')
b2 = KeyboardButton(text='/cheat_sheet')
kb.add(b,b2)