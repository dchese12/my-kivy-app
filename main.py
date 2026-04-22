from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
import time
import threading
from kivy.clock import mainthread
import sys

db_name = "TheDatabase.db"


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
            hint_text : "Enter......"
            multiline : False
            font_size : '24sp'
            foreground_color: 1,0,0,1
            halign : 'center'
            size_hint: 1,0.2   
            
        Button :
            text : "Create"
            background_color: 0,1,0,0
            size_hint: 1,0.2
            on_press: app.action_a()
        
                
        Button:
            text: "Insert"
            background_color: 1,0,0,1
            size_hint: 1,0.2
            on_press: app.action_b()
        
        Button:
            text : "Automatic Next Page"
            background_color: 0,1,0,1
            size_hint: 1,0.1
            on_press : app.action_c()

<SecondScreen>:
    name : 'secondscreen'
    BoxLayout:
        orientation: 'vertical'
        
        Label :
            text : "This is the SecondScreen"
            color : 0.2,0.6,0.9,1
            id : secon_text
       
        TextInput:
            hint_text: "Type name, id, or quantity"
            foreground_color: 1, 0, 1, 1
            halign: 'center'
            multiline: False
            id : fetch
            
        Button:
            text: "Fetch Data"
            size_hint: 1,0.2
            background_color: 0,1,0,0
            on_press : app.fetch_data()
        
        Button:
            text: "Close"
            background_color: 1,1,1,1
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
        import sqlite3
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

class My_App(App):
    def build(self):
        return Builder.load_string(KV)
        
    
    def action_a(self):
        work = threading.Thread(target = self.bk_work)
        work.start()
    @mainthread
    def switch_screen(self, message):
        self.root.current = message
    @mainthread 
    def update_text(self, message):
        first_screen = self.root.get_screen('firstscreen')
        first_screen.ids.second.text = message
    
    def update_text2(self, message):
        second_screen = self.root.get_screen('secondscreen')
        second_screen.ids.secon_text.text = message
    
    def action_b(self):
        work1 = threading.Thread(target = self.bk_work2)
        work1.start()
    def bk_work(self):
        self.update_text("Creating Database now............")
        first_screen = self.root.get_screen('firstscreen')
        Value = first_screen.ids.input.text
        with python_sql(db_name) as cursor:
            cursor.execute(f''' CREATE TABLE IF NOT EXISTS {Value}(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, quantity INTEGER)''')
            time.sleep(2)
            self.switch_screen('secondscreen')
         
    def action_c(self):
        work2=threading.Thread(target = self.bk_work3)
        work2.start()
    
    def bk_work3(self):
        self.update_text("Switching Screens........")
        time.sleep(3)
        self.switch_screen('secondscreen')
        
        
    def bk_work2(self):
        self.update_text("Inserting........")
        first_screen = self.root.get_screen('firstscreen')
        Value = first_screen.ids.input.text
        Values1 = Value.split(",")
        id_num = Values1[0]
        name_num = Values1[1]
        qty_num = Values1[2]
        with python_sql(db_name)as cursor:
            cursor.execute(f"INSERT INTO History(id, name, quantity) Values (?, ?, ?)", (id_num, name_num, qty_num))
            time.sleep(3)
            self.switch_screen('secondscreen')
    
    def data_gen(self, db_name):
        second_screen = self.root.get_screen('secondscreen')
        fetch_text = second_screen.ids.fetch.text 
        with python_sql(db_name) as cursor:
            cursor.execute(f''' SELECT {fetch_text} FROM History''')
            for items in cursor:
                yield items[0]
    
    def fetch_data(self):
        get = threading.Thread(target = self.fetching)
        get.start()
        
    def fetching(self):
        second_screen= self.root.get_screen('secondscreen')
        for item in self.data_gen(db_name):
            self.update_text2(f"Retrieving Data: {item}")
            time.sleep(2)
    
    def close(self):
        closed = threading.Thread(target = self.closing)
        closed.start()
    
    def closing(self):
        self.update_text2('Closing Program........')
        time.sleep(3)
        from kivy.app import App
        App.get_running_app().stop()
        
        
        
            
    
    
    
            
          
My_App().run()
    
        
