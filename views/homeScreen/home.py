from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard 
from kivy.properties import StringProperty, NumericProperty,ColorProperty
from kivy.lang import Builder 

import os 
PATH = os.path.dirname( __file__ )

### A swipe sensitive Screen, parent of all screen layouts
from gestures4kivy import CommonGestures
class SwipeScreen(MDScreen, CommonGestures):
    def cgb_horizontal_page(self, touch, right):
        MDApp.get_running_app().swipe_screen(right)


class MDCardValue( MDCard ):
    icon             = StringProperty()   
    type             = StringProperty()   
    used_value       = StringProperty()       
    to_use_value     = StringProperty()           
    available_value  = StringProperty()           
    progress_value   = NumericProperty()          
    color_available  = ColorProperty()            
    def __init__(self, icon, type, used_value, to_use_value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = icon                   
        self.type = type                   
        self.used_value = 'R$' + str( used_value)              
        self.to_use_value = 'R$' + str( to_use_value )   
        available_value =  to_use_value - used_value
        if available_value > 0:
            self.color_available = [119/255, 221/255, 119/255, 0.95 ]
        elif available_value < 0:
            self.color_available = [196/255, 2/255, 51/255, 0.95 ]
        else: 
            self.color_available = [255/255, 247/255, 85/255, 0.95 ]
        self.available_value = 'R$' + str( available_value )
        self.progress_value = round(used_value/to_use_value*100, 3)

from random import randint 

# Tela inicial do aplicativo após logado 
class Home( SwipeScreen ):
    KV_FILE = PATH + '\\home.kv'
    already_draw = False 
    PAGE = None
    def __init__(self, **args):
        super().__init__(**args)
        self.PAGE = Builder.load_file(self.KV_FILE)
        self.heroes_to = [ self.PAGE.ids.hero_header, self.PAGE.ids.hero_footer ]
        self.add_widget( self.PAGE )
    

    def on_pre_enter(self, *args):
        if not self.already_draw:
            self.draw_screen()
            self.already_draw = True 
        return super().on_pre_enter(*args)
    

    def draw_screen(self):
        # Pegar os valores do banco de dados 
        name = 'Bruno'
        family_name = 'Sampaio'
        user_name = name + ' ' + family_name
        user_photo_link = "icons\\handsome.jpg"
        user_income = 'R$10.523,00' 
        
        self.PAGE.ids.user_photo.source = user_photo_link
        self.PAGE.ids.user_name.text = user_name
        self.PAGE.ids.user_income.text = user_income
        
        icons = ['home', 'horse', 'car', 'cloud', 'book-multiple-outline', 'pencil', 'pac-man', 'android', 'feet']
        types = ['Mansão do Neymar', 'Pasto', 'Pneu novo', 'Roupas Carmen Steffens ', 'Papiros', 'Material escolar', 'Jogos retor', 'Reparo do celular', 'Tenis de corrida']
        NUM_OBJ = 8
        padding = 10 
        for i in range(NUM_OBJ):
            self.PAGE.ids.home_page_id.height = NUM_OBJ*100 + padding + 105 # jerk spaces ( init = 65, end = 60 )
            self.PAGE.ids.home_page_id.add_widget(   
                MDCardValue( 
                    icon = icons[i],
                    type = types[i],
                    used_value = randint(100, 10_000),
                    to_use_value = randint(100, 10_000)
                ))
        # Jerk space 
        self.PAGE.ids.home_page_id.add_widget( MDCard( size_hint_y = None, height = 70, padding = 10, md_bg_color = [0,0,0,0]) )
