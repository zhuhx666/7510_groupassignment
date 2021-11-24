#这是我论坛的主页
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from requests.sessions import ContentDecodingError
from function_21461295 import MyApp
from firebase import Firebase
from mandel_lib import *
from datetime import datetime
from kivy.clock import Clock, ClockBase




# config = {
#     'apiKey': '',
#     'authDomain':'comp7510-a0002.firebaseapp.com',
#     'databaseURL': 'https://comp7510-a0002-default-rtdb.firebaseio.com/UserAccount',
#     'storageBucket':'comp7510-a0002.appspot.com',
#     'serviceAccount': {
#         "type": "service_account",
#         "project_id": "comp7510-a0002",
#         "private_key_id": "30972a5845108e9c9d82fabe034222e0ad7429d8",
#         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCVXIG7ZIKy/KY5\ny+sfnktEcdfeqBoYtYOp0f55jlyvIF+S/A3WkeV3cDymbpOWZ8j56vgwW4NQrhwg\nUnW1Z3p1r7fXcWvLhlVOzzbnBikcJBz7eh+9Z5yi967+MP3RMcmM80/ok2wLhyFs\np5qXi2T0QQz6Z81a8NNWrxvsiYtNfwWWhTceTcVizg1g9HGkFy8UxqGsvzXvChAP\nj2vkRtmfeEozqjH9yLXl4K4CTE1k/Rmx9ELzngHn5bFGaKCGQ6emh+k4prQ2ZDA4\nurJBHPbPivbtJHwgxNsEtCKRKaoYqiOIsSgLrVbiui4ugw+VkFYZ4nY7hwyomwZM\n6+KvThsnAgMBAAECggEAP4eC6NWGICKFg5TgU+kNA7ZWhu7CdtsR/xQCZOqwMo8X\nB9ps+mTBEQ3sxi/HV9SaL+8JFOx/zLvZ28enKHs0o8UTcbBdFMr1ExnhNN+ycbVM\nnIxj3rio78phJN5qv2WpYGoHhZna/YZDKceaYjYYwSnAHuwy9Sj1A2xk+LXCSjoD\n3cou7/DdwZ+rFlE4wRlKtZCENelnRdZ0W98CN2fMw++LwIkHjOaNy+hWtgG7UzGi\nTkOY7pBYYWIO/sc2z1cHG60tjS5mZ3/qgdawSC+EH9usgfoqwL9EEmWKt36skwSN\nTzCV3qi86ldJ2Z5hlPAJ6WmNuZGRLgUUokXBXYOvlQKBgQDPoU/R09mGCqJ+/LWa\nCImwIAm1dNBt4N449EN3z7XeZUP8aIIVxUu+uQO6XN35nqIlcvHV4VSra6P0vhfI\nxvVfstDd92LbABS4xmmeaLuR/bw7nm7Km74rUuoKpbpSiuFE9XiUZmylyAxobwOd\nJBxzmasoeg81ewt+hEek5/fITQKBgQC4KCZqPDBkVPKGB6vIeXxCiIGPuJOsRu3Q\n/xlxPInHnz2M1ZPcmMAqVoO1R/ubKjlF3M8kfJSgUfY73amaMpvIX/hBWSJG1ruY\nZl8b7ZQI0Yis0/aoIU4JO+bkd7sIikoB67+H0bug7Smc302txFNAfLjR8KkScIVq\n8Ze5Ae7rQwKBgGfMMfYo3XboPCIVvce6evLkoVXohwZXQ2DfpBbybO44W8uEh3vQ\nvTQklBuHr6TJzC/Cjempk0V7M2T33zYNWL+1yjsdIHtxR+qzrjt2CkdKvN5lLuf1\nAhXwhnY6MbJwIXvy54vwxGIAZ0uSLBFT6zFTYkCC/LV0xONDx/lFyhaFAoGAQHdd\nq0bSsezC0YSR8CYHB8t9f3Bf0akqy0TiBS/qE4V9KHYDwu9+JdQPW0CNpa3MStaX\ndPBfnxfSGPbpzl71BdoCr+2iACZfmWQM21v5vHSNYeL5r7Wo+baMh2IaiUzPx4hd\njhAvnJApRw8sxC277xE6KdQTe68EJYHZWRyCJL0CgYBlfTweihJw4y1eWa9ny+8n\nv9OPTRpCoPeayZBsgzzzf5TKpjU6qZRtulOk+zty9tPsfsRj5dwQcnQF2Uzqwvhz\nTbVA8Uh4bguVacjSqMlCCIbWp3norL1mUE6iifzJgfAyglbv/b4JjRfU2ZvgevD8\nLNUb3mdoVnVp55syP/y/HA==\n-----END PRIVATE KEY-----\n",
#         "client_email": "firebase-adminsdk-rqtso@comp7510-a0002.iam.gserviceaccount.com",
#         "client_id": "100279388816701333086",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rqtso%40comp7510-a0002.iam.gserviceaccount.com"
#     }

# }#我的数据库配置，你应该用你的替换掉

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




number=1
def uploaddata(un, tp, rp,t):  
    global number#计数器，表示整个论坛里有多少帖子和回复    
    data = dict(username=un,topic=tp, reply=rp,time=t)
    db.child('/Forum/'+str(number) ).set(data)
    number+=1

    
uploaddata('Denny','What are the fun attractions in Hong Kong?','I think Climbing Lion Rock is a great experience','2021-11-14 17:43')
uploaddata('harryzhu','','Hong Kong Ocean Park','2021-11-14 17:45')

uploaddata('zhang','','hk','2021-11-24 1:45')

class forums(Screen):
    global user
    user = 'cbo'
    showname=user#要求里有每个页面显示用户名，所以cbo是我手动输入的。最终，应该是用登录界面的登录名替换cbo。
    content1='Topic:'+db.child('Forum/1/topic/').get().val()+'\n'+'Content:'+db.child('Forum/1/reply/').get().val()+'\t\t'+'User:'+db.child('Forum/1/username/').get().val()+'\t\t'+'Time:'+db.child('Forum/1/time/').get().val()+'\n'+'Reply:'+db.child('Forum/2/reply/').get().val()+'\t\t'+'User:'+db.child('Forum/2/username/').get().val()+'\t\t'+'Time:'+db.child('Forum/2/time/').get().val()+'\n'
    
    #这里假设发帖和回帖上传和下载数据库时，只有一位用户操作
    def personal(self):
        MDApp.get_running_app().switchTo('PersonalScreen')#屏幕切换到function页面的函数
    def Quit(self):
        MyApp().stop()#App退出函数
    def Post(self):
        MDApp.get_running_app().switchTo('post')#屏幕切换到post页面函数
        
        global event
        event=Clock.schedule_interval(lambda x: self.refresh(), 10)
        

    def Replying1(self):
        reply1=self.ids.id_reply1.text#使用变量reply1接收回复框内容
        t1=datetime.now().strftime('%Y-%m-%d %H:%M:%S')#使用t接收当时时间
        uploaddata(user,'',reply1,t1)#上传用户名，空，回复，时间到数据库（PS：因为是跟帖，所以我设置topic为空）
        number1=number-1
        self.ids.id_text1.text=self.ids.id_text1.text+'Reply:'+db.child('/Forum/'+str(number1)+'/reply/' ).get().val()+'\t\t'+'User:'+db.child('/Forum/'+str(number1)+'/username/').get().val()+'\t\t'+'Time:'+db.child('/Forum/'+str(number1)+'/time/').get().val()+'\n'
        #将第一个显示框导入回复内容
        self.ids.id_reply1.text=''#清空回复框
    def refresh(self):
        number2=number-1
        #本该做个循环，但无法用变量表示各个文本框，只能这样
        if(self.ids.id_text2.text==''):
            self.ids.id_text2.text='Topic:'+db.child('Forum/'+str(number2)+'/topic/').get().val()+'\n'+'Content:'+db.child('Forum/'+str(number2)+'/reply/').get().val()+'\t\t'+'User:'+db.child('Forum/'+str(number2)+'/username/').get().val()+'\t\t'+'Time:'+db.child('Forum/'+str(number2)+'/time/').get().val()+'\n'
            event.cancel()
            
        elif(self.ids.id_text3.text==''):
            self.ids.id_text3.text='Topic:'+db.child('Forum/'+str(number2)+'/topic/').get().val()+'\n'+'Content:'+db.child('Forum/'+str(number2)+'/reply/').get().val()+'\t\t'+'User:'+db.child('Forum/'+str(number2)+'/username/').get().val()+'\t\t'+'Time:'+db.child('Forum/'+str(number2)+'/time/').get().val()+'\n'
            event.cancel()
        else:
            forums.show_dialog1(self)
            event.cancel()
    def Refresh(self):
        content2=db.child('UserAccount/Forum/')
        print(content2)
    
    def show_dialog1(self):
        dialog = MDDialog(
            title = 'Warning',
            text = 'The forum is full and users are unable to post new posts',

        )
        dialog.open()
    def Replying2(self):
        if self.ids.id_text2.text=='':
            self.ids.id_reply2.text=''
            return
        else:
            reply2=self.ids.id_reply2.text
            t21=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            uploaddata(user,'',reply2,t21)
            number21=number-1
            self.ids.id_text2.text=self.ids.id_text2.text+'Reply:'+db.child('/Forum/'+str(number21)+'/reply/' ).get().val()+'\t\t'+'User:'+db.child('/Forum/'+str(number21)+'/username/').get().val()+'\t\t'+'Time:'+db.child('/Forum/'+str(number21)+'/time/').get().val()+'\n'
            self.ids.id_reply2.text=''
    def Replying3(self):
        if self.ids.id_text3.text=='':
            self.ids.id_reply3.text=''
            return
        else:
            reply3=self.ids.id_reply3.text
            t31=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            uploaddata(user,'',reply3,t31)
            number31=number-1
            self.ids.id_text3.text=self.ids.id_text3.text+'Reply:'+db.child('/Forum/'+str(number31)+'/reply/' ).get().val()+'\t\t'+'User:'+db.child('/Forum/'+str(number31)+'/username/').get().val()+'\t\t'+'Time:'+db.child('/Forum/'+str(number31)+'/time/').get().val()+'\n'
            self.ids.id_reply3.text=''

    def Clear1(self):
        self.ids.id_reply1.text=''
    def Clear2(self):
        self.ids.id_reply2.text=''
    def Clear3(self):
        self.ids.id_reply3.text=''
        
        
    
    

class post(Screen):
    def Posting(self):
        
        newtopic=self.ids.txt_newtopic.text
        newcontent=self.ids.txt_newcontent.text
        lennewtopic= newtopic.strip()
        t2=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if len(lennewtopic)==0:
            post.show_dialog2(self)
            self.ids.txt_newcontent.text=''
        else:
            uploaddata(user,newtopic,newcontent,t2)
            MDApp.get_running_app().switchTo('forums')#切换到forums页面
        
        
    def Clear(self):
        self.ids.txt_newtopic.text=''
        self.ids.txt_newcontent.text=''
        MDApp.get_running_app().switchTo('forums')
        #清除topic和content文本框中内容，并切换到forums页面
    username=user#这里同样是用户名的显示，手动输入的，应该由登录界面的用户名替换
    def show_dialog2(self):
        dialog = MDDialog(
            title = 'Warning',
            text = 'The topic can not be blank',

        )
        dialog.open()


    

    
    




    




