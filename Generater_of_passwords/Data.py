import sqlite3

class DataBase:
	def __init__(self,database_file):
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()
	def show_service(self, service):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `passwds` WHERE `service` = ?', (service,)).fetchall()
			return result
	def service_exists(self, service):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `passwds` WHERE `service` = ?', (service,)).fetchall()
			return bool(len(result))
	def show_key(self, service):
		with self.connection:
			result = self.cursor.execute('SELECT `keys` FROM `passwds` WHERE `service` = ?', (service,)).fetchone()
			return result
	def change_key(self,service,key):
		with self.connection:
			return self.cursor.execute("UPDATE `passwds` SET `keys` = ? WHERE `service`= ?", (key,service,))	
	def insert_key(self,service,key):
		with self.connection:
			return self.cursor.execute("INSERT INTO `passwds` (`keys`, `service`) VALUES(?,?)", (key,service,))	
	def delete_service(self,service):
		with self.connection:
			return self.cursor.execute('''DELETE FROM `passwds` WHERE `service`= ?''', (service,))