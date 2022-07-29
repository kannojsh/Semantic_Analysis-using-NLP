from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
#from button import Requirement_Analysis_Tool
#import button

#class MyGrid(GridLayout):
class MyGrid(Screen):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

    def drop(self):
        self.docTypes = ["Csv", "Doc", "Excel", "Pdf"]
        self.dropdown = DropDown()
        self.dropdownBtnText = 'Select Document Type'
        self.rows = 2
        for index in range(len(self.docTypes)):
            button = Button(text=self.docTypes[index], size_hint=(None, None))
            button.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(button)
        self.mainButton = Button(text='Select Document Type', size_hint_y=0.10, size_hint_x=0.25, pos_hint={'x':0.7,'y':0.80},height=30)
        self.mainButton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainButton, 'text', x))
        #return self.mainButton
        runTouchApp(self.mainButton)

#    def build(self):
class button2(Screen):
    def box_layout(self):
        self.button1 = Button(text="Test Pre-Processing",  font_size="19sp",size=(10, 10),size_hint=(.24, .065),pos=(400, 400))
        self.button2 = Button(text="Extract Nouns",  font_size="19sp",size=(10, 10),size_hint=(.24, .065),pos=(300, 300))
        self.button3 = Button(text="Fetch Synonyms",  font_size="19sp",size=(10, 10),size_hint=(.24, .065),pos=(200, 200))
        self.button4 = Button(text="Validate Ambiguities",  font_size="19sp", size=(10, 10),size_hint=(.24, .065),pos=(-100, -100))
        self.boxlayout =BoxLayout(orientation='vertical',spacing=10)
        self.boxlayout.add_widget(self.button1)
        self.boxlayout.add_widget(self.button2)
        self.boxlayout.add_widget(self.button3)
        self.boxlayout.add_widget(self.button4)
        #self.dropdown.add_widget(self.boxlayout)
        #return self.boxlayout
        #self.mainButton.bind(self.boxlayout)
        #self.dash = keybinding.start(self.mainButton, self.boxlayout)
        runTouchApp(self.boxlayout)


class Requirement_Analysis_Tool(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyGrid(name='start'))
        sm.add_widget(button2(name='Step2'))
        return sm
        #runTouchApp(sm)
        #return MyGrid()

#root = Requirement_Analysis_Tool()

if __name__ == "__main__":
    #MyGrid.run()
#    Requirement_Analysis_Tool.run(MyGrid)
    Requirement_Analysis_Tool().run()
    #root.run()
