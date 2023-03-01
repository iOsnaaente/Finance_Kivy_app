from views.extratoScreen.extrato import Extrato 
from views.profitScreen.profit import Profit
from views.loginScreen.login import Login 
from views.homeScreen.home import Home

class LoginPage( Login ):
    def __init__(self, **args):
        super().__init__(**args)

class HomePage( Home ):
    def __init__(self, **args):
        super().__init__(**args)

class ProfitPage( Profit ):
    def __init__(self, **args):
        super().__init__(**args)

class ExtratoPage( Extrato ):
    def __init__(self, **args):
        super().__init__(**args)