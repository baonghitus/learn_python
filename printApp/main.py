from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.core.window import Window
from datetime import datetime, timedelta
from kivy.uix.label import Label

class ClockTime():
    pass
class MainBoard(Widget):
    now = ObjectProperty()
    clocklabel = StringProperty()

    def build(self):
        self.now = datetime.now()
        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1.0)

    def update_clock(self, dt):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds = 1)
        self.clocklabel = self.now.strftime('%H:%M:%S')


class PrinterApp(App):
    def build(self):
        Window.size = (800, 600)
        board = MainBoard()
        board.build()
        return board

PrinterApp().run()