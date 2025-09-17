from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import re
import aiotable

def is_email(string):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, string) is not None

@dp.message_handler(state=State.enter_name)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.phone, reply_markup=kb.number_kb)
    await State.waiting_for_number.set()
    name = message.text
    await aiotable.update_cell(message.from_id, 4, name)
    

@dp.message_handler(state=State.waiting_for_number, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    if not message.contact:
        await message.answer(texts.bad_phone, reply_markup=kb.number_kb)
        return

    phone_number = 'Не указал'
    if message.contact:
        phone_number = message.contact.phone_number

    await message.answer(texts.email, reply_markup=types.ReplyKeyboardRemove())
    await State.enter_email.set()
    await aiotable.update_cell(message.from_id, 5, phone_number)

    

@dp.message_handler(state=State.enter_email)
async def send_welcome(message: types.Message, state: FSMContext):
    email = message.text.strip()
    if not is_email(email):
        await message.answer(texts.bad_email)
        return
    
    await message.answer(texts.begin, reply_markup=kb.rules)
    await State.tap_rules.set()
    
    await aiotable.update_cell(message.from_user.id, 6, email)
