# from kivymd.tools.hotreload.app import MDApp
from kivymd.app import MDApp

from kivymd.uix.screenmanager import MDScreenManager
from screens import LoginPage, HomePage, ExtratoPage, ProfitPage


# Plataform definitions
# Window Linux or Android 
from kivy.utils import platform
if platform == 'win':
    # Resolution 
    from kivy.core.window import Window
    Window.size = (435, 700)
    #  Second SCREEN  #
    ###################
    Window.left = -500
    ###################
    Window.top  = 50


class App( MDApp ):
    # Hot loader macro 
    DEBUG  = True 
    KV_FILES = [
        'views/loginScreen/login_page.kv', 
        'views/homeScreen/home.kv', 
        'views/profitScreen/profit.kv', 
        'views/extratoScreen/extrato.kv', 
        ]
    
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "DeepOrange"        
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = "Light"

        # To navigate through the screens
        self.enable_swipe = True
        self.manager = MDScreenManager()
        self.manager.current_heroes = []
        self.screens = {
            'Login':    LoginPage   ( name = 'login'  ), 
            'Home':     HomePage    ( name = 'home'   ),
            'Extrato':  ExtratoPage ( name = 'extrato'),
            'Profit':   ProfitPage  ( name = 'profit' )}
        
        for s in self.screens.values():
            self.manager.add_widget(s)
        
        ## JUST FOR DEBUG
        self.manager.current_heroes = ['header', 'footer']
        self.change_screen( 'home')

        return self.manager
    
    # Swipe the screen, usedo in the main loop of application 
    def swipe_screen(self, right):
        if self.enable_swipe:
            page = self.manager.current
            if right:
                if page == 'profit':
                    self.manager.transition.direction = 'right'
                    self.change_screen( 'home'  )
                    self.screens['Home'].PAGE.ids.profit_icon_button.icon_color  = [ 1,1,1,1]
                    self.screens['Home'].PAGE.ids.profit_text_button.text_color  = [ 1,1,1,1]            
                    self.screens['Home'].PAGE.ids.extrato_icon_button.icon_color = [ 1,1,1,1]
                    self.screens['Home'].PAGE.ids.extrato_text_button.text_color = [ 1,1,1,1]
                elif page == 'home': 
                    self.manager.transition.direction = 'right'
                    self.change_screen( 'extrato' )
                    self.screens['Home'].PAGE.ids.extrato_icon_button.icon_color = [212/255, 175/255, 55/255, 1]
                    self.screens['Home'].PAGE.ids.extrato_text_button.text_color = [212/255, 175/255, 55/255, 1]
            else: # left 
                if page == 'extrato':
                    self.manager.transition.direction = 'left'
                    self.change_screen( 'home' )
                    self.screens['Home'].PAGE.ids.profit_icon_button.icon_color  = [ 1,1,1,1]
                    self.screens['Home'].PAGE.ids.profit_text_button.text_color  = [ 1,1,1,1]            
                    self.screens['Home'].PAGE.ids.extrato_icon_button.icon_color = [ 1,1,1,1]
                    self.screens['Home'].PAGE.ids.extrato_text_button.text_color = [ 1,1,1,1]
                elif page == 'home':
                    self.manager.transition.direction = 'left'
                    self.change_screen( 'profit' )
                    self.screens['Home'].PAGE.ids.profit_icon_button.icon_color  = [212/255, 175/255, 55/255, 1]
                    self.screens['Home'].PAGE.ids.profit_text_button.text_color  = [212/255, 175/255, 55/255, 1]


    def change_screen( self, screen  ):
        self.manager.current = screen
    def change_swipe( self, state ):
        self.enable_swipe = state 
    
    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
        if "ctrl" in modifiers and text == "r":
            self.rebuild()


if __name__ == '__main__':
    App().run()
    