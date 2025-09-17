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
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 

    else:
        await message.answer(random.choice(texts.wrongs))
    await message.answer(texts.comment_1)
    with open('images/1.jpg', 'rb') as photo:
        await message.answer_photo(photo)
    await message.answer('Готов к следующему вопросу? Жми на кнопку внизу экрана ⤵️', reply_markup=kb.next_que)
    await State.que_2_.set()
    


@dp.message_handler(state=State.que_2_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_2, reply_markup=kb.variants)
    await State.que_2.set()

    

@dp.message_handler(state=State.que_2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '2':
        await message.answer(random.choice(texts.corrects))
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))

    await message.answer(texts.comment_2)
    with open('images/2.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kb.next_que)

    await State.que_3_.set()
    

@dp.message_handler(state=State.que_3_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_3, reply_markup=kb.variants)
    await State.que_3.set()
    

@dp.message_handler(state=State.que_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '4':
        await message.answer(random.choice(texts.corrects))
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))
    await message.answer(texts.comment_3)
    with open('images/3.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kb.next_que)
    await State.que_4_.set()
    

@dp.message_handler(state=State.que_4_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_4, reply_markup=kb.variants)
    await State.que_4.set()

@dp.message_handler(state=State.que_4)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '1':
        await message.answer(random.choice(texts.corrects))
     
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))
    await message.answer(texts.comment_4, disable_web_page_preview=True)
    with open('images/4.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kb.next_que)
    await State.que_5_.set()
    

@dp.message_handler(state=State.que_5_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_5, reply_markup=kb.variants)
    await State.que_5.set()
    

@dp.message_handler(state=State.que_5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '3':
        await message.answer(random.choice(texts.corrects))
       
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))

    await message.answer(texts.comment_5)
    with open('images/5.jpg', 'rb') as photo:
        await message.answer_photo(photo)
    await message.answer(texts.next_round, reply_markup=kb.round2)
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
       
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))

    await message.answer(texts.comment_6)
    with open('images/6.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kb.next_que)
    await State.que_7_.set()
    
@dp.message_handler(state=State.que_7_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_7, reply_markup=kb.variants)
    await State.que_7.set()
    

@dp.message_handler(state=State.que_7)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '4':
        await message.answer(random.choice(texts.corrects))
      
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))
    await message.answer(texts.comment_7, disable_web_page_preview=True)
    with open('images/7.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kb.next_que)
    await State.que_8_.set()
    

@dp.message_handler(state=State.que_8_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_8, reply_markup=kb.variants)
    await State.que_8.set()


@dp.message_handler(state=State.que_8)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '3':
        await message.answer(random.choice(texts.corrects))
      
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))
    await message.answer(texts.comment_8)
    with open('images/8.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kb.next_que)
    await State.que_9_.set()
    


@dp.message_handler(state=State.que_9_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_9, reply_markup=kb.variants)
    await State.que_9.set()

@dp.message_handler(state=State.que_9)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '1':
        await message.answer(random.choice(texts.corrects))
       
        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))
    await message.answer(texts.comment_9)
    with open('images/9.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kb.next_que)
    await State.que_10_.set()
    

@dp.message_handler(state=State.que_10_)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.question_10, reply_markup=kb.variants)
    await State.que_10.set()
    

@dp.message_handler(state=State.que_10)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '4':
        await message.answer(random.choice(texts.corrects))

        data = await state.get_data()
        sum = int(data.get('sum'))
        await state.update_data(sum=str(sum + 1)) 
    else:
        await message.answer(random.choice(texts.wrongs))

    await message.answer(texts.comment_10,  disable_web_page_preview=True)
    with open('images/10.jpg', 'rb') as photo:
        await message.answer_photo(photo)
    await message.answer(texts.end, reply_markup=kb.result)
    await State.tap_result.set()
    

@dp.message_handler(state=State.tap_result)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    sum = int(data.get('sum'))
    points = sum
    await message.answer(texts.generate_result(points), reply_markup=kb.sub)
    await State.tap_sub.set()
    await aiotable.update_cell(message.from_user.id, 7, points)
    

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
    await message.answer(texts.bye,  disable_web_page_preview=True)
    await State.ended.set()
    await aiotable.update_cell(message.from_user.id, 8, message.text)
        
        
   