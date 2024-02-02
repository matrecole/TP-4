import arcade
import random


SCRN_W = 800 # largeur de l'ecran de jeu
SCRN_H = 600 # hauteur de l'ecran de jeu

COLORS = [arcade.color.BLUE, arcade.color.RED, arcade.color.WHITE, arcade.color.BLUE_VIOLET, arcade.color.CANDY_APPLE_RED, arcade.color.PERSIAN_ROSE, arcade.color.BOYSENBERRY, arcade.color.CHESTNUT, arcade.color.YELLOW_ORANGE] # tuple pour les couleurs


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

    def on_update(self, delta_time: float):
        for circls in self.circles: # pour chaque cercles dans le groupe
            circls.update() # mettre a jour la position du cercle sur l'ecran

        for rects in self.rectangles: # pour chaque rectangle dans le groupe
            rects.update() # mettre a jour la position du rectangle sur l'ecran

#######################

class Balle:
    def __init__(self):
        self.x = None # les positions de la balle sont definis par la souris
        self.y = None
        self.changex = random.randint(1,5) # vitesse du cercle en x aléatoire entre 1 et 5
        self.changey = random.randint(1,5) # vitesse du cercle en y aléatoire entre 1 et 5

        self.rayon = random.randint(10, 30) # generer un rayon au hasard entre 10 et 30
        self.color = random.choice(COLORS) # définir une couleur au hasard dans le tuple

    def update(self):
        self.x += self.changex
        self.y += self.changey

        if self.x > SCRN_W - self.rayon: # si le cercle va plus loin que la bordure droite de l'ecran
            self.x = SCRN_W - self.rayon # empèche le cercle de sortir
            self.changex *= -1 # changer la direction pour l'opposé

        if self.x < self.rayon: # si le cercle va plus loin que la bordure gauche de l'ecran
            self.x = self.rayon
            self.changex *= -1

        if self.y > SCRN_H - self.rayon: # si le cercle va plus loin que la bordure en haut de l'ecran
            self.y = SCRN_H - self.rayon
            self.changey *= -1

        if self.y < self.rayon: # si le cercle va plus loin que la bordure en bas de l'ecran
            self.y = self.rayon
            self.changey *= -1

        arcade.finish_render() # afficher l'ecran apres avoir mis a jour

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color) # dessiner un cercle sur l'ecran


class Rectangle:
    def __init__(self):
        self.x = None
        self.y = None
        self.changex = random.randint(-5,5) # vitesse du rectangle en x aléatoire entre 1 et 5
        self.changey = random.randint(-5,5) # vitesse du rectangle en y aléatoire entre 1 et 5

        self.width = random.randint(10,30) # définir une largeur entre 10 et 30
        self.height = random.randint(10,30) # définir une hauteur entre 10 et 30
        self.angle = random.randint(0, 359) # définir l'angle du rectangle entre 0 et 359° (360 et 0 c'est la meme chose)

        self.color = random.choice(COLORS) # définir une couleur au hasard dans le tuple

    def update(self):
        self.x += self.changex
        self.y += self.changey

        if self.x > SCRN_W - self.width: # si le rectangle va plus loin que la bordure droite de l'ecran
            self.x = SCRN_W - self.width # empèche le rectangle de sortir
            self.changex *= -1 # changer la direction pour l'opposé

        if self.x < self.width: # si le rectangle va plus loin que la bordure gauche de l'ecran
            self.x = self.width
            self.changex *= -1

        if self.y > SCRN_H - self.height: # si le rectangle va plus loin que la bordure en haut de l'ecran
            self.y = SCRN_H - self.height
            self.changey *= -1

        if self.y < self.height: # si le rectangle va plus loin que la bordure en bas de l'ecran
            self.y = self.height
            self.changey *= -1

        arcade.finish_render() # afficher l'ecran apres avoir mis a jour

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle) # dessiner un rectangle sur l'ecran

#######################

def main():
    my_game = MyGame()
    my_game.setup()    
    
    arcade.run()

main()

#######################
