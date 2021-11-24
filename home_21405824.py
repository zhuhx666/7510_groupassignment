from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mandel_lib import *
from reg_21405824 import RegisterScreen
from login_21405824 import LoginScreen
from personal_21405824 import PersonalScreen
from database_21405824 import ListScreen
from database_21405824 import BtnScreen

from forums_21461295 import forums
from forums_21461295 import post #21461295

from kivy.core.window import Window
from kivy.utils import platform
if platform in ('win', 'macosx'):
    Window.size = (414, 736)
    Window.top = 50

class HomeScreen(Screen):
    def to_login(self):
        MDApp.get_running_app().switchTo('LoginScreen')
        app = MDApp.get_running_app()
        app.manager.transition.direction = 'left'

    def to_register(self):
        MDApp.get_running_app().switchTo('RegisterScreen')
        app = MDApp.get_running_app()
        app.manager.transition.direction = 'left'

class MyApp(MDApp):
    manager = None

    def build(self):
        Builder.load_file('home_21405824.kv')
        Builder.load_file('reg_21405824.kv')
        Builder.load_file('login_21405824.kv')
        Builder.load_file('personal_21405824.kv')
        Builder.load_file('database_21405824.kv')
#############################################################################################
        # Builder.load_file('function_21461295.kv')
        Builder.load_file('forums_21461295.kv') 
        Builder.load_file('post_21461295.kv')#21461295 +personal_21405524.kv(OneLineListItem)+personal_21405524.py(to_forums)
        ######################################+login_21405824.py
#############################################################################################  
        manager = self.manager = ScreenManager()

        manager.add_widget(HomeScreen())
        manager.add_widget(LoginScreen())
        manager.add_widget(RegisterScreen())
        manager.add_widget(ListScreen())
        manager.add_widget(BtnScreen())
        manager.add_widget(PersonalScreen())
#############################################################################################        
        # manager.add_widget(function())
        manager.add_widget(forums())
        manager.add_widget(post()) #21461295
#############################################################################################  
        return manager

    def switchTo(self, screen_name):
        self.manager.current = screen_name

if __name__ == '__main__' :
    MyApp().run()
