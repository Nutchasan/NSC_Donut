from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("test.kv")

# Declare both screens
class MenuScreen(Screen):
    pass

class BeginScreen(Screen):
    pass

class HelpScreen(Screen):   
    pass    

class Lesson_1(Screen):
    pass
            
# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(BeginScreen(name='begin'))
sm.add_widget(HelpScreen(name='help'))
sm.add_widget(Lesson_1(name='lesson_1'))

class TestApp(App):
    title = 'Python Coding Game Lesson'

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()