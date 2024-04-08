from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import os

class MyApp(App):
# Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.label = Label(text='')
        self.input_data = TextInput(hint_text='Bведите название файла')
        self.input_data2 = TextInput(hint_text='Введите текст файла')
        self.button = Button(text='Open file')
        self.button2 = Button(text='Create file')
        self.button3 = Button(text='Write to file')
        self.button.bind(on_press=self.open)
        self.button2.bind(on_press=self.create)
        self.button3.bind(on_press=self.write)
    def build(self):
    # Все объекты будем помещать в один общий слой
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.input_data2)
        box.add_widget(self.button)
        box.add_widget(self.button2)
        box.add_widget(self.button3)
        return box

    def open(self, *args):
        name = self.input_data.text #считываем название файла
        try: #пробуем открыть файл
            f = open(name, 'r')
            t = f.read()# открываем файл для чтения
            if t != "":
                self.label.text = str(t)
            else:
                self.label.text = str("Empty")
            f.close()
        except:
            self.label.text = str("no such file")

    def create(self, *args):
        name = self.input_data.text
        try:
            if os.path.exists(name):
                self.label.text = f'File {name} already exists'
            else:
                f=open(name, 'w')
                self.label.text = f'File {name} was created'
                f.close()
        except Exception as e:
            print(e)

    def write(self, *args):
        name = self.input_data.text
        text = self.input_data2.text
        try:
            if os.path.exists(name):
                f = open(name, 'a')
                f.write(text)
                self.label.text=f"Text '{text}' was writed to file {name}"
                f.close()
            else:
                self.label.text=f"File {name} not exists"
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    MyApp().run()