from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import aiotable
from datetime import datetime, timedelta, timezone

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/max.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.hi)
        await State.enter_name.set()
        await state.update_data(sum='0') 
        
        username = str(message.from_user.username)
        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")

        await aiotable.append_user_strict(str(datetime_str), str(message.from_user.id), str(username))
        

@dp.message_handler(commands=['terms'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('doc.pdf', 'rb') as f:
        await message.answer_document(f)