from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreenManager:
    SwipeScreen:
        name: "screen A"
        md_bg_color: "lightblue"
        MDHeroFrom:
            id: hero_header
            tag: 'header'
            pos_hint: {'center_x': .5, 'center_y' : 0.5 }
            size_hint: 1, 1
            MDBoxLayout:
                md_bg_color: app.theme_cls.primary_color
                orientation: 'horizontal'
                pos_hint: {'center_x': .5, 'center_y' : 1-0.15/2 }
                size_hint: 1, .15
                elevation: 2
                cols: 3
                # Image / last access 
                MDBoxLayout:
                    size_hint: 0.25, 1 
                    orientation: 'vertical'
                    padding: [10,10,10,10]
                    MDCard:
                        radius: 50
                        md_bg_color: 1,1,1,1
                        pos_hint: {"center_x": .5, "center_y": .5}
                        height: '100dp'
                        shadow_softness: 12
                        shadow_offset: 0, 2 
                        elevation: 4
                        FitImage:
                            id: user_photo
                            source: "icons\\handsome.jpg"
                            pos_hint: { "top": 1 }
                            radius: 50,50,50,50
                # ADICIONAR NA IMAGEM O BEHAVIOR HOVER//SELECTED 
                # abrir um card para selecionar uma foto/ editar ou excluir 
                # Name 
                MDBoxLayout: 
                    size_hint: 0.4, 1 
                    MDLabel:
                        id: user_name  
                        text: 'Nome do usuário'
                        font_size: 20
                        valing: 'midlle' 
                        halign: 'center'
                        bold: True
                        elevation: 4
                # Informações de renda 
                MDBoxLayout:
                    size_hint: 0.35, 1 
                    orientation: 'vertical'
                    Label: 
                        size_hint: .8, .2
                    MDLabel:
                        size_hint: 1, .4
                        text: 'Renda total'
                        font_size: 20 
                        valing: 'bottom' 
                        halign: 'center'
                    MDLabel: 
                        size_hint: 1, .2
                        id: user_income
                        text: 'R$ xx.xxx,xx'
                        font_size: 14
                        bold: True 
                        valing: 'top' 
                        halign: 'center'
                    Label: 
                        size_hint: .8, .2

                
        MDRaisedButton:
            text: "Move Hero To Screen B"
            pos_hint: {"center_x": .5}
            y: "36dp"
            on_release:
                root.current_hero = "header"
                root.current = "screen B"

    MDScreen:
        name: "screen B"
        heroes_to: [hero_to_kivymd]
        md_bg_color: "cadetblue"
        
        MDHeroTo:
            id: hero_to_kivymd
            tag: 'header'
            pos_hint: {'center_x': .5, 'center_y' : 0.5 }
            size_hint: 1, 1
        MDRaisedButton:
            text: "Move Hero To Screen A"
            pos_hint: {"center_x": .5}
            y: "36dp"
            on_release:
                root.current_hero = "header"
                root.current = "screen A"
                print(type(root.current_hero))
'''

from kivymd.uix.screen import MDScreen
from gestures4kivy import CommonGestures
class SwipeScreen(MDScreen, CommonGestures):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def cgb_horizontal_page(self, touch, right):
        MDApp.get_running_app().swipe_screen(right)


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()