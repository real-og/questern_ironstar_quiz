from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import buttons

number_btn = KeyboardButton(buttons.number, request_contact=True)
number_kb = ReplyKeyboardMarkup([[number_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

rules = ReplyKeyboardMarkup([[buttons.rules]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

begin = ReplyKeyboardMarkup([[buttons.start]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

go = ReplyKeyboardMarkup([[buttons.go]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

variants = ReplyKeyboardMarkup([[buttons.ans_1, buttons.ans_2, buttons.ans_3, buttons.ans_4]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

round2 = ReplyKeyboardMarkup([[buttons.round_2]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

result = ReplyKeyboardMarkup([[buttons.result]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

next_que = ReplyKeyboardMarkup([[buttons.next_que]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

sub = InlineKeyboardMarkup()

button_1 = InlineKeyboardButton(text=buttons.sub, url='https://t.me/ironstar_official ')
button_2 = InlineKeyboardButton(text=buttons.check_sub, callback_data='check')
sub.row(button_1)
sub.row(button_2)

feedback = ReplyKeyboardMarkup([[buttons.feedback_1, buttons.feedback_2, buttons.feedback_3]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
