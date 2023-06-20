import datetime
import os.path

from dotenv import load_dotenv
load_dotenv()
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

from spreadsheets import spreadsheet_manager
from keyboard import kb_again, kb_again_text

class FSM(StatesGroup):
  waiting_for_answer = State()

def init_bot():
  storage = MemoryStorage()
  bot = Bot(token=os.getenv('TG_BOT_TOKEN'))
  dp = Dispatcher(bot=bot, storage=storage)

  @dp.message_handler(commands=['start'])
  @dp.message_handler(lambda message: message.text and message.text == kb_again_text)
  async def on_start(message: types.Message):
    await message.reply(f"Салют Товарищ! Вижу ты узнал невыдуманную новость о которой не можешь молчать! Мы расскажем о ней людям, если она интересна. Пришли мне текст новости.", reply_markup=ReplyKeyboardRemove())
    await FSM.waiting_for_answer.set()

  @dp.message_handler(state=FSM.waiting_for_answer)
  async def on_getting_answer(message: types.Message, state: FSMContext):
    username = 'https://t.me/' + message.from_user.username
    content = message.text
    time_now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    spreadsheet_manager.append_row([username, content, time_now])
    await message.reply(f"Спасибо! Наши лаборатории на Нибиру активированы. Проверяем новость которую ты прислал 🌖", reply_markup=kb_again)
    await state.finish()

  executor.start_polling(dp, skip_updates=True)