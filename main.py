import arcade
import random


SCRN_W = 800 # largeur de l'ecran de jeu
SCRN_H = 600 # hauteur de l'ecran de jeu


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCRN_W, SCRN_H, "TP 4")

        self.circles = [] # groupe des cercles
        self.rectangles = [] # groupe des rectangles

    def setup(self):
        pass

    def on_draw(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
        for circls in self.circles: # pour chaque cercles dans le groupe
            circls.draw() # dessiner le cercle sur l'ecran

        for rects in self.rectangles: # pour chaque rectangle dans le groupe
            rects.draw() # dessiner le rectangle sur l'ecran

    def on_mouse_press(self, x, y, button, modifiers: None): # quand un bouton de la souris est appuyer
        if button == arcade.MOUSE_BUTTON_LEFT: # si c'est un clique gauche
            ball = Balle()
            ball.x = x 
            ball.y = y
            ball.draw()

            self.circles.append(ball) # ajouter la balle au groupe

        elif button == arcade.MOUSE_BUTTON_RIGHT: # si c'est un clique droit
            rect = Rectangle()
            rect.x = x
            rect.y = y
            rect.draw()

            self.rectangles.append(rect) # ajouter le rectangle au groupe

#######################

class Balle:
    def __init__(self):
        self.x = None # les positions de la balle sont definis par la souris
        self.y = None
        self.changex = 5 # vitesse du cercle en x
        self.changey = 5 # vitesse du cercle en y

        self.rayon = random.randint(10, 30) # generer un rayon au hasard entre 10 et 30
        self.color = arcade.color # cherche les couleurs dans la librairie arcade

    def update(self):
        self.x += self.changex
        self.y += self.changey

        if self.x > SCRN_W - self.rayon: # si la position en x va plus loin que la bordure de l'ecran
            self.x = SCRN_W - self.rayon
            self.changex * -1 # changer la direction pour l'opposer

        if self.x < self.rayon: # si la position en x va plus loin que la bordure de l'ecran
            self.x = self.rayon
            self.changey * -1

        if self.y > SCRN_H - self.rayon: # si la position en y va plus loin que la bordure de l'ecran
            self.y = SCRN_H - self.rayon
            self.changey * -1

        if self.y < self.rayon: # si la position en y va plus loin que la bordure de l'ecran
            self.y = self.rayon
            self.changey * -1

        arcade.finish_render() # afficher l'ecran apres avoir mis a jour

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, (random.randint(0,255), random.randint(0, 255), random.randint(0, 255))) # dessiner un cercle sur l'ecran


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
