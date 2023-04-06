import pygame, json
import display, utils


pygame.init()

with open("data.json", "r") as f:
        data = json.load(f)
        screenSize = data['settings']['screenSize']['size']
        isFullScreen = data['settings']['screenSize']['full']

if isFullScreen:
    screen = pygame.display.set_mode()
else: screen = pygame.display.set_mode(screenSize)

#logo = pygame.image.load("assets/image/icon.png")




pygame.display.set_caption("Loup-Garou") #titre de la fenêtre
# pygame.mouse.set_cursor(*pygame.cursors.arrow)
image = pygame.image.load("./assets/image/icon.svg").convert()
pygame.display.set_icon(image)

clock = pygame.time.Clock()

display.home.main(screen, clock, screenSize)