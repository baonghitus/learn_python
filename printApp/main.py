from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.core.window import Window
from datetime import datetime
from datetime import timedelta
from kivy.uix.label import Label

class ClockTime():
    pass
class MainBoard(Widget):
    now = StringProperty('')

    def build(self):
        self.now = datetime.now()

        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1)
        self.my_label = Label(text= self.now.strftime('%H:%M:%S'))
        return self.my_label  # The label is the only widget in the interface

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds = 1)
        self.my_label.text = self.now.strftime('%H:%M:%S')


class PrinterApp(App):
    def build(self):
        Window.size = (400, 600)
        board = MainBoard()
        return board

PrinterApp().run()