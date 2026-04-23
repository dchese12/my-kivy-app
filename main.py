from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.clock import mainthread
import time
import threading
import sqlite3  # Moved to top for Buildozer to see it clearly
import os

# Get path to writeable folder on Android
if 'PYTHON_SERVICE_ARGUMENT' in os.environ:
    db_path = os.path.join(os.getenv('PYTHON_SERVICE_ARGUMENT'), "TheDatabase.db")
else:
    db_path = "TheDatabase.db"

KV = ''' 
ScreenManager:
    FirstScreen: 
    SecondScreen: 

<FirstScreen>:
    name : 'firstscreen'
    BoxLayout:
        orientation : 'vertical'
        Label :
            id : second
            text : "Welcome!!"
            size_hint: 1,0.2
        TextInput:
            id : input 
            hint_text : "Enter table name or data..."
            multiline : False
            font_size : '24sp'
            halign : 'center'
            size_hint: 1,0.2   
        Button :
            text : "Create Table"
            size_hint: 1,0.2
            on_press: app.action_a()
        Button:
            text: "Insert Data (id,name,qty)"
            size_hint: 1,0.2
            on_press: app.action_b()
        Button:
            text : "Automatic Next Page"
            size_hint: 1,0.1
            on_press : app.action_c()

<SecondScreen>:
    name : 'secondscreen'
    BoxLayout:
        orientation: 'vertical'
        Label :
            text : "This is the SecondScreen"
            id : secon_text
        TextInput:
            hint_text: "Type column name (id, name, quantity)"
            halign: 'center'
            multiline: False
            id : fetch
        Button:
            text: "Fetch Data"
            size_hint: 1,0.2
            on_press : app.fetch_data()
        Button:
            text: "Close"
            size_hint : 1,0.1
            on_press : app.close()
'''

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class python_sql:
    def __init__(self, db_name):
        self.db_name = db_name
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

class My_App(App):
    def build(self):
        return Builder.load_string(KV)
    
    @mainthread
    def switch_screen(self, screen_name):
        self.root.current = screen_name

    @mainthread 
    def update_text(self, message):
        self.root.get_screen('firstscreen').ids.second.text = message

    @mainthread
    def update_text2(self, message):
        self.root.get_screen('secondscreen').ids.secon_text.text = message

    def action_a(self):
        threading.Thread(target=self.bk_work).start()

    def bk_work(self):
        self.update_text("Creating Table...")
        table_name = self.root.get_screen('firstscreen').ids.input.text
        if not table_name: table_name = "DefaultTable"
        with python_sql(db_path) as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}(id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)")
        time.sleep(1)
        self.switch_screen('secondscreen')

    def action_b(self):
        threading.Thread(target=self.bk_work2).start()

    def bk_work2(self):
        self.update_text("Inserting...")
        val = self.root.get_screen('firstscreen').ids.input.text
        try:
            v = val.split(",")
            with python_sql(db_path) as cursor:
                cursor.execute("INSERT INTO History(id, name, quantity) VALUES (?, ?, ?)", (v[0], v[1], v[2]))
            self.switch_screen('secondscreen')
        except:
            self.update_text("Error: Use format 1,name,10")

    def action_c(self):
        threading.Thread(target=self.bk_work3).start()

    def bk_work3(self):
        self.update_text("Switching...")
        time.sleep(2)
        self.switch_screen('secondscreen')

    def fetch_data(self):
        threading.Thread(target=self.fetching).start()

    def fetching(self):
        col = self.root.get_screen('secondscreen').ids.fetch.text
        try:
            with python_sql(db_path) as cursor:
                cursor.execute(f"SELECT {col} FROM History")
                res = cursor.fetchone()
                if res:
                    self.update_text2(f"Result: {res[0]}")
        except:
            self.update_text2("Fetch Error")

    def close(self):
        self.stop()

if __name__ == '__main__':
    My_App().run()
