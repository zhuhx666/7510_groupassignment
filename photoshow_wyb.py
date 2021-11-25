from kivy.lang import Builder
from kivy.core.window import Window
from mandel_lib import *
from firebase import Firebase
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
# import sharing_page 
# import homepage

config = {
    'apiKey': '',
 'authDomain':'lab-exercise2.firebaseapp.com',
 'databaseURL': 'https://lab-exercise2-default-rtdb.firebaseio.com/',
 'storageBucket':'lab-exercise2.appspot.com',
 'serviceAccount':{
  "type": "service_account",
  "project_id": "lab-exercise2",
  "private_key_id": "e350b1aff9a3938f79506c63a27a03490f496d71",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDbQ7+c/U3IQCGi\nwDwDNsXKzF63QLExZDrI6BCicNGneNMjZjzBgPGzP4sEaX8XRStO/uqqui+7fYqx\n105ImFWAeZ11OHbhjCJ51EFqD1Hx+Hf19fxXG29Ayt/t977RCjnqhUstYVHD81zr\n/5pwIRPtwDKV7rUhMgLhdcjBN5Y839qXwDHMxuWfB+PZe/iccdPbrUdZUORxupkf\nhuu2D1rUY/BlddgYDhMGS35aFxCgzre52Y8dskiAyhUIf+P/QKaoM1fM5jnvyMb7\nEck2uSz0JRD6yIiM6kkfzOme671t6COLDysPAzGkAkkbGRH/Cbj2XzvOe2dbzq9l\nOToR6QA5AgMBAAECggEAIZFfaCgibJYe4CT4exB7WvcLSBhUGEjtM/1NMKU/f5lg\nj6KTChfUyPmhLYl+HsCk5vjhUcZj0NshLOVWs4f4zQyxVbURhCm5THf5lMRoKfh9\nWw8v9OD7GQsGGc8sLCIZ6ETEU9v6kdpz3yB4UxLJU4RxaiFLoxueM8idtbDuI/7j\n01yuuf+yu0wBsDUX+iF7EqXunglm1cg5ZaB3f0TBMR9/jejNMXhVEMoz+Senj9yI\n0D5w5Yrv1jxts5XiN60oPIIW+PhaUByWwx64PuOoVnpzBd25LdcZLvazXDhzMF5W\nZpKQxOh3lXBdfBsymDBlr2jso55v/8P4nxvK57/NdQKBgQDu5iO/WBzlTC6DnzHY\nph72ko/t7gPL43OIv1ICdtuhMhUEsdhghaNHR99SHt2+OSRNVYetxIh5YL4FEeXc\nsniWevDTdZlqV3j48UvjmaLPs+N8SwJEPSQuhd3fZPLNPVHYRhLXDx1XCyD9xSba\nkSKLKcxDD1WywpHyyTiwxeODFQKBgQDq9c565YhFTdKsEorgrCiX5NIfssGBeCxv\nMAS1toewrmqwfvzFHKn++0aWrylbS+v/c2LtXCcgbmQaoNYvf15WQ0IifSS7bRdw\nTYqxQpZppdzsZ/Stgk5Q5V9OBbJaVMRUSpfuFHhF2kHw99dyLKrYWpAtL4OcavQZ\nFKcZVDghlQKBgQDszY7toieyWltY+LnuKGxUuV6V1/JHbgQdrpdZ/fsiw4P2DVuQ\nAaehhmqk+heO8RE83uUIp+Enf2+bkuwoYXgKoX6J/O2/bUlqabRxvN6Xx5Zco/Vx\nMrHks6kEQQozyu6P1JXkOwU4PL3NDlm/GVIGY74nUtH9ycPlxvO8tcsZKQKBgQDq\nGnPae2xlMP8hN3BsHtxrSzAZKTAoYaZUOlHXA8D6xy3CISSU+NRgG9jfNjNMpb7E\nTSFaQiEx7QuMhIgj1xIVfPoeBvZcUHu0B26S4zeemAYg/gsJ/fUuIPvubzqfSio7\nmf761iZn4ukkwKxHND4dR06z1s2ZQe9oNe2wDPvIaQKBgQC7gaFMMv1qMvBFp1iu\nv3RsGXY9+gFsPNrsgfsycqr9G7uRN9eeLJyqyl01sC0uxHF1NsaKdJvDZNS8Ach9\nyWGRbLEDrXQlsIZPWebBcTBh5XecsrlhFqI8I1sKYpVqfFmPyfEHrWB62gl/tysq\nChQepiaRdxrlxZ8kuceIENYPZg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-nj5mn@lab-exercise2.iam.gserviceaccount.com",
  "client_id": "101147277452233465410",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-nj5mn%40lab-exercise2.iam.gserviceaccount.com"
    }
}

myfirebase = Firebase(config)
db = myfirebase.database()
storage = myfirebase.storage()



class showscreen(Screen):
    def on_enter(self):
    # def showscreen(self):
        response = db.child('/Images/img_urls').get().val()
        print(sharing_page.imgname)
        # self.imgu = sharing_page.imgname.decode("utf-8")
        # self.ids.img.source = self.imgu
        app = MDApp.get_running_app()
        self.ids.img.source = response #app.imgname
        self.ids.img.reload()
    
    def to_home(self):
        MDApp.get_running_app().switchTo('home')
        
class photoshow(MDApp):
    
    def switchTo(self, screen_name):
        self.manager.current = screen_name
    
    def build(self):
        Builder.load_file('homepage.kv')
        self.manager = manager = ScreenManager()
        manager.add_widget(homepage.home())
        return manager


if __name__ == "__main__":
    photoshow().run()