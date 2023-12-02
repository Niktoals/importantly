import sqlite3

class DataBase:
	def __init__(self,database_file):
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()
	def user_exists(self, user_id):
		'''Проверка есть ли юзер в бд'''
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `users` WHERE `telegram_id` = ?', (user_id,)).fetchall()
			return bool(len(result))
	def user_exists_by_username(self, username):
		'''Проверка есть ли юзер в бд'''
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `users` WHERE `telegram_username` = ?', (username,)).fetchall()
			return bool(len(result))
	def add_user(self,telegram_username,telegram_id,full_name, public_id):
		'''Добавляем нового юзера'''
		with self.connection:
			return self.cursor.execute("INSERT INTO `users` (`telegram_username`, `telegram_id`,`full_name`, `public_id`) VALUES(?,?,?,?)", (telegram_username,telegram_id,full_name,public_id,))
	def create_profile(self,telegram_id,telegram_username,name,description,city,sex,age,social_link,school,photo):
		'''Создаём анкету'''
		with self.connection:
			return self.cursor.execute("INSERT INTO `profile_list` (`telegram_id`,`telegram_username`,`name`,`description`,`city`,`sex`,`age`,`school`,`social_link`,`photo`) VALUES(?,?,?,?,?,?,?,?,?,?)", (telegram_id,telegram_username,name,description,city,sex,age,school,social_link,photo))
	def profile_exists(self,user_id):
		'''Проверка есть ли анкета в бд'''
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `profile_list` WHERE `telegram_id` = ?', (user_id,)).fetchall()
			return bool(len(result))
	def delete_profile(self,user_id):
		'''Удаление анкеты'''
		with self.connection:
			return self.cursor.execute("DELETE FROM `profile_list` WHERE `telegram_id` = ?",(user_id,))
	def all_profile(self,user_id):
		'''поиск по анкетам'''
		with self.connection:
			return self.cursor.execute("SELECT * FROM `profile_list` WHERE `telegram_id` = ?",(user_id,)).fetchall()
	def edit_description(self,description,user_id):
		'''изменение описания'''
		with self.connection:
			return self.cursor.execute('UPDATE `profile_list` SET `description` = ? WHERE `telegram_id` = ?',(description,user_id))
	def edit_age(self,age,user_id):
		'''изменение возвраста'''
		with self.connection:
			return self.cursor.execute('UPDATE `profile_list` SET `age` = ? WHERE `telegram_id` = ?',(age,user_id))
	def edit_school(self,school,user_id):
		'''изменение возвраста'''
		with self.connection:
			return self.cursor.execute('UPDATE `profile_list` SET `school` = ? WHERE `telegram_id` = ?',(school,user_id))
	def get_info(self,user_id):
		'''получение ифнормации по профилю'''
		with self.connection:
			return self.cursor.execute("SELECT * FROM `profile_list` WHERE `telegram_id` = ?",(user_id,)).fetchone()
	def get_school(self,user_id):
		with self.connection:
			return self.cursor.execute("SELECT `school` FROM `profile_list` WHERE `telegram_id` = ?",(user_id,)).fetchone()
	def get_info_user(self,user_id):
		'''получение информации по юзеру'''
		with self.connection:
			return self.cursor.execute("SELECT * FROM `users` WHERE `telegram_id` = ?",(user_id,)).fetchone()
	def get_user_id_in_school(self,school):
		with self.connection:
			return self.cursor.execute("SELECT `telegram_id` FROM `profile_list` WHERE `school`=? and `session`='active'",(school,)).fetchall()
	def set_session(self, user_id, session):
		with self.connection:
			return self.cursor.execute("UPDATE `profile_list` SET `session` = ? WHERE `telegram_id` = ?",(session, user_id,))
	def get_session(self, user_id):
		with self.connection:
			return self.cursor.execute("SELECT `session` FROM `profile_list` WHERE `telegram_id` = ?",(user_id,)).fetchone()
	def get_schools(self):
		with self.connection:
			return self.cursor.execute("SELECT DISTINCT `school` FROM `profile_list`").fetchall()
	def get_user_by_school(self, school):
		with self.connection:
			return self.cursor.execute("SELECT COUNT(`telegram_id`) FROM `profile_list` WHERE `school` = ?", (school,)).fetchall()
	def get_count_users(self):
		with self.connection:
			return self.cursor.execute("SELECT COUNT(`telegram_id`) FROM `profile_list`").fetchall()
	def get_stat_of_anonymus(self, user_id):
		with self.connection:
			return self.cursor.execute("SELECT `anonymus` FROM `users` WHERE`telegram_id` = ?",(user_id,)).fetchone()	
	def set_stat_of_anonymus(self, user_id, anon):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `anonymus`=? WHERE `telegram_id` = ?",(anon, user_id,))	
	def get_telegram_username(self, user_id):
		with self.connection:
			return self.cursor.execute("SELECT `telegram_username` FROM `users` WHERE `telegram_id` = ?",(user_id,)).fetchone()	
	def set_requset(self, public_id1, public_id2, description):
		with self.connection:
			return self.cursor.execute("INSERT INTO `requests` (`public_id1`, `public_id2`,`description`) VALUES(?,?,?)",(public_id1, public_id2, description,))
	def get_telegramid_byusername(self, username):
		with self.connection:
			return self.cursor.execute("SELECT `telegram_id` FROM `users` WHERE `telegram_username` = ?",(username,)).fetchone()		
	def check_notices(self, public_id2):
		with self.connection:
			return self.cursor.execute('''SELECT * FROM `requests` WHERE `public_id2` = ?''', (public_id2,)).fetchall()
	def check_bool_notices(self, public_id2):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `requests` WHERE `public_id2` = ?''', (public_id2,)).fetchall()
			return bool(len(result))
	def delete_notices(self, public_id1, public_id2):
		with self.connection:
			return self.cursor.execute('''DELETE FROM `requests` WHERE `public_id1` = ? and `public_id2` = ?''', (public_id1, public_id2,))
	def get_pb_id(self, user_id):
		with self.connection:
			return self.cursor.execute('''SELECT `public_id` FROM `users` WHERE `telegram_id` = ?''', (user_id,)).fetchone()
	def pb_id_exists(self, public_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `users` WHERE `public_id` = ?', (public_id,)).fetchall()
			return bool(len(result))
	def get_tgid_pb_id(self, public_id):
		with self.connection:
			return self.cursor.execute('''SELECT `telegram_id` FROM `users` WHERE `public_id` = ?''', (public_id,)).fetchone()
	def add_user_ban_list(self,message_text,telegram_id):
		'''Добавляем нового юзера'''
		with self.connection:
			return self.cursor.execute("INSERT INTO `ban_list` (`message`, `telegram_id`) VALUES(?,?)", (message_text,telegram_id,))	
	def search_ban_message(self, message):
		with self.connection:
			return self.cursor.execute("SELECT * FROM `ban_list` WHERE `message` LIKE ?", (message,)).fetchall()
	def search_message(self):
		with self.connection:
			return self.cursor.execute("SELECT `message`, `telegram_id` FROM `ban_list`").fetchall()
	def delete_ban_list(self):
		with self.connection:
			return self.cursor.execute('''DELETE FROM `ban_list`''')