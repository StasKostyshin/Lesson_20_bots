from aiogram import Bot, executor, Dispatcher, types
import logging

from config import TOKEN_API
from keyboard import ikb, kb, b2

bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot)

logging.basicConfig(filename='log.txt', format=u'%(filename)s [Line:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO)

async def on_startup(_):
    print('Я запущен!')

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    joined_File = open('user.txt', 'r')
    joined_Users = set()
    for line in joined_File:
        joined_Users.add(line.strip())

    if not str(message.chat.id) in joined_Users:
        joined_File = open('user.txt', 'a')
        joined_File.write(str(message.chat.id)+ "\n")
        joined_Users.add(message.chat.id)

    await message.answer(text='Добро пожаловать',
                         reply_markup=kb)

@dp.message_handler(commands=['cheat_sheet'])
async def info(message):
    await bot.send_message(message.chat.id, f'Шпаргалка для пользователя {message.from_user.first_name} по языку PYTHON',
                           reply_markup=b2)
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/1.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/2.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/3.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/4.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/5.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/6.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/7.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/8.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/9.jpg'))
    media.attach_photo(types.InputFile('C:/Users/dizba/PycharmProjects/Lesson 20 bots/Tele_bot2/photo/10.jpg'))

    await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(commands=["links"])
# async def links_command(message: types.Message):
async def links_command(message):
    await message.answer(text='Выберите опцию',
                         reply_markup=ikb)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup = on_startup)