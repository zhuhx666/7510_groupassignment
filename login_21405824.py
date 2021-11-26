from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mandel_lib import *
from firebase import Firebase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

# from query import QueryScreen
from forums_21461295 import forums
from forums_21461295 import post

from reg_21405824 import RegisterScreen
# from login_21405824 import LoginScreen
from personal_21405824 import PersonalScreen
from database_21405824 import ListScreen
from database_21405824 import BtnScreen

from forums_21461295 import forums
from forums_21461295 import post #21461295

from query import QueryScreen
from querydb import QueryScreendb

from photoshow_wyb import showscreen
from sharing_page_wyb import share

from kivy.core.window import Window
from kivy.utils import platform
if platform in ('win', 'macosx'):
    Window.size = (414, 736)
    Window.top = 50

config = {
    'apiKey': '',
    'authDomain': 'comp7510-6c8da.firebaseapp.com',
    'databaseURL': 'https://comp7510-6c8da-default-rtdb.firebaseio.com/',
    'storageBucket': 'comp7510-6c8da.appspot.com',
    'serviceAccount': {
        "type": "service_account",
        "project_id": "comp7510-6c8da",
        "private_key_id": "c0fbe38f86348192163f1506a970b5b37ea97e26",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDlj5pvlVFMvRG4\n9mUUsblo3cCyEgo7NUedVwy6X/z1Hk2v2h4vKXx03E/YUprnA1lcrdV4+LffBYe+\nyV6s6vuKJxqxt5/gThUpjJXAdGBFMkoS8/0GFeaRiwkN7EYvV7OdTZJ/OfIP3xDK\nkaTDtzqi0V1U0aVKAQa6wneiHOTIYi/3Mrgmo4LhO0Cj/egJkOmw5jC2JvLv2lZ2\nSsEJ5RSBjiUBAmA64cjRWWpSNI6cpP7U2CNjE+zR3imCCNmGkPa1ibYQxJCK2CJs\ndbE13fKgti/qPxpNrd4Mc0Ex8Oa90SQTd4f4ktUdyyEdX4aItLHnEQwUBypAZKaT\n0KBwau6RAgMBAAECggEABipIPMPEbPHtTQEgX6un6IMqHBjZbv55klDGmKZ1d0oi\nznymZQsGxWcEUEbkU5zL/y3zptMmhwYRlPljV56w9jnMy6Xm6eHW9ihz03kcpnHD\nuloUpcpGngqJ9KEvlQZp3mk5VxLh53S3cU/ziPETEVEw9z3xI+QT/5szliY+AQv6\n/XMx6eNAdvvfZoJp1+pZ3ixTtYcuVTA57i6cuI6gwchhhBsUkqCPgR8ZTNTu0FiZ\nLzjXIKsy+vXWMP0bgMiTMUWmBYRaPFOk3X8RoCZJxsV7sq4r2yx+DHc32r3TmJ8i\niQlFWjnnS1JcEKgLvlWjAT5+eijVBdNPwQlFfEx+cQKBgQD9EK1E2A4GxJuYnmQC\nKNobjSdRbFRYWNukiDBNYNWEQrgAkgsfryN/+0+TFsJSG1WDqaIy4a7DsfRyQVzK\ntKEt4vlHRiIIT7qADl+vSBsH1ZJzN/f8M4Zg+l3iukP3uTvEFZ6Jwl+W+WvELSyS\n12lcDsOttWqSNc/RKwt7a6sNuQKBgQDoOSUfkMl6xLx+/IaQDVzK40WWBBWaTklm\nyIkHxjJQ7ZiWLOsnbQvsHGhxDZ7eGvoAf2i/L2ya81wf7XgMp3qU1cmDv5AViyp0\nRsy4dUIog+e7deZRHcB6sGBlzmu8ci5Z2IUfTS4WqBn6CyzxSSvSH3+/BX38rilP\n38ROHAMTmQKBgG2XNEH1ApYBvJQqO4sH3/RAe39yV1BvIqcs5yYLQkvljMOKe1C8\nSrZYwcwj9gESn0TGSFyaiVFsFj0Ie0O5V3eErIkmIQTSaiSclOlWY4ZQAfzthvHr\n6kzC/7d5DIgR6oTvC9oCl9zMpNOu8Hei25inOCxYvQ8WSKn/ZxiKtufZAoGBAKJj\n267wK8SbMQlIA71Was5CEdYu8wBdwHyMvS5fja4ECFD0Blkiq1SoJOzxzmeYy7xv\nXEtdmX/dsE1vXSTUNSdBPNLRsasvDzgSjnRrIyF75B+1+aI9wOzKzA5FRBeabQlN\nHQJfkVwsn0W4bOwp8+fTORzWdVyuWZtOalMIyan5AoGAITEIcFiDOqk5cqMZoAl1\naFEeyL9qoX9nzu9mdVOutsx2taCT4h2WPXABNwm6uJa64jU0VA1igwXw7/Qc2a1q\n3jBJjBsQ7akELYVgiwUSGOaJiWJXz1URG27PUFhguz8PQeVhl/EdzDF1XKzNz6sm\nELcUtR/TrSRfzblrNvnNIoc=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-3e883@comp7510-6c8da.iam.gserviceaccount.com",
        "client_id": "108067384295080648816",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-3e883%40comp7510-6c8da.iam.gserviceaccount.com"
    }
}

myfirebase = Firebase(config)
db = myfirebase.database()

class LoginScreen(Screen):
    
    def login(self):
        global id
        try:
            id = str(self.ids.txt_id.text)
            ppassword = str(self.ids.txt_password.text)
        except:
            LoginScreen.error_dialog(self)
        else:
            if id == '' or ppassword == '' :
                LoginScreen.show_dialog(self)
            else:
                result = db.child('/Userlist').get().val()
                try:
                    x = result[f'{id}']
                except:
                    LoginScreen.id_dialog(self)
                else:
                    if result[f'{id}']['password'] == '123456':
                        print('Entering administrator account')
                        self.ids.txt_id.text = ''
                        self.ids.txt_password.text = ''
                        MDApp.get_running_app().switchTo('ListScreen')
                    elif result[f'{id}']['password'] == ppassword:
                        print('Successful Login')
                        self.ids.txt_id.text = ''
                        self.ids.txt_password.text = ''
                        app = MDApp.get_running_app()
                        personalscreen = app.manager.get_screen('PersonalScreen')

                        forumsscreen = app.manager.get_screen('forums')#21461295
                        postscreen = app.manager.get_screen('post')#21461295

                        queryscreen = app.manager.get_screen('QueryScreen')

                        sharescreen = app.manager.get_screen('share')
                        #################################################################
                        # screen.key = self.key
                        personalscreen.title = id

                        forumsscreen.user = id#21461295
                        postscreen.user = id#21461295
                        forums.user = id
                        post.user = id
                        queryscreen.title = id

                        sharescreen.title = id

                        print(personalscreen.title)
                        personalscreen.label_text = result[f'{id}']['emailaddress']
                        personalscreen.content = result[f'{id}']['password']
                        personalscreen.phone = result[f'{id}']['phonenumber']

                        app.manager.transition.direction = 'left'
                        app.manager.current = 'PersonalScreen'
                    else:
                        LoginScreen.password_dialog(self)

        return

    def to_register(self):
        self.ids.txt_id.text = ''
        self.ids.txt_password.text = ''
        MDApp.get_running_app().switchTo('RegisterScreen')

    def cancel(self):
        self.ids.txt_id.text = ''
        self.ids.txt_password.text = ''
        print('CANCEL')

    # def back(self):
    #     self.ids.txt_id.text = ''
    #     self.ids.txt_password.text = ''
    #     app = MDApp.get_running_app()
    #     app.manager.transition.direction = 'left'
    #     app.manager.current = 'HomeScreen'
    #     print('BACK')

    def error_dialog(self):
        dialog = MDDialog(
            title = 'Dialog',
            text = 'Login fields error!',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
        dialog.open()

    def show_dialog(self):
        dialog = MDDialog(
            title = 'Dialog',
            text = 'Login fields cannot be empty!',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
        dialog.open()

    def password_dialog(self):
        dialog = MDDialog(
            title = 'Dialog',
            text = 'Login password error!',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
        dialog.open()

    def id_dialog(self):
        dialog = MDDialog(
            title = 'Dialog',
            text = 'User does not exist!',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
        dialog.open()

class MyApp(MDApp):
    manager = None

    def build(self):
        # Builder.load_file('home_21405824.kv')
        Builder.load_file('reg_21405824.kv')
        Builder.load_file('login_21405824.kv')
        Builder.load_file('personal_21405824.kv')
        Builder.load_file('database_21405824.kv')
#############################################################################################
        # Builder.load_file('function_21461295.kv')
        Builder.load_file('forums_21461295.kv') 
        Builder.load_file('post_21461295.kv')#21461295 +personal_21405524.kv(OneLineListItem)+personal_21405524.py(to_forums)

        Builder.load_file('query.kv')
        Builder.load_file('querydb.kv')

        Builder.load_file('photoshow_wyb.kv')
        Builder.load_file('sharing_page_wyb.kv')
        ######################################+login_21405824.py
#############################################################################################  
        manager = self.manager = ScreenManager()

        # manager.add_widget(HomeScreen())
        manager.add_widget(LoginScreen())
        manager.add_widget(RegisterScreen())
        manager.add_widget(ListScreen())
        manager.add_widget(BtnScreen())
        manager.add_widget(PersonalScreen())
#############################################################################################        
        # manager.add_widget(function())
        manager.add_widget(forums())
        manager.add_widget(post()) #21461295

        manager.add_widget(QueryScreen())
        manager.add_widget(QueryScreendb())

        manager.add_widget(showscreen())
        manager.add_widget(share())
#############################################################################################  
        return manager

    def switchTo(self, screen_name):
        self.manager.current = screen_name

if __name__ == '__main__' :
    MyApp().run()