TOKEN = '5505410546:AAHxnzeBdA3BT4UrCKaSYHxGyvfg7vS9EIg'

import asyncio
import logging
from datetime import *
import random


#aiogram и всё утилиты для коректной работы с Telegram API
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from list_of_admins import list_of_admins as lsa

#конфиг с настройками
#кастомные ответы
import custom_answer as cus_ans
from Data import DataBase
import sender_ban_static as bs


#задаём логи
logging.basicConfig(level=logging.INFO)


#инициализируем бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

#инициализируем базу данных
db = DataBase('database.db')

def create_public_id():
	public_id=''
	for i in range(10):
		public_id+=str(random.randint(0, 9))
	return public_id


# def aim_stat():
# 	button_aim = f'До добавления стикеров осталось {100 - db.count_user()[0]} пользователей'
# 	return button_aim

#хендлер команды /start
@dp.message_handler(commands=['start'],state='*')
async def start(message : types.Message):

	#кнопки для волшебного входа
	button_start = KeyboardButton('Зайти в мир знакомств')

	first_page = ReplyKeyboardMarkup(one_time_keyboard=True)

	first_page.add(button_start)
	if(not db.user_exists(message.from_user.id)):
    #если юзера нет в базе добавляем его
		public_id=create_public_id()
		db.add_user(message.from_user.username,message.from_user.id,message.from_user.full_name,public_id)
		await message.answer('Привет! Это место, где ты можешь познакомиться с ребятами из любой школы и развивать ваше школьное сообщество онлайн)',reply_markup=first_page)
		
    # await bot.send_message(-1001406772763,f'Новый пользователь!\nID - {str(message.from_user.id)}\nusername - {str(message.from_user.username)}')
	else:
		await message.answer('Привет! Давно не виделись',reply_markup=first_page)


@dp.message_handler(lambda message: message.text == 'Зайти в мир знакомств' or message.text == '/main_start',state='*')
async def main_start(message : types.Message):
	'''Функция для меню самого бота'''
	# await send_log(message)
	#кнопки меню
	button_join_chat = KeyboardButton('Вступить в чат школы')
	button_create_profile = KeyboardButton('Создать анкету📌')
	button_edit_profile = KeyboardButton('Редактировать анкету📝')
	button_send_request = KeyboardButton('Отправить запрос на просмотр анкет😏')
	button_check_notes = KeyboardButton('Посмотреть ваши запросы')
	button_remove_profile = KeyboardButton('Удалить🗑')
	button_admin = KeyboardButton('Админка⚙️')
	menu = ReplyKeyboardMarkup(row_width=2)

	if(not db.profile_exists(message.from_user.id)):
			menu.add(button_join_chat,button_create_profile)
	elif(db.profile_exists(message.from_user.id)) :
		menu.add(button_join_chat,button_edit_profile,button_remove_profile, button_admin, button_send_request, button_check_notes)

	await message.answer('Если что, то внизу есть кнопочки😉',reply_markup=menu)

class CreateProfile(StatesGroup):
	name = State()
	description = State()
	city = State()
	photo = State()
	sex = State()
	age = State()
	social_link	 = State()
	school=State()
	
@dp.message_handler(lambda message: message.text == 'Создать анкету📌',state='*')
async def create_profile(message : types.Message):
	button_exit = KeyboardButton('Выйти❌')
	menu_exit = ReplyKeyboardMarkup()
	menu_exit.add(button_exit)
	if message.from_user.username != None:
		if(not db.profile_exists(message.from_user.id)):
			await message.answer("Давайте начнём с твоего имени, как мне тебя называть?",reply_markup=menu_exit)
			await CreateProfile.name.set()
		elif(db.profile_exists(message.from_user.id)) :
			await message.answer('У тебя уже есть активная анкета\n\n')
	else:
		await message.answer('‼️У вас не заполнен username в телеграм!\n\nПожалуйста сделайте это для коректного функционирования бота\nДля этого зайдите в настройки -> Edit Profile(Изменить профиль) и жмякайте add username\n\nТам вводите желаемый никнейм и вуаля')

@dp.message_handler(state=CreateProfile.name)
async def create_profile_name(message: types.Message, state: FSMContext):
	if str(message.text) == 'Выйти❌':
		await state.finish()
		await main_start(message)
		return
	if len(str(message.text)) < 35 and (not str(message.text) in cus_ans.ban_symvols):
		await state.update_data(profile_name=message.text)
		button_skip = KeyboardButton('Пропустить')
		skip_input = ReplyKeyboardMarkup(one_time_keyboard=True)
		skip_input.add(button_skip)
		await message.answer('Теперь ты можешь написать о себе пару слов(это необязательно, но лучше заполнить это поле)', reply_markup=skip_input)
		await CreateProfile.next()
	elif str(message.text) in cus_ans.ban_symvols:
		await message.answer('У тебя в сообщении запрещённые символы🤬🤬\nЗапятая к примеру')
	else:
		await message.answer(cus_ans.random_reapeat_list())
		return

@dp.message_handler(state=CreateProfile.description)
async def create_profile_description(message: types.Message, state: FSMContext):
	if str(message.text) == 'Выйти❌':
		await state.finish()
		await main_start(message)
		return
	if str(message.text) == 'Пропустить':
		await message.answer('Теперь предлагаю заполнить город', reply_markup=ReplyKeyboardRemove())
		await state.update_data(profile_description='Отсутствует')
		await CreateProfile.next()
		return
	if len(message.text)<100 and (not str(message.text) in cus_ans.ban_symvols):
		await state.update_data(profile_description=message.text)
		await message.answer('Теперь предлагаю заполнить город', reply_markup=ReplyKeyboardRemove())
		await CreateProfile.next()
	elif str(message.text) in cus_ans.ban_symvols:
		await message.answer('У тебя в сообщении запрещённые символы🤬🤬\nЗапятая к примеру', reply_markup=ReplyKeyboardRemove())
	else:
		await message.answer(cus_ans.random_reapeat_list())
		return

@dp.message_handler(state=CreateProfile.city)
async def create_profile_city(message: types.Message, state: FSMContext):
	if str(message.text) == 'Выйти❌':
		await state.finish()
		await main_start(message)
		return
	if len(message.text) < 35 and (not str(message.text) in cus_ans.ban_symvols):
		await state.update_data(profile_city=message.text.lower())
		await message.answer('Прелестно, теперь добавим твою фотокарточку\n\nВажно отправлять фотографией, а не файлом!')
		await CreateProfile.next()
	elif str(message.text) in cus_ans.ban_symvols:
		await message.answer('У тебя в сообщении запрещённые символы🤬🤬\nЗапятая к примеру')
	else:
		await message.answer(cus_ans.random_reapeat_list())
		return
	
@dp.message_handler(state=CreateProfile.photo,content_types=['photo'])
async def create_profile_photo(message: types.Message, state: FSMContext):
	if str(message.text) == 'Выйти❌':
		await state.finish()
		await main_start(message)

	button_male = KeyboardButton('Мужской')

	button_wooman = KeyboardButton('Женский')

	sex_input = ReplyKeyboardMarkup(one_time_keyboard=True)
	sex_input.add(button_male,button_wooman)

	await message.photo[-1].download('photo_user/' + str(message.from_user.id) + '.jpg')
	await message.answer('Осталось совсем немного,укажи свой пол',reply_markup=sex_input)
	await CreateProfile.next()
@dp.message_handler(state=CreateProfile.sex)
async def create_profile_sex(message: types.Message, state: FSMContext):
	if str(message.text) == 'Выйти❌':
		await state.finish()
		await main_start(message)
		return
	if message.text == 'Мужской' or message.text == 'Женский':
		await state.update_data(profile_sex=message.text.lower())
		await message.answer('Замечательно!\nОсталось совсем чуть-чуть\n\nДавай же узнаем твой возвраст ')
		await CreateProfile.next()
	else:
		await message.answer(cus_ans.random_reapeat_list())
		return

@dp.message_handler(state=CreateProfile.age)
async def create_profile_age(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Выйти❌':
			await state.finish()
			await main_start(message)
			return
		if int(message.text) < 6:
			await message.answer('ой🤭\nТы чёт маловат...')
			await message.answer(cus_ans.random_reapeat_list())

			return
		elif int(message.text) > 54:
			await message.answer('Ты слишком стар чтобы быть школьником👨‍')
			await message.answer(cus_ans.random_reapeat_list())

			return
		elif int(message.text) > 6 and int(message.text) < 54:
			await state.update_data(profile_age=message.text)
			button_skip = KeyboardButton('Пропустить')
			skip_input = ReplyKeyboardMarkup(one_time_keyboard=True)
			skip_input.add(button_skip)
			await message.answer('Наконец-то!!\nПоследний шаг - указать ссылку на свой ВК🤑\nЕсли нет желания - можно пропустить➡',reply_markup=skip_input)
			await CreateProfile.next()
		else:
			await message.answer('Укажи правильный возраст, только цифры')
			return
	except:
		await message.answer(cus_ans.random_reapeat_list())
		return

@dp.message_handler(state=CreateProfile.social_link)
async def create_profile_social_link(message: types.Message, state: FSMContext):
    try:
        if str(message.text) == 'Выйти❌':
            await state.finish()
            await main_start(message)
            return
        if str(message.text) == 'Пропустить':
            await state.update_data(profile_link="Отсутствует")
            await message.answer('Укажи номер школы, в чат которой ты хочешь вступить')
            await CreateProfile.next()
        elif str(message.text).startswith('https://vk.com/'):
            await state.update_data(profile_link=message.text)
            await message.answer('Укажи номер школы, в чат которой ты хочешь вступить')
            await CreateProfile.next()
        else :
            await message.answer('Ссылка корявая!!\n\nОна должна начинаться с https://vk.com/\n\nК примеру - https://vk.com/someone/')

            return
    except:
        await message.answer(cus_ans.random_reapeat_list())
        #прерывание функции
        return

	
@dp.message_handler(state=CreateProfile.school)
async def create_profile_school(message: types.Message, state: FSMContext):
    try:
        if str(message.text) == 'Выйти❌':
            await state.finish()
            await main_start(message)
            return
        if len(message.text)<=5:
            await state.update_data(profile_school=message.text)
            await message.answer('Анкета успешно создана!')
            user_data = await state.get_data()
            db.create_profile(message.from_user.id,message.from_user.username,str(user_data['profile_name']),str(user_data['profile_description']),str(user_data['profile_city']),str(user_data['profile_sex']),str(user_data['profile_age']),str(user_data['profile_link']), str(user_data['profile_school']), 'photo/' + str(message.from_user.id) + '.jpg') #self,telegram_id,telegram_username,name,description,city,photo,sex,age,social_link
            await state.finish()
            await main_start(message)
        else:
            await message.answer('Введи только номер школы')
            return
    except:
        await message.answer(cus_ans.random_reapeat_list())
        #прерывание функции
        return


		

@dp.message_handler(lambda message: str(message.text) == 'Удалить🗑')
async def delete_profile(message : types.Message):
	'''Функция для удаления анкеты'''
	# await send_log(message)
	try:
		db.delete_profile(message.from_user.id) 
		await message.answer('Анкета успешно удалена!')
		await main_start(message)
	except:
		await message.answer(cus_ans.random_reapeat_list())
		return


@dp.message_handler(lambda message: message.text == 'Редактировать анкету📝')
async def edit_profile(message : types.Message):
    if(not db.profile_exists(message.from_user.id)):
        await message.answer('У тебя нет анкеты!')
    elif(db.profile_exists(message.from_user.id)) :
        photo = open('photo_user/' + str(message.from_user.id) + '.jpg','rb')
        #кнопки выбора пола
        button_school = KeyboardButton('Изменить номер школы')

        button_again = KeyboardButton('Заполнить анкету заново')

        button_edit_description = KeyboardButton('Изменить описание анкеты')

        button_edit_age = KeyboardButton('Изменить количество годиков')

        button_cancel = KeyboardButton('Выйти❌')

        edit_profile = ReplyKeyboardMarkup(one_time_keyboard=True)
        edit_profile.add(button_again,button_edit_description,button_edit_age,button_cancel, button_school)
        caption = 'Твоя анкета:\n'
        inf=list(db.all_profile(message.from_user.id)[0][3:-2:])
        for i in range(len(inf)):
            if str(inf[i])!='Отсутствует':
                caption+=cus_ans.profile_naming[i]+inf[i]
        await message.answer_photo(photo,caption=caption,reply_markup=edit_profile)
        photo.close()




@dp.message_handler(lambda message: message.text == 'Заполнить анкету заново')
async def edit_profile_again(message : types.Message):
	'''Функция для заполнения анкеты заново'''
	# await send_log(message)
	try:
		db.delete_profile(message.from_user.id)
		await create_profile(message)

	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return


class EditProfile(StatesGroup):
	description_edit = State()
	age_edit = State()
	school_edit = State()


@dp.message_handler(lambda message: message.text == 'Изменить количество годиков' or message.text == 'Изменить описание анкеты' or message.text == 'Изменить номер школы')
async def edit_profile_age(message : types.Message):
	try:
		button_cancel = KeyboardButton('Отменить❌')

		button_cancel_menu = ReplyKeyboardMarkup(one_time_keyboard=True)

		button_cancel_menu.add(button_cancel)

		if message.text == 'Изменить количество годиков':
			await message.answer('Введи свой новый возвраст',reply_markup=button_cancel_menu)
			await EditProfile.age_edit.set()
		elif message.text == 'Изменить описание анкеты':
			await message.answer('Введи новое хайп описание своей анкеты!',reply_markup=button_cancel_menu)
			await EditProfile.description_edit.set()
		elif message.text == 'Изменить номер школы':
			await message.answer('Введи новый номер школы',reply_markup=button_cancel_menu)
			await EditProfile.school_edit.set()
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return
	
@dp.message_handler(state=EditProfile.age_edit)
async def edit_profile_age_step2(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Отменить❌':
			await state.finish()
			await main_start(message)

			return
		elif int(message.text) < 6:
			await message.answer('ой🤭\nТы чёт маловат...')
			await message.answer(cus_ans.random_reapeat_list())

			#прерывание функции
			return
		elif int(message.text) > 54:
			await message.answer('Пажилой человек👨‍')
			await message.answer(cus_ans.random_reapeat_list())

			#прерывание функции
			return
		elif int(message.text) > 6 and int(message.text) < 54:
			await message.answer('Малый повзрослел получается🤗\n\nВозвраст успешно измененён!')
			await state.update_data(edit_profile_age=message.text)
			user_data = await state.get_data()

			db.edit_age(user_data['edit_profile_age'],str(message.from_user.id))
			await state.finish()
			await edit_profile(message)
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return
	
@dp.message_handler(state=EditProfile.description_edit)
async def edit_profile_description(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Отменить❌':
			await state.finish()
			await main_start(message)

			return
		await message.answer('Описание успешно изменено!')
		await state.update_data(edit_profile_description=message.text)
		user_data = await state.get_data()

		db.edit_description(user_data['edit_profile_description'],str(message.from_user.id))
		await state.finish()
		await edit_profile(message)
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return
	
@dp.message_handler(state=EditProfile.school_edit)
async def edit_profile_school_step2(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Отменить❌':
			await state.finish()
			await main_start(message)
			return
		if len(message.text)<5:
			await state.update_data(edit_profile_school=message.text)
			user_data = await state.get_data()
			db.edit_school(user_data['edit_profile_school'],str(message.from_user.id))
			await state.finish()
			await edit_profile(message)
			
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return

@dp.message_handler(lambda message: message.text == 'Выйти❌')
async def exit(message : types.Message):
	await main_start(message)


@dp.message_handler(lambda message: message.text == 'Вступить в чат школы')
async def set_session(message: types.Message):

	try:
		if db.profile_exists(message.from_user.id):
			button_close_session=KeyboardButton('Выйти из чата')
			button_of_anonymus_off=KeyboardButton('Выключить анонимность')
			button_of_anonymus_on=KeyboardButton('Включить анонимность')
			session=ReplyKeyboardMarkup()
			session.add(button_close_session, button_of_anonymus_off, button_of_anonymus_on)
			db.set_session(message.from_user.id, "active")
			await bot.send_message(message.from_user.id, f"Приятного времяпрепровождения в чате школы {str(db.get_school(message.from_user.id)[0])}", reply_markup=session)
		else:
			await message.answer('Ты еще не создал анкету, бегом исправлять это')	
			return
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return

@dp.message_handler(lambda message: message.text == 'Выйти из чата')
async def quit_chat(message: types.Message):
    db.set_session(message.from_user.id, "sleep")
    await bot.send_message(message.from_user.id, "До новых встреч!)")
    await main_start(message)

@dp.message_handler(lambda message: message.text == 'Выключить анонимность')
async def quit_chat(message: types.Message):
	if db.get_stat_of_anonymus(message.from_user.id)[0]=='1':
		await message.answer("Режим анонимности выключен(теперь над вашим сообщением будет виден никнейм)")
		db.set_stat_of_anonymus(message.from_user.id, 'False')
	else:
		await message.answer("Режим анонимности уже выключен")

@dp.message_handler(lambda message: message.text == 'Включить анонимность')
async def quit_chat(message: types.Message):
	if db.get_stat_of_anonymus(message.from_user.id)[0]=='False':
		await message.answer("Режим анонимности включен(теперь над вашим сообщением не будет виден никнейм)")
		db.set_stat_of_anonymus(message.from_user.id, '1')
	else:
		await message.answer("Режим анонимности и так включен")

class Admin(StatesGroup):
	users_by_school = State()

@dp.message_handler(lambda message: message.text == 'Админка⚙️')
async def admin_panel(message: types.Message):
	if message.from_user.id in lsa:
		button_show_all_schools=KeyboardButton('Показать список школ')
		button_count_users_in_school = KeyboardButton('Показать количество юзеров в школе')
		button_count_all_users=KeyboardButton("Посчитать всех юзеров")
		send_ban_static = KeyboardButton("Отправить бан-статистику")
		button_cancel = KeyboardButton('Выйти❌')
		send_post=KeyboardButton("Отправить пост в школу или всем")
		admin_markup=ReplyKeyboardMarkup()
		admin_markup.add(button_show_all_schools, button_count_users_in_school, button_count_all_users, button_cancel, send_ban_static, send_post)
		await bot.send_message(message.from_user.id, 'Добро пожаловать админ! Вот твои инструменты', reply_markup=admin_markup)
	else:
		await message.answer("Увы, но вам  отказано в доступе(")
		return
	
class Send_post(StatesGroup):
	number_of_school=State()
	text_post = State()
	photo_post = State()

@dp.message_handler(lambda message: message.text == 'Отправить пост в школу или всем')
async def list_of_schools(message: types.Message):
	if message.from_user.id in lsa:
		# send_all = KeyboardButton("Отправить всем школам")
		send_to= KeyboardButton("Отправить в школу")
		button_cancel = KeyboardButton('Выйти❌')
		send_menu = ReplyKeyboardMarkup(one_time_keyboard=True)
		send_menu.add(send_to,button_cancel)
		await message.answer("Теперь выбери нужное", reply_markup=send_menu)
	else:
		await message.answer("Отказано в доступе")

@dp.message_handler(lambda message: message.text == 'Отправить всем школам')
async def list_of_schools(message: types.Message):
	if message.from_user.id in lsa:
		try:
			button_cancel = KeyboardButton('Отменить❌')
			button_cancel_menu = ReplyKeyboardMarkup(one_time_keyboard=True)
			button_cancel_menu.add(button_cancel)
			await message.answer('''Отправь текст поста''', reply_markup=button_cancel_menu)
			await Send_post.text_post.set()
		except:
			await message.answer("Не получилось задать форму")
	else:
		await message.answer("Отказано в доступе")

@dp.message_handler(lambda message: message.text == 'Отправить в школу')
async def send_to_school(message: types.Message):
	if message.from_user.id in lsa:
		try:
			button_cancel = KeyboardButton('Отменить❌')
			button_cancel_menu = ReplyKeyboardMarkup(one_time_keyboard=True)
			button_cancel_menu.add(button_cancel)
			await message.answer('''Отправь номер школы''', reply_markup=button_cancel_menu)
			await Send_post.number_of_school.set()
		except:
			await message.answer("Не получилось задать форму")
	else:
		message.answer("Отказано в доступе")

@dp.message_handler(state=Send_post.number_of_school)
async def set_school(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Отменить❌':
			await state.finish()
			await admin_panel(message)
			return
		elif len(message.text)<5:
			await state.update_data(number_of_school=message.text)
			await message.answer('Теперь введи текст')
			await Send_post.next()
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return
	
@dp.message_handler(state=Send_post.text_post)
async def set_text(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Отменить❌':
			await state.finish()
			await admin_panel(message)
			return
		elif len(message.text)<100:
			button_skip = KeyboardButton('Пропустить')
			skip_input = ReplyKeyboardMarkup(one_time_keyboard=True)
			skip_input.add(button_skip)
			await state.update_data(text_post=message.text)
			await message.answer('Теперь отправь фото', reply_markup=skip_input)
			await Send_post.next()
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return

@dp.message_handler(state=Send_post.photo_post, content_types=['photo', 'text'])
async def set_photo(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Пропустить':
			# user_data = await state.get_data()
			# if user_data['number_of_school']==None:
			# 	await state.update_data(number_of_school='all')
			user_data = await state.get_data()
			caption=''
			inf=[user_data['number_of_school'], user_data['text_post']]
			for i in range(len(inf)):
				caption+=inf[i]+'\n'
			await message.answer(caption)
			await state.finish()
			await admin_panel(message)
			return

		await message.photo[-1].download('photo_posts/' + str(message.from_user.id) + '.jpg')
		# user_data = await state.get_data()
		# if user_data['number_of_school']==None:
		# 	await state.update_data(number_of_school='all')
		user_data = await state.get_data()
		caption=''
		photo = open('photo_posts/' + str(message.from_user.id) + '.jpg','rb')
		inf=[user_data['number_of_school'], user_data['text_post']]
		for i in range(len(inf)):
			caption+=inf[i]+'\n'
		await message.answer_photo(photo,caption=caption)
		await state.finish()
		photo.close()
		await main_start(message)
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return
	

@dp.message_handler(lambda message: message.text == 'Отправить бан-статистику')
async def list_of_schools(message: types.Message):
	if message.from_user.id in lsa:
		try:
			file = 'ban_list.txt'
			bs.creating_ban_list(file, db)
			print(bs.send_email(file=file))
			db.delete_ban_list()
			await message.answer("Бан-лист был отправлен на вашу почту")
			await admin_panel(message)
		except:
			await message.answer("Не удалось отправить бан-лист")
			await admin_panel(message)
	else:
		message.answer("Отказано в доступе")

@dp.message_handler(lambda message: message.text == 'Показать список школ')
async def list_of_schools(message: types.Message):
	if message.from_user.id in lsa:	
		list_of_schools=''
		for school in db.get_schools():
			list_of_schools+=str(school[0])+' '
		await message.answer(list_of_schools)
	else:
		message.answer("Отказано в доступе")
	
@dp.message_handler(lambda message: message.text == 'Посчитать всех юзеров')
async def count_all_users(message: types.Message):
	if message.from_user.id in lsa:	
		await message.answer(db.get_count_users()[0][0])
	else:
		message.answer("Отказано в доступе")
	
@dp.message_handler(lambda message: message.text == 'Показать количество юзеров в школе')
async def request_to_school(message: types.Message):
	if message.from_user.id in lsa:	
		button_cancel = KeyboardButton('Отменить❌')

		button_cancel_menu = ReplyKeyboardMarkup(one_time_keyboard=True)

		button_cancel_menu.add(button_cancel)
		await message.answer("Отправьте номер интересующей школы", reply_markup=button_cancel_menu)
		await Admin.users_by_school.set()
	else:
		message.answer("Отказано в доступе")	

@dp.message_handler(state=Admin.users_by_school)
async def request_to_school(message: types.Message, state=FSMContext):
    try:
        if str(message.text) == 'Отменить❌':
            await state.finish()
            await admin_panel(message)
            return
        elif len(message.text)<5:
            school=db.get_user_by_school(message.text)
            await state.update_data(users_by_school=school)
            user_data = await state.get_data()
            await state.finish()
            await bot.send_message(message.from_user.id, user_data['users_by_school'][0][0])
            await admin_panel(message)

    except Exception as e:
        await message.answer(cus_ans.random_reapeat_list())
        print(e)
        return

class Send_request(StatesGroup):
	public_id2 = State()
	description = State()

@dp.message_handler(lambda message: message.text == 'Отправить запрос на просмотр анкет😏')
async def request(message: types.Message):
	try:
		button_cancel = KeyboardButton('Выйти❌')
		button_cancel_menu = ReplyKeyboardMarkup()
		button_cancel_menu.add(button_cancel)
		await message.answer('''Отправь id того, кому хочешь отправить запрос\n
					   Подсказка: id - это то, что ты видишь перед сообщением (если человек отлючил анонимность)''', reply_markup=button_cancel_menu)
		await Send_request.public_id2.set()
	except:
		await message.answer("Не получилось задать форму")

@dp.message_handler(state=Send_request.public_id2)
async def set_username2(message: types.Message, state=FSMContext):
	try:
		if db.pb_id_exists(message.text):
			button_skip = KeyboardButton('Пропустить')
			skip_input = ReplyKeyboardMarkup(one_time_keyboard=True)
			skip_input.add(button_skip)
			await bot.send_message(message.from_user.id, "Теперь можешь написать что-то получателю, а можешь пропустить (до 50 символов)", reply_markup=skip_input)
			await state.update_data(public_id2=str(message.text))
			await Send_request.next()
		else:
			await message.answer("Такого человечка у нас не числится😢")
			return
	except:
		await message.answer("Что-то пошло не так")
		return
	
@dp.message_handler(state=Send_request.description)
async def set_description(message: types.Message, state=FSMContext):
	public_id = db.get_pb_id(message.from_user.id)[0]
	try:
		if str(message.text) == 'Пропустить':
			await state.update_data(description="Отсутствует")
			user_data = await state.get_data()
			db.set_requset(str(public_id), str(user_data["public_id2"]), str(user_data["description"]))
			await bot.send_message(message.from_user.id, "У вас новый запрос!")
			await state.finish()
			await main_start(message)
		elif 0<len(str(message.text))<=50 and (not str(message.text) in cus_ans.ban_symvols):
			await state.update_data(description=str(message.text))
			user_data = await state.get_data()
			db.set_requset(str(public_id), str(user_data["public_id2"]), str(user_data["description"]))
			await bot.send_message(message.from_user.id, "У вас новый запрос!")
			await state.finish()
			await main_start(message)
		elif str(message.text) in cus_ans.ban_symvols:
			await message.answer('У тебя в сообщении запрещённые символы🤬🤬\nЗапятая к примеру', reply_markup=ReplyKeyboardRemove())
		else:
			await message.answer(cus_ans.random_reapeat_list())
			#прерывание функции
			return
	except:
		await message.answer('??????')
		return
	
@dp.message_handler(lambda message: message.text == 'Посмотреть ваши запросы')
async def check_notices(message: types.Message):
	public_id = db.get_pb_id(message.from_user.id)[0]
	try:
		if db.check_bool_notices(public_id):
			await message.answer('Юхууу, мы нашли запросик (или больше)\nЧтобы одобрить запрос напииши "Одобрить и никнейм"')
			markup_accept = ReplyKeyboardMarkup(one_time_keyboard=True)
			for notice in db.check_notices(public_id):
				button = KeyboardButton(f'Одобрить {str(notice[1])}')
				markup_accept.add(button)
				await bot.send_message(message.from_user.id, f'Запросик:\nОтправитель - {str(notice[1])}\nОписание - {str(notice[3])}')
			await bot.send_message(message.from_user.id, "Теперь можешь выбрать кого одобрить", reply_markup=markup_accept)
		else:
			await message.answer('Эххх, но пока что вам не прислали запросы(')
			await main_start(message)
	except:
		await bot.send_message(message.from_user.id, cus_ans.random_reapeat_list())

@dp.message_handler(lambda message: "одобрить" in str(message.text).lower())
async def check_notices(message: types.Message):
	public_id2=str(message.text).lower().split()[1]
	user_id2=db.get_tgid_pb_id(public_id2)[0]
	if db.user_exists(user_id2):

		photo1 = open('photo_user/' + str(message.from_user.id) + '.jpg','rb')
		photo2 = open('photo_user/' + str(user_id2) + '.jpg','rb')
		caption1 = 'Анкета одобряющего:\n'
		caption2 = 'Анкета отправителя:\n'
		inf1=list(db.all_profile(message.from_user.id)[0][3:-2:])
		inf2=list(db.all_profile(user_id2)[0][3:-2:])
		for i in range(len(inf2)):
			if str(inf2[i])!='Отсутствует':
				caption2+=cus_ans.profile_naming[i]+inf2[i]
		for i in range(len(inf1)):
			if str(inf1[i])!='Отсутствует':
				caption1+=cus_ans.profile_naming[i]+inf1[i]	
		await bot.send_message(user_id2, "Ваш запрос одобрен, вот анкета анкета этого человека")	
		await bot.send_photo(user_id2, photo1, caption=caption1)	
		await message.answer_photo(photo2, caption=caption2)
		db.delete_notices(user_id2, message.from_user.id)
		photo1.close()
		photo2.close()
		await main_start(message)
	else:
		await message.answer('Такой человечек отсутствует')
		await main_start(message)

@dp.message_handler()
async def chatting(message: types.Message):
	public_id=db.get_pb_id(message.from_user.id)[0]
	if str(db.get_session(message.from_user.id)[0])=='active':
		list_active_users=[user_id for user_id in db.get_user_id_in_school(db.get_school(message.from_user.id)[0])]
		print(list_active_users)
		db.add_user_ban_list(message.text.lower(), message.from_user.id)
		for i in list_active_users:
			if str(i[0])!=str(message.from_user.id):
				if db.get_stat_of_anonymus(message.from_user.id)[0]=="1":
					if message['reply_to_message']:
						await bot.send_message(i[0], message.text, reply_to_message_id=message['reply_to_message']['message_id']-1)
					else:
						await bot.send_message(i[0], message.text)
				else:
					if message['reply_to_message']:
						
						await bot.send_message(i[0], f"***/{str(public_id)}/***\n{message.text}", reply_to_message_id=message['reply_to_message']['message_id']-1)
					else:
						await bot.send_message(i[0], f"***/{str(public_id)}/***\n{message.text}")
	else:
		await message.answer("Вы еще не вошли в чат, чтобы отправить сообщение")
		
if __name__=="__main__":
	executor.start_polling(dp, skip_updates=False)


