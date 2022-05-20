from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from random import randint
from kivy.core.window import Window

class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.2

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def reset(self, dx, dy):
        self.x = dx / 2
        self.y = dy / 2
        self.velocity = Vector(4, 0).rotate(randint(0, 360))
        self.move()

# Update

# on_touch_down()
# on_touch_up()
# on_touch_move()

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        if (self.ball.y < 0) or (self.ball.y > self.height - self.ball.height):
            self.ball.velocity_y *= -1

        if self.ball.x < 0:
            self.ball.velocity_x *= -1
            self.player1.score += 1
            self.ball.reset(self.width, self.height)

        if self.ball.x > self.width - self.ball.width:
            self.ball.velocity_x *= -1
            self.player2.score += 1
            self.ball.reset(self.width, self.height)


        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 1/4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y


    def key_action(self, win, keyboard, keycode, text, modifiers):
        if (keycode == 82) and (self.player2.center_y < self.height):
            self.player2.center_y += 20
        elif keycode == 81 and (self.player2.center_y > 0):
            self.player2.center_y -= 20
        elif keycode == 26 and (self.player1.center_y < self.height):
            self.player1.center_y += 20
        elif keycode == 22 and (self.player1.center_y > 0):
            self.player1.center_y -= 20
        return True
        # print ("got a key keycode: %s" % keycode)
        # print ("got a key text: %s" % text)
        # print ("got a key keyboard: %s" % keyboard)

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Window.bind(on_key_down=game.key_action)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

PongApp().run()