from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.spinner import Spinner
from kivy.app import App


Builder.load_string('''
<MainScreen>:
    GridLayout:      
        orientation: 'lr-tb'
        cols: 1
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  
            Rectangle:
                pos: self.pos
                size: self.size
        GridLayout:      
            orientation: 'lr-tb'
            cols: 2
            Spinner:
                id: first
                text: ' First Number'
                values: ['1','2','3','4','5','6','7','8','9'] 
            Spinner:
                id: second
                text: ' Second Number'
                values: ['1','2','3','4','5','6','7','8','9']       
        Label:
            id: result
            text: ' Result'
            color: 0,0,0,1
        Button:
            id: res
            on_press: root.onPow(first.text,second.text)
            text: 'Progress'
''')

class MainScreen(FloatLayout):
    changet = StringProperty() 
    def __init__(self, **kwargs):          
        super(MainScreen, self).__init__(**kwargs)
    def onPow(self,fir,sec):
        a = 0
        b = 0
        for i in range((10000)):
            print(b)
            self.ids.result.text=str(b*(int(fir)*int(sec)+i))
            b+=1
class TestApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__": 
    TestApp().run() 