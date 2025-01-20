from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
    #def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        #self.textinput = TextInput(multiline= False,hint_text='insert text',size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y":0.7})
        #btn = Button(text='Submit',size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y":0.6})
        #self.label = Label(text="Nothing",size_hint=(0.5,0.1), pos_hint={"center_x":0.5,"center_y":0.5})
        #self.textinput.bind(on_text_validate = self.displayData)
        #btn.bind(on_press=self.displayData)
        #self.add_widget(self.textinput)
        #self.add_widget(btn)
        #self.add_widget(self.label)
    def displayData(self):
        data = self.ids.textinput.text
        self.ids.label.text = data
        #self.label.text = self.textinput.text



class FirstApp(App):
    #def build(self):
        #return Interface()
        pass

FirstApp().run()