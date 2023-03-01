from kivy.lang import Builder

from kivymd.tools.hotreload.app import MDApp

from kivymd.uix.floatlayout import MDFloatLayout

from kivy.utils import platform
if platform == 'win':
    from kivy.core.window import Window
    Window.size = (435, 700)

import os 
PATH = os.path.dirname( __file__ )


class Footer(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Example(MDApp):
    KV = PATH + '\\footer.kv'
    DEBUG = True  
    KV_FILES = [PATH + "\\footer.kv"]

    def build_app(self):
        return Builder.load_file(self.KV)


Example().run()
