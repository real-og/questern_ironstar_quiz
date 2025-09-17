from loader import dp, bot, CHANNEL_ID
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import re
import random
import buttons
import aiotable

@dp.message_handler(state=State.tap_rules)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.rules, reply_markup=kb.begin)
    await State.tap_begin.set()
    

@dp.message_handler(state=State.tap_begin)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.round1, reply_markup=kb.go)
    await State.tap_round1.set()
    

@dp.message_handler(state=State.tap_round1)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_1, reply_markup=kb.variants)
    await State.que_1.set()
    

@dp.message_handler(state=State.que_1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '3':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 7, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 7, '0')
    await message.answer(texts.comment_1)
    await message.answer(texts.question_2, reply_markup=kb.variants)
    await State.que_2.set()
    

@dp.message_handler(state=State.que_2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '2':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 8, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 8, '0')
    await message.answer(texts.comment_2)
    await message.answer(texts.question_3, reply_markup=kb.variants)
    await State.que_3.set()
    

@dp.message_handler(state=State.que_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '4':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 9, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 9, '0')
    await message.answer(texts.comment_3)
    await message.answer(texts.question_4, reply_markup=kb.variants)
    await State.que_4.set()
    

@dp.message_handler(state=State.que_4)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '1':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 10, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 10, '0')
    await message.answer(texts.comment_4)
    await message.answer(texts.question_5, reply_markup=kb.variants)
    await State.que_5.set()
    

@dp.message_handler(state=State.que_5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '2':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 11, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 11, '0')
    await message.answer(texts.comment_5, reply_markup=kb.round2)
    await State.round2.set()
    

@dp.message_handler(state=State.round2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == buttons.round_2:
        await message.answer(texts.round2)
        await message.answer(texts.question_6, reply_markup=kb.variants)
    else:
        await message.answer('Жми на кнопку внизу экрана ⤵️ ', reply_markup=kb.round2)
    await State.que_6.set()
    

@dp.message_handler(state=State.que_6)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '2':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 12, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 12, '0')
    await message.answer(texts.comment_6)
    await message.answer(texts.question_7, reply_markup=kb.variants)
    await State.que_7.set()
    

@dp.message_handler(state=State.que_7)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '4':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 13, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 13, '0')
    await message.answer(texts.comment_7)
    await message.answer(texts.question_8, reply_markup=kb.variants)
    await State.que_8.set()
    

@dp.message_handler(state=State.que_8)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '3':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 14, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 14, '0')
    await message.answer(texts.comment_8)
    await message.answer(texts.question_9, reply_markup=kb.variants)
    await State.que_9.set()
    

@dp.message_handler(state=State.que_9)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '1':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 15, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 15, '0')
    await message.answer(texts.comment_9)
    await message.answer(texts.question_10, reply_markup=kb.variants)
    await State.que_10.set()
    

@dp.message_handler(state=State.que_10)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '4':
        await message.answer(random.choice(texts.corrects))
        await aiotable.update_cell(message.from_user.id, 16, '1')
    else:
        await message.answer(random.choice(texts.wrongs))
        await aiotable.update_cell(message.from_user.id, 16, '0')
    await message.answer(texts.comment_10)
    await message.answer(texts.end, reply_markup=kb.result)
    await State.tap_result.set()
    

@dp.message_handler(state=State.tap_result)
async def send_welcome(message: types.Message, state: FSMContext):
    
    points = await aiotable.get_score(message.from_user.id)
    await message.answer(texts.generate_result(points), reply_markup=kb.sub)
    await State.tap_sub.set()
    

@dp.callback_query_handler(state=State.tap_sub)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    tapped_butt = callback.data
    user_status = await bot.get_chat_member(CHANNEL_ID, callback.from_user.id)

    if user_status['status'] == 'left':
        await callback.message.answer(texts.not_subscribed, reply_markup=kb.sub)
        return
    if tapped_butt == 'check':
        number = await aiotable.get_row_number(callback.from_user.id)
        await callback.message.answer(texts.generate_num(number))
        await callback.message.answer(texts.thanks, reply_markup=kb.feedback)
        await State.feedback.set()
        
@dp.message_handler(state=State.feedback)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.bye)
    await State.ended.set()
    await aiotable.update_cell(message.from_user.id, 17, message.text)
        
        
   