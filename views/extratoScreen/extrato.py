from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 

from kivymd.uix.expansionpanel import MDExpansionPanelThreeLine
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton

from kivy.properties import StringProperty, NumericProperty,ColorProperty


from kivy.utils import platform
if platform == 'win':
    import datetime 
    import os 
    PATH = os.path.dirname( __file__ )


### A swipe sensitive Screen, parent of all screen layouts
from gestures4kivy import CommonGestures
class SwipeScreen(MDScreen, CommonGestures):
    def cgb_horizontal_page(self, touch, right):
        MDApp.get_running_app().swipe_screen(right)

class ExtratoList(MDFlatButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MonthsCards( MDFlatButton ):
    month = StringProperty()   
    def __init__(self, month : str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.month = month 
        
        
class Extrato( SwipeScreen, MDScreen ):
    KV_FILE = PATH + '\\extrato.kv'
    already_draw = False 
    PAGE = None 

    def __init__(self, **args):
        super().__init__(**args)
        self.PAGE = Builder.load_file(self.KV_FILE)
        self.heroes_to = [ self.PAGE.ids.extrato_header, self.PAGE.ids.extrato_footer ]
        self.add_widget( self.PAGE )

    def on_enter(self, *args):
        if not self.already_draw: 
            self.draw_screen()
            self.already_draw = True 
        return super().on_enter(*args)


    def draw_screen(self):
        # data = get_data_somewhere() -> [ icon_name, text, secondary_text, user, value, date ]
        for _ in range(10):
                self.PAGE.box.add_widget(
                    MDExpansionPanel(
                        icon = "plus",
                        content = ExtratoList(
                            '', # Icon
                            '', # Text
                            '', # Secondary_text
                        ),
                        panel_cls = MDExpansionPanelThreeLine(
                            text = "Text",
                            secondary_text = "Secondary text",
                            tertiary_text = "Tertiary text",
                        )
                    )
                )

        month_index = 'janeiro,fevereiro,março,abril,maio,junho,julho,agosto,setembro,outubro,novembro,dezembro'.upper().split(',')
        for n, month in enumerate(month_index):
            if n+1 == datetime.datetime.now().month:     
                self.PAGE.extrato_months.add_widget(
                    MonthsCards( month = month, md_bg_color = [1,1,0,1], text_color = [0.2,0.2,0.2,1] )
                )
            else:
                self.PAGE.extrato_months.add_widget(
                    MonthsCards( month = month )
                )