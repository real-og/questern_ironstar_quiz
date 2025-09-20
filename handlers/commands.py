from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import aiotable
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
import asyncio
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
        

@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer("Если Вам нужна помощь, пишите @lenkkey")
    

@dp.message_handler(commands=['check'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    print('here')
    all = await aiotable.get_all()
    for i, user in enumerate(all[1:]):
        print(i, user[1])
        num = i + 2
        user_status = await bot.get_chat_member(-1001016200452, user[1])

        if user_status['status'] == 'left':
            await aiotable.update_cell_strict(num, 9, 'no')
            print('no')
        else:
            await aiotable.update_cell_strict(num, 9, 'yes')
            print('yes')
            
    await aiotable.update_cell_strict(1, 9, 'no')
    

@dp.message_handler(commands=['broadcast'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    print(message.text)
    nums = message.text.split()
    n1 = nums[1]
    n2 = nums[2]
    n3 = nums[3]
    all = await aiotable.get_all()
    user_ids = []
    for user in all[1:]:
        user_ids.append(user[1])
    user_ids = list(set(user_ids))
    text = f"""Внимание, финиш! 🏁
Розыгрыш состоялся, и у нас есть три чемпиона, которые получают фирменный мерч от IRONSTAR:
⚡️ Участник {n1} - толстовку для тёплых стартов!
⚡️ Участник {n2}  - футболку для жарких тренировок!
⚡️ Участник {n3} - кепку для стильного забега!

Всем остальным — спасибо за участие! Следи за новыми стартами на сайте 👉 <a href="iron-star.com">IRONSTAR</a>
До следующих рекордов! 💪🔥"""
    for user_id in user_ids:
        try:
            await bot.send_message(user_id, text, disable_web_page_preview=True)
            print(f"✅ Сообщение отправлено {user_id}")
            await asyncio.sleep(1)  # минимальная задержка, чтобы избежать спама
        except BotBlocked:
            print(f"⛔ Бот заблокирован пользователем {user_id}")
        except ChatNotFound:
            print(f"❌ Чат не найден для {user_id}")
        except Exception as e:
            print(f"⚠️ Ошибка при отправке {user_id}: {e}")
