from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ObjectProperty, StringProperty
from kivy.core.window import Window
from datetime import datetime, timedelta
from kivy.uix.label import Label
from game import TicTacToe
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class Board(Widget):
    letter = "X"
    game = TicTacToe()
    o_player = GeniusComputerPlayer('O')

    def build(self):
        pass

    def presser(self, btn, key):
        self.game.make_move(key - 1, self.letter)
        self.setmove(btn)
        if self.game.current_winner:
            self.parent.set_winner('human wins!')
            return

        if self.game.empty_squares() == False:
            self.parent.set_winner('ties!')
            return

        self.computer_move()
        # self.game.print_board()

    def setmove(self, btn):
        btn.text = self.letter
        btn.disabled = True
        # self.game.print_board()
        # btn.background_color = (0, 0, 0, 1)
        # switches player
        if self.letter == 'X':
            btn.disabled_color = (1, 0, 0, 1)
            btn.color = (1, 0, 0, 1)
            self.letter = 'O'
        else:
            btn.disabled_color = (0, 0, 1, 1)
            btn.color = (0, 0, 1, 1)
            self.letter = 'X'

    def computer_move(self):
        square = self.o_player.get_move(self.game)
        self.game.make_move(square, self.letter)
        btnid = "btn{}".format(square+1)
        btn = self.parent.ids[btnid]
        if self.game.current_winner:
            self.parent.set_winner('computer wins!')
        self.setmove(btn)

        if self.game.empty_squares() == False:
            self.parent.set_winner('ties!')
            return

    def reset(self):
        self.game = TicTacToe()
        computer_letter = 'O' if self.letter == 'X' else 'X'
        self.o_player = GeniusComputerPlayer(computer_letter)
        # pass

class GameBoard(Widget):
    mxboard = ObjectProperty(None)
    now = ObjectProperty(None)
    clocklabel = StringProperty()
    messresult = StringProperty()
    x_player = HumanPlayer('X')

    def build(self):
        self.now = datetime.now()
        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1.0)

    def update_clock(self, dt):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds = 1)
        self.clocklabel = self.now.strftime('%H:%M:%S')

    def reset(self):
        for x in range(9):
            btnid = "btn{}".format(x+1)
            btn = self.ids[btnid]
            btn.text = ''
            btn.disabled = False
        self.mxboard.reset()

    def set_winner(self, text):
        self.messresult = text
        for x in range(9):
            btnid = "btn{}".format(x+1)
            btn = self.ids[btnid]
            btn.disabled = True


class TictactoeApp(App):
    def build(self):
        Window.size = (400, 300)
        board = GameBoard()
        board.build()
        return board

TictactoeApp().run()