import pygame
from pygame.locals import *

def load_IMG(loc):
    return pygame.image.load("images/"+loc+".png").convert()

class object:
    def __init__(self, name="", place=(0, 0), source=None, visible = True):
        self.name = name
        self.x, self.y = place
        self.place = 32*self.x, 32*self.y
        self.source = source
        self.visible = visible
        self.rotation = 0

    def draw(self, screen):
        self.place = 32*self.x, 32*self.y
        if self.visible and self.source is not None:
            screen.blit(self.source, self.place)

    def __repr__(self):
        if self.name != "":
            return "<object {} at ({}, {})>".format(self.name, self.x, self.y)
        return "<object>"

def init():
    global framerate, screen, objects, layers, player
    pygame.init()
    width = 640
    heigth = 480
    game_width = width // 32 #20
    game_heigth = heigth // 32 #15
    screen = pygame.display.set_mode((width+10, heigth+10))
    layers = [
        #backgroundlayer
        [],
        #tilelayer
        [],
        #spritelayer
        [],
    ]
    objects = layers[0]
    objects.append(object(name = "bg", source = load_IMG("blackbackground")))
    objects = layers[1]
    for x in range(game_width):
        for y in range(game_heigth):
            objects.append(object(name = "tile", place =[x, y], source = load_IMG("/tiles/sand")))
    objects = layers[2]

    player = object(
        "player",
        (
            int(game_width/2),
            int(game_heigth/2)
        ),
        load_IMG("/sprites/player")
    )

    objects.append(player)

    framerate = 100
    running = False

def render():
    for objects in layers:
        for obj in objects:
            obj.draw(screen)

def handle_events():
    global running, player
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.y += 1
            if event.key == pygame.K_w:
                player.y -= 1
            if event.key == pygame.K_d:
                player.x += 1
            if event.key == pygame.K_a:
                player.x -= 1

            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False


def mainloop():
    global running
    running = True
    while running:
        handle_events()
        if not running:break
        render()
        pygame.display.update()
        pygame.time.delay(framerate)
