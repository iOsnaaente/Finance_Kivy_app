from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ColorProperty

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard

from kivymd.app import MDApp

KV = '''
<MDCardValue>:
    size_hint_y: None
    height: 300
    pos_hint: {"center_x": .5, "center_y": .5}
    md_bg_color: "white"
    # focus_behavior: True
    # unfocus_color: "pink"
    # focus_color: "grey"
    padding: 10
    elevation: 3
    orientation: 'vertical'
    MDGridLayout:
        cols: 4 
        orientation: 'lr-tb'
        size_hint: 1, .45
        pos_hint: {'center_x': 0.5, 'center_y': 0.5 }
        MDIconButton:
            icon: root.icon
            valing: 'center'
        MDLabel:
            text: root.type
            pos_hint: {'left': 1, 'center_y': 0.5 }
        MDIconButton:
            icon: 'view-list-outline'
        MDIconButton:
            icon: 'dots-vertical' 

    MDGridLayout:
        cols: 2
        size_hint: 0.95, 0.35
        pos_hint: {'center_x': 0.5, 'center_y': 0.5 }
        MDLabel:
            text: '[color=0f0f0f][b]'+ root.used_value + '[/b][/color] [color=a0a0a0] de ' + root.to_use_value + '[/color]'
            markup : True 
            haling: 'left'
        MDLabel:
            halign: 'right'
            text: root.available_value
            color: root.color_available
            bold: True

    MDProgressBar:
        value: root.progress_value
        color: root.color_available
        size_hint: 0.95, 0.15
        pos_hint: {'center_x': 0.5, 'center_y': 0.5 }
    
    MDGridLayout:
        size_hint: 0.95, 0.1


MDScreen:
    MDBoxLayout:
        id: box
        size_hint: 0.95, 0.6
        pos_hint: {"center_x": .5, "center_y": .5}
        orientation: 'vertical'
        spacing: '10dp'
'''

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

class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def on_start(self):
        scrow = MDScrollView()
        box = MDBoxLayout( orientation = 'vertical', size_hint_y = None, height = 1000 )
        
        box.add_widget( MDCardValue( icon = 'home', type = 'Mercadinho Boa Compra', used_value = 12200, to_use_value = 3200 ) )
        box.add_widget( MDCardValue( icon = 'car', type = 'Flavinho do pneu', used_value = 13000, to_use_value = 56200 ) ) 
        box.add_widget( MDCardValue( icon = 'cow', type = 'Rajadão do filé', used_value = 600, to_use_value = 3200 ) )
        
        scrow.add_widget( box )
        self.root.ids.box.add_widget( scrow )


Example().run()