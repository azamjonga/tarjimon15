from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button = InlineKeyboardMarkup()
btn = InlineKeyboardButton(text="🇺🇿 Uzbekcha->🇺🇸 Inglizcha", callback_data='uzen')
btn1 = InlineKeyboardButton(text="🇺🇸 Inglizcha->🇺🇿 Uzbekcha", callback_data='enuz')
btn2 = InlineKeyboardButton(text="🇺🇿Uzbekcha->🇷🇺 Ruscha", callback_data='uzru')
btn3 = InlineKeyboardButton(text="🇷🇺 Ruscha->🇺🇿 Uzbekcha", callback_data='ruuz')
btn4 = InlineKeyboardButton(text="🇺🇿 Uzbekcha->🇹🇷 Turkcha", callback_data='uztr')
btn5 = InlineKeyboardButton(text="🇹🇷 Turkcha->🇺🇿 Uzbekcha", callback_data='truz')
btn6 = InlineKeyboardButton(text="🇺🇿 Uzbekcha->🇸🇦 Arabcha", callback_data='uzar')
btn7 = InlineKeyboardButton(text="🇸🇦 Arabcha->🇺🇿 Uzbekcha", callback_data='aruz')
button.add(btn, btn1).add(btn2, btn3).add(btn4, btn5).add(btn6, btn7)