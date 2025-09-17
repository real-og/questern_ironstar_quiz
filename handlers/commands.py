from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/max.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.hi)
        await State.tap_result.set()