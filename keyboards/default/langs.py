from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

langsMarkup = InlineKeyboardMarkup(row_width=2)
langsButtons = [
    InlineKeyboardButton(text='🇷🇺Русский', callback_data='ru'),
    InlineKeyboardButton(text='🇰🇿Қазақша', callback_data='kz')]

langsMarkup.add(*langsButtons)