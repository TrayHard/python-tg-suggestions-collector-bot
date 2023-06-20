

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_again_text = "Прислать ещё"
kb_again = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(kb_again_text))