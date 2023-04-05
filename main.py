import display, utils
import pygame


pygame.init()

screenSize = (400, 400)
screen = pygame.display.set_mode(screenSize) #si vide alors plein écran

pygame.display.set_caption("Loup-Garou") #titre de la fenêtre
# pygame.mouse.set_cursor(*pygame.cursors.arrow)
image = pygame.image.load("./assets/image/logo.jpg").convert()
pygame.display.set_icon(image)

clock = pygame.time.Clock()

display.home.main(screen, clock, screenSize)