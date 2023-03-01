from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.dialog import MDDialog 
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.lang import Builder


class App( MDApp ):
        
    KV = """
Screen: 
    MDBoxLayout:
        md_bg_color: .1, .1, .1, .8
        pos_hint: {'center_x': 0.5,'center_y': 0.425 }
        orientation: 'vertical'
        elevation: 0
        
        MDRectangleFlatButton: 
            text: 'Some alert popup'
            pos_hint: {'center_x': .5, 'center_y': .5 }
            on_release: app.pop_up() 

        MDLabel: 
            id: label
            text:  'Some text'
"""
    def build_app(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "DeepOrange"        
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = "Dark"
    
        return Builder.load_string( self.KV )

    dialog = None 
    def pop_up(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text = 'popup',
                title = 'Some dialog title',
                buttons = [
                    MDFlatButton(
                        text = 'CANCEL',
                        on_release = self.dismiss 
                    ),
                    MDRectangleFlatButton(
                        text = 'OK',
                        on_release = self.dismiss
                    )
                ]
            )
        self.dialog.open() 

    def dismiss(self, obj ):
        self.dialog.dismiss()

if __name__ == '__main__':
    App().run()