# import kivy module
#import kivy
from kivy.uix.boxlayout import BoxLayout

#kivy.require("1.9.1")
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# class in which we are creating the button
#class Requirement_Analysis_Tool(App):

    #def build(self):
    '''button1 = Button(text="Test Pre-Processing",  font_size="19sp",size=(10, 10),size_hint=(.24, .065),pos=(400, 400))
        button2 = Button(text="Extract Nouns",  font_size="19sp",size=(10, 10),size_hint=(.24, .065),pos=(300, 300))
        button3 = Button(text="Fetch Synonyms",  font_size="19sp",size=(10, 10),size_hint=(.24, .065),pos=(200, 200))
        button4 = Button(text="Validate Ambiguities",  font_size="19sp", size=(10, 10),size_hint=(.24, .065),pos=(-100, -100))
        boxlayout =BoxLayout(orientation='vertical',spacing=10)
        boxlayout.add_widget(button1)
        boxlayout.add_widget(button2)
        boxlayout.add_widget(button3)
        boxlayout.add_widget(button4)
        
     return boxlayout'''


# creating the object root for ButtonApp() class
#root = Requirement_Analysis_Tool()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
#root.run()