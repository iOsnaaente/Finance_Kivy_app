from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 

import os 
PATH = os.path.dirname( __file__ )


### A swipe sensitive Screen, parent of all screen layouts
from gestures4kivy import CommonGestures
class SwipeScreen(MDScreen, CommonGestures):
    def cgb_horizontal_page(self, touch, right):
        MDApp.get_running_app().swipe_screen(right)


# Tela de estimativas de lucro ou prejuízos ao longo do tempo e 
# estimativas/ascensões de gastos e crescimento do valor ganho ao longo do tempo 
class Profit( SwipeScreen ):
    KV_FILE = PATH + '\\profit.kv'
    already_draw = False
    PAGE = None
    def __init__(self, **args):
        super().__init__(**args)
        self.PAGE = Builder.load_file(self.KV_FILE)
        self.heroes_to = [ self.PAGE.ids.profit_header, self.PAGE.ids.profit_footer ]
        self.add_widget( self.PAGE )


    def on_enter(self, *args):
        print( self.PAGE.ids.profit_header )
        return super().on_enter(*args)
    

    def on_pre_enter(self, *args):
        if not self.already_draw:
            self.draw_screen()
            self.already_draw = True 
        return super().on_pre_enter(*args)

    def draw_screen( self ):
        pass 
    