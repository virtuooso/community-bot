from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

interests = {'Творческое 👨‍🎨': 'https://t.me/CreativeUralsk',
    'Техники 👩‍💻': 'https://t.me/TechUralsk','Спорт ⚽': 'https://t.me/SportUralsk',
    'Наука ⚛': 'https://t.me/ScienceUralsk'}

interestsMarkup = InlineKeyboardMarkup(row_width=2)
interestButtons = [InlineKeyboardButton(i, url=j) for (i, j) in interests.items()]
interestsMarkup.add(*interestButtons)