from kivymd.app import MDApp

from kivymd_extensions.sweetalert.sweetalert import SweetAlert
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard

from kivy.lang import Builder 

# Plataform definitions
# Window Linux or Android 
from kivy.utils import platform
if platform == 'win':
    import datetime
    import sqlite3
    import os 
    PATH = os.path.dirname( __file__ )
    # Import socket functions and define host:port
    import socket
    SERVER = '127.0.0.1'
    LOGIN_PORT = 50505


### A swipe sensitive Screen, parent of all screen layouts
from gestures4kivy import CommonGestures
class SwipeScreen(MDScreen, CommonGestures):
    def cgb_horizontal_page(self, touch, right):
        MDApp.get_running_app().swipe_screen(right)

# Tela de login e card de cadastro de novo usuário 
class CardNewUser( MDCard ):
    def close_card( self ): 
        self.parent.remove_widget( self ) 

class Login( SwipeScreen, MDScreen ):
    KV_FILE = PATH + '\\login_page.kv'
    keep_login_data = False
    login_client = None 
    USER_ID = False
    PAGE = None 

    def __init__(self, **args):
        super().__init__(**args)
        self.PAGE = Builder.load_file( self.KV_FILE )
        self.heroes_to = []
        self.add_widget( self.PAGE )
    
    def raise_card(self, **args):
        self.add_widget( CardNewUser() )
    
    def keep_data(self, user, password):
        print( 'Salvar os dados de login:' )

    def on_enter(self): 
        # Inicia o socket de login
        state = self.connect_server()
        if not state:
            # Clock.schedule_once( self.connect_server, 1 )
            pass 
        return super().on_enter()
    
    def connect_server(self, rise_alert : bool = False ):
        if platform == 'win':
            try:
                self.login_client = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
                self.login_client.connect( (SERVER, LOGIN_PORT) )
                self.login_client.settimeout( 1 )
                return True 
            except socket.error as e :
                if rise_alert:
                    SweetAlert( timer = 2 ).fire( 'O servidor de login não esta conectado.\n{}'.format(str(e)), type='question')
                return False 
        return False 
    
    def login(self, name, password ):
        if platform == 'win':
            try:
                self.login_client.send( ('LGN;' + name + ';' + password + ';').encode() ) 
                USER_ID = self.login_client.recv( 1024 ).decode()
            except socket.error as e:         
                SweetAlert( timer = 2 ).fire( str(e), type='failure' )
                USER_ID = False
            if USER_ID == '-1':
                SweetAlert( timer = 1 ).fire('Usuário ou senha incorretos [COD -1]', type='failure' )
            else: 
                if USER_ID == False: 
                    return False 
                print( 'User ID: ', USER_ID )
                self.manager.current = 'home'
                self.enable_swipe = True
                self.USER_ID = USER_ID 
                # VERIFICAR SE RETEM USUÁRIO E SENHA OU NÃO
    
    def create_new_user( self, user, password, family  ):
        if platform == 'win':
            if user and password:
                data = 'NEW;' + user + ';' + password + ';' + family
                try: 
                    self.login_client.send( data.encode() )  
                    STATE = self.login_client.recv( 1024 )
                    if STATE:
                        SweetAlert( timer = 1 ).fire('Usuário criado com sucesso', type='success' )
                        self.screens['Login'].children[0].close_card()
                    else: 
                        SweetAlert( timer = 1 ).fire( 'Erro ao criar novo usuário', type = 'failure' )  
                except socket.error as e:  
                    SweetAlert( timer = 1 ).fire( 'Erro ao criar novo usuário', type = 'failure' )   
            else:
                SweetAlert( timer = 2 ).fire( 'Usuário e senha inválidos', type = 'failure' )

    def close_card( self, id ): 
        self.remove_widget( id ) 
