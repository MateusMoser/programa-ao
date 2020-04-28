import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols= 6
        self.add_widget(Label(text='Name: '))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='year: '))
        self.year = TextInput(multiline=False)
        self.add_widget(self.year)

        self.add_widget(Label(text='emil: '))
        self.emil = TextInput(multiline=False)
        self.add_widget(self.emil)


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()