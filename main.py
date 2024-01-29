import arcade
import random


SCRN_W = 800
SCRN_H = 600


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCRN_W, SCRN_H, "TP 4")

        self.circles = []
        self.rectangles = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
        for circls in self.circles:
            circls.draw()

        for rects in self.rectangles:
            rects.draw()

    def on_mouse_press(self, x, y, button, modifiers: None):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = Balle()
            ball.x = x
            ball.y = y
            ball.draw()

            self.circles.append(ball)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rect = Rectangle()
            rect.x = x
            rect.y = y
            rect.draw()

            self.rectangles.append(rect)

#######################

class Balle:
    def __init__(self):
        self.x = None
        self.y = None
        self.changex = None
        self.changey = None

        self.rayon = random.randint(10, 30)
        self.color = arcade.color

    def update(self):
        self.x += self.changex
        self.y += self.changey

        if self.x > SCRN_W - self.rayon:
            self.x = SCRN_W - self.rayon
            self.changex = 0

        if self.x < self.rayon:
            self.x = self.rayon
            self.changey = 0

        if self.y > SCRN_H - self.rayon:
            self.y = SCRN_H - self.rayon
            self.changey = 0

        if self.y < self.rayon:
            self.y = self.rayon
            self.changey = 0

        arcade.finish_render()

    def draw(self):

        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color.WHITE)


class Rectangle:
    def __init__(self):
        self.x = None
        self.y = None
        self.changex = None
        self.changey = None

        self.width = random.randint(10,30)
        self.height = random.randint(10,30)
        self.angle = random.randint(0, 359)

        self.color = arcade.color

    def update(self):
        if self.x > SCRN_W - self.width:
            self.x = SCRN_W - self.width
            self.changex = 0

        if self.x < self.width:
            self.x = self.width
            self.changey = 0

        if self.y > SCRN_H - self.height:
            self.y = SCRN_H - self.height
            self.changey = 0

        if self.y < self.height:
            self.y = self.height
            self.changey = 0

        arcade.finish_render()

    def draw(self):

        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color.WHITE, self.angle)

#######################

def main():
    my_game = MyGame()
    my_game.setup()    
    
    arcade.run()

main()

#######################
