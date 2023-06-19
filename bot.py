import os.path
import logging

from dotenv import load_dotenv
load_dotenv()
from aiogram import Bot, Dispatcher, executor, types
from spreadsheets import spreadsheet_reader

def on_startup():
  print('Starting up...')

def init_bot():
  bot = Bot(token=os.getenv('TG_BOT_TOKEN'))
  dp = Dispatcher(bot=bot)

  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

  @dp.message_handler(commands=['start'])
  async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    logging.info(f'{user_id=} {user_fullname=}')
    await message.reply(f"Салют Товарищ! Вижу ты узнал невыдуманную новость о которой не можешь молчать! Мы расскажем о ней людям, если она интересна. Пришли мне текст новости.")

  @dp.message_handler(commands=['test'])
  async def start_handler(message: types.Message):
    spreadsheet_reader.print_from_sheet()
    message.reply(f"Тестовая команда")