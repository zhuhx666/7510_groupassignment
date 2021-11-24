
# 1. 您需要使用 Python 和 Kivy 和 KivyMD 框架来完成应用程序。
# 2. 应用中显示的核心数据必须从Firebase实时数据库下载和存储。
# 3. 应用首页必须是要求输入用户名和密码的登录页面。用户ID 和密码应提前存储在 Firebase 实时数据库中。
# 4. 登录后，出现功能选择页面。
# 5. 应用程序应有不同的页面，包括撰写页面、列表页面、修改页面等。页面应该安排得很好。
# 6. 您的应用程序应提供信息共享功能、查询功能等。例如，照片分享、问题问答、论坛（论坛）等。
# 7. 每个页面（显示在登录页面之后）必须显示登录名。
# 8. 如果您的群组有 4 名成员，则该应用程序应至少有 6 个页面，包括登录页面。
# 9. 代码文件必须在项目文件夹中组织良好，作为一个完整的可移动的应用。
# 10.根据难度等级、完成程度、实用性打分个别页面。因此，成员可能有不同的分数

#注意：这个页面是是功能选择页面，照片，论坛，查询，所以我只做了论坛的按钮作为测试
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mandel_lib import *
from forums_21461295 import *
#from post import *




class function(Screen):
    def clickme(self):
        MDApp.get_running_app().switchTo('forums')#屏幕切换到home的函数





class MyApp(MDApp):
    def build(self):
        Builder.load_file('function_21461295.kv')
        Builder.load_file('forums_21461295.kv')
        Builder.load_file('post_21461295.kv')
        #加载三个页面的文件
        
        manager = self.manager = ScreenManager()
        manager.add_widget(function())
        manager.add_widget(forums())
        manager.add_widget(post())
        #加载screenmanager和3个widget用于屏幕切换
        
        return manager
        #应该是显示屏幕
        
    def switchTo(self, screen_name):
        self.manager.current = screen_name
    #用屏幕名来定义屏幕切换函数


if __name__ == '__main__':
    MyApp().run()
    #App启动