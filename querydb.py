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

# config = {
#     'apiKey': '',
#     'authDomain':'comp7510-lab4ex.firebaseapp.com',
#     'databaseURL':'https://comp7510-lab4ex-default-rtdb.firebaseio.com/',
#     'storageBucket':'comp7510-lab4ex.appspot.com',
#     'serviceAccount': {
#         "type": "service_account",
#         "project_id": "comp7510-lab4ex",
#         "private_key_id": "94308661b3ec0885a95c6a56d038f3c0cb9348f2",
#         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCTOEsUbV0SPbE5\njy5elotgCUItvLRYu9W8OIOJZALj2fwfQYZQshh1MkzvZVXr4BBx/KvVBFjM6J6V\nVL8pCOH0h5XvXA1xViom+8q1zIKuIvkhhDCozI6DWQdjp+thrYrBKDABnHCtlxy8\nxEHsuvtzONBcDful1bDQMsxxy4yZ1sKHDoKy3NFYQrpw+PJpuJlxRWbeobB78pyc\noAzTUwl396dM38OcZz91kaFgwsJDh+dTLtxays2f3SXU3/XgC3QX0aDkzQ/rP99+\nVA7iOkkITQ0cXQXB4V9jEMhwyVdWdZfQX84fOnh1r1JIX1pc9TOsfffpWVSazX6X\nZEekv5gXAgMBAAECggEAAhv9X2aNvdQqdOOrS2mmx5J6Y0Nf5iGS12aL4+0N6YvX\nA++haAiVNyCoX4m5KG8GbUusfpnYV99BXmxfbMwWyLUkndBY1PXiFrrm1aH/gVU4\n8pT9SX3c0N72ryPZyIV/BnN39J30M1iF7eJ1+1lWfvkiax88Ks0cAm+n5D2BXzbh\n9GaGXwb84a05ehJeTLd7mjjTaB6PR4lFcFv7PKRFb+XpoKHB2u2WY4DWV1qt8Zmq\n6s83SYufrRUNshwaO1EZLj/8DE17dmn0g8sALcXyuzLuVCIzrnqsUfkC3Y03sZB+\nWLHzyv5C+MJBiWrNqKolNPfVHXxUB8VV7taGXvUcAQKBgQDELDreHhWN2Z3q/L9u\ndzMQblRSxB98rsKeH9pVLlB38ChuvyVyUGY0khpuk0PFHhCycXzh0A6d93WbQacI\nEbgAQzGWzNbaCtVYh6h+vJ37ulLCRZPj44b2Mve1SrhVxeYShLyaxfAU2dqxk4zT\ngRrnlXGCGXZBF4y3Bmu4MjWGFwKBgQDAHiwJk5cIbOTWMGHDcnHRnJaqnEo0UhS8\n4llSDmEmVy+WvD4jTuHgVV0RfVZJIkzOyardKbPyZWk81LVtjir3sFH8Yj7LTnHo\nXH5QabvKIRX08VvbnepqGjJ5O08ZV81unZ4pAPGFaMlei9XHEm6kqfxaMIzIyPJX\nvY65B0O+AQKBgEz87r1tIRhiZ09pkddQgIHaSs2QmqrcCxTze0QiwQHRBo0wBwot\n825+SFFNCjO58OOXFmOou5PTIhykT2EjUwsHU9bS3R8FUWVFGCNk8rtwDDqiA8BT\n8wt8RSqpAF7pI7nwzfQP6oDEXseCGKqI6H4qcDmWtIonK9pIcs3/JnJRAoGAAzB9\nCquoljs4kVW8ScJcoV44Ihz2Hmg+b+RSF0ql0j0gTSBS58MnfNHt+ZxbElu/aq9u\nZr2Kfzuvw5LEcE0r6XDD66y13iovOexPLIaU14Y1Fxvqqnq0qY5FyD1z0rficTOs\nrIGXgN98eFVZ9zQXIiSwS88Ch1LOsyYyeF/mgAECgYAnHW9utvVYTBxScUxe8IIS\nmDqzGJ9V3zKAUikgRMtIW385YJ/WzRKZ5hVGK35fVGiVUweUxRSm/4srFDVd1ow3\nAEK0w+vs1NvmTP28Ar84DRoJNYob8Bt7f5jau5mAC+s0yHd4HkVRgeWH7Zf5MG3z\nPTEyE2fVertH1fPmHlKFzg==\n-----END PRIVATE KEY-----\n",
#         "client_email": "firebase-adminsdk-n5oba@comp7510-lab4ex.iam.gserviceaccount.com",
#         "client_id": "112827568008122639408",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-n5oba%40comp7510-lab4ex.iam.gserviceaccount.com"
#     }
# }

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
