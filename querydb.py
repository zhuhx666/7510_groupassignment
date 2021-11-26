from logging import error
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mandel_lib import *
# from reg import RegisterScreen
# from login import LoginScreen
# from personal import PersonalScreen
# from database import ListScreen
# from database import BtnScreen
from firebase import Firebase
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

if platform in ('win', 'macosx'):
    Window.size = (414, 736)
    Window.top = 50

config = {
    'apiKey': '',
    'authDomain':'comp7510-lab4ex.firebaseapp.com',
    'databaseURL':'https://comp7510-lab4ex-default-rtdb.firebaseio.com/',
    'storageBucket':'comp7510-lab4ex.appspot.com',
    'serviceAccount': {
        "type": "service_account",
        "project_id": "comp7510-lab4ex",
        "private_key_id": "94308661b3ec0885a95c6a56d038f3c0cb9348f2",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCTOEsUbV0SPbE5\njy5elotgCUItvLRYu9W8OIOJZALj2fwfQYZQshh1MkzvZVXr4BBx/KvVBFjM6J6V\nVL8pCOH0h5XvXA1xViom+8q1zIKuIvkhhDCozI6DWQdjp+thrYrBKDABnHCtlxy8\nxEHsuvtzONBcDful1bDQMsxxy4yZ1sKHDoKy3NFYQrpw+PJpuJlxRWbeobB78pyc\noAzTUwl396dM38OcZz91kaFgwsJDh+dTLtxays2f3SXU3/XgC3QX0aDkzQ/rP99+\nVA7iOkkITQ0cXQXB4V9jEMhwyVdWdZfQX84fOnh1r1JIX1pc9TOsfffpWVSazX6X\nZEekv5gXAgMBAAECggEAAhv9X2aNvdQqdOOrS2mmx5J6Y0Nf5iGS12aL4+0N6YvX\nA++haAiVNyCoX4m5KG8GbUusfpnYV99BXmxfbMwWyLUkndBY1PXiFrrm1aH/gVU4\n8pT9SX3c0N72ryPZyIV/BnN39J30M1iF7eJ1+1lWfvkiax88Ks0cAm+n5D2BXzbh\n9GaGXwb84a05ehJeTLd7mjjTaB6PR4lFcFv7PKRFb+XpoKHB2u2WY4DWV1qt8Zmq\n6s83SYufrRUNshwaO1EZLj/8DE17dmn0g8sALcXyuzLuVCIzrnqsUfkC3Y03sZB+\nWLHzyv5C+MJBiWrNqKolNPfVHXxUB8VV7taGXvUcAQKBgQDELDreHhWN2Z3q/L9u\ndzMQblRSxB98rsKeH9pVLlB38ChuvyVyUGY0khpuk0PFHhCycXzh0A6d93WbQacI\nEbgAQzGWzNbaCtVYh6h+vJ37ulLCRZPj44b2Mve1SrhVxeYShLyaxfAU2dqxk4zT\ngRrnlXGCGXZBF4y3Bmu4MjWGFwKBgQDAHiwJk5cIbOTWMGHDcnHRnJaqnEo0UhS8\n4llSDmEmVy+WvD4jTuHgVV0RfVZJIkzOyardKbPyZWk81LVtjir3sFH8Yj7LTnHo\nXH5QabvKIRX08VvbnepqGjJ5O08ZV81unZ4pAPGFaMlei9XHEm6kqfxaMIzIyPJX\nvY65B0O+AQKBgEz87r1tIRhiZ09pkddQgIHaSs2QmqrcCxTze0QiwQHRBo0wBwot\n825+SFFNCjO58OOXFmOou5PTIhykT2EjUwsHU9bS3R8FUWVFGCNk8rtwDDqiA8BT\n8wt8RSqpAF7pI7nwzfQP6oDEXseCGKqI6H4qcDmWtIonK9pIcs3/JnJRAoGAAzB9\nCquoljs4kVW8ScJcoV44Ihz2Hmg+b+RSF0ql0j0gTSBS58MnfNHt+ZxbElu/aq9u\nZr2Kfzuvw5LEcE0r6XDD66y13iovOexPLIaU14Y1Fxvqqnq0qY5FyD1z0rficTOs\nrIGXgN98eFVZ9zQXIiSwS88Ch1LOsyYyeF/mgAECgYAnHW9utvVYTBxScUxe8IIS\nmDqzGJ9V3zKAUikgRMtIW385YJ/WzRKZ5hVGK35fVGiVUweUxRSm/4srFDVd1ow3\nAEK0w+vs1NvmTP28Ar84DRoJNYob8Bt7f5jau5mAC+s0yHd4HkVRgeWH7Zf5MG3z\nPTEyE2fVertH1fPmHlKFzg==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-n5oba@comp7510-lab4ex.iam.gserviceaccount.com",
        "client_id": "112827568008122639408",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-n5oba%40comp7510-lab4ex.iam.gserviceaccount.com"
    }
}

myfirebase = Firebase(config)
db = myfirebase.database()
storage = myfirebase.storage()


class QueryScreendb(Screen):

    def back(self):
        app = MDApp.get_running_app()
        app.manager.transition.direction = 'left'
        app.manager.current = 'ListScreen'
        print('BACK')
        
    def show_dialog(self):
        dialog = MDDialog(
            title = 'Dialog',
            text = 'Content cannot be empty',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
        dialog.open()

    
    def to_search(self):
        content = self.ids.content_field.text
        content = content.strip()
        if len(content) == 0:
            self.show_dialog()
            return

        # def show_username():
        #     dialog = MDDialog(
        #         title = 'Dialog',
        #         text = v['reply']+v['time']+v['topic']+v['username'],
        #         buttons = [
        #             MDRaisedButton(
        #                 text = 'Close',
        #                 on_release = lambda x: dialog.dismiss()),
        #         ]
        #     )
        #     dialog.open()

        def show_database():
            dialog = MDDialog(
                title = 'Dialog',
                text = 'emailaddress: '+w['emailaddress']+', '+'id: '+w['id']+', '+'password: '+w['password']+', '+'phonenumber: '+w['phonenumber'],
                buttons = [
                    MDRaisedButton(
                        text = 'Close',
                        on_release = lambda x: dialog.dismiss()),
                ]
            )
            dialog.open()
        result = db.child('/Forum').get().val()
        # for k,v in result.items():
        #     if content in v['username']:
        #         show_username()
        #         break
        #         # print('username', v)
        #         # dialog.open()
        #     if content in v['reply']:
        #         # print('reply', v)
        #         show_username()
        #         break

        result1 = db.child('/Userlist').get().val()
        for l,w in result1.items():
            if content in w['id']:
                show_database()
                break
                # print('username', v)
                # dialog.open()
