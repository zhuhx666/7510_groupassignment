# from firebase import Firebase
# import json



# config = {
#     'apiKey': '',
#     'authDomain': 'comp7510-6c8da.firebaseapp.com',
#     'databaseURL': 'https://comp7510-6c8da-default-rtdb.firebaseio.com/',
#     'storageBucket': 'comp7510-6c8da.appspot.com',
#     'serviceAccount': {
#         "type": "service_account",
#         "project_id": "comp7510-6c8da",
#         "private_key_id": "c0fbe38f86348192163f1506a970b5b37ea97e26",
#         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDlj5pvlVFMvRG4\n9mUUsblo3cCyEgo7NUedVwy6X/z1Hk2v2h4vKXx03E/YUprnA1lcrdV4+LffBYe+\nyV6s6vuKJxqxt5/gThUpjJXAdGBFMkoS8/0GFeaRiwkN7EYvV7OdTZJ/OfIP3xDK\nkaTDtzqi0V1U0aVKAQa6wneiHOTIYi/3Mrgmo4LhO0Cj/egJkOmw5jC2JvLv2lZ2\nSsEJ5RSBjiUBAmA64cjRWWpSNI6cpP7U2CNjE+zR3imCCNmGkPa1ibYQxJCK2CJs\ndbE13fKgti/qPxpNrd4Mc0Ex8Oa90SQTd4f4ktUdyyEdX4aItLHnEQwUBypAZKaT\n0KBwau6RAgMBAAECggEABipIPMPEbPHtTQEgX6un6IMqHBjZbv55klDGmKZ1d0oi\nznymZQsGxWcEUEbkU5zL/y3zptMmhwYRlPljV56w9jnMy6Xm6eHW9ihz03kcpnHD\nuloUpcpGngqJ9KEvlQZp3mk5VxLh53S3cU/ziPETEVEw9z3xI+QT/5szliY+AQv6\n/XMx6eNAdvvfZoJp1+pZ3ixTtYcuVTA57i6cuI6gwchhhBsUkqCPgR8ZTNTu0FiZ\nLzjXIKsy+vXWMP0bgMiTMUWmBYRaPFOk3X8RoCZJxsV7sq4r2yx+DHc32r3TmJ8i\niQlFWjnnS1JcEKgLvlWjAT5+eijVBdNPwQlFfEx+cQKBgQD9EK1E2A4GxJuYnmQC\nKNobjSdRbFRYWNukiDBNYNWEQrgAkgsfryN/+0+TFsJSG1WDqaIy4a7DsfRyQVzK\ntKEt4vlHRiIIT7qADl+vSBsH1ZJzN/f8M4Zg+l3iukP3uTvEFZ6Jwl+W+WvELSyS\n12lcDsOttWqSNc/RKwt7a6sNuQKBgQDoOSUfkMl6xLx+/IaQDVzK40WWBBWaTklm\nyIkHxjJQ7ZiWLOsnbQvsHGhxDZ7eGvoAf2i/L2ya81wf7XgMp3qU1cmDv5AViyp0\nRsy4dUIog+e7deZRHcB6sGBlzmu8ci5Z2IUfTS4WqBn6CyzxSSvSH3+/BX38rilP\n38ROHAMTmQKBgG2XNEH1ApYBvJQqO4sH3/RAe39yV1BvIqcs5yYLQkvljMOKe1C8\nSrZYwcwj9gESn0TGSFyaiVFsFj0Ie0O5V3eErIkmIQTSaiSclOlWY4ZQAfzthvHr\n6kzC/7d5DIgR6oTvC9oCl9zMpNOu8Hei25inOCxYvQ8WSKn/ZxiKtufZAoGBAKJj\n267wK8SbMQlIA71Was5CEdYu8wBdwHyMvS5fja4ECFD0Blkiq1SoJOzxzmeYy7xv\nXEtdmX/dsE1vXSTUNSdBPNLRsasvDzgSjnRrIyF75B+1+aI9wOzKzA5FRBeabQlN\nHQJfkVwsn0W4bOwp8+fTORzWdVyuWZtOalMIyan5AoGAITEIcFiDOqk5cqMZoAl1\naFEeyL9qoX9nzu9mdVOutsx2taCT4h2WPXABNwm6uJa64jU0VA1igwXw7/Qc2a1q\n3jBJjBsQ7akELYVgiwUSGOaJiWJXz1URG27PUFhguz8PQeVhl/EdzDF1XKzNz6sm\nELcUtR/TrSRfzblrNvnNIoc=\n-----END PRIVATE KEY-----\n",
#         "client_email": "firebase-adminsdk-3e883@comp7510-6c8da.iam.gserviceaccount.com",
#         "client_id": "108067384295080648816",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-3e883%40comp7510-6c8da.iam.gserviceaccount.com"
#     }
# }

# myfirebase = Firebase(config)
# db = myfirebase.database()

# y = 12

# result = db.child('/Userlist').get().val()
# x = json.dumps(result)
# y = json.loads(x)
# print(type(y))
# print(type(result))
# y.items()
# def b(a):
#     x = a + 1
#     return x
# c = b(5)
# print(b(5))

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()
