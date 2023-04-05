import pygame
import sys 

pygame.init()

# user32 = ctypes.windll.user32 
# screensize = user32.GetSystemMetrics(78)-100, user32.GetSystemMetrics(79)-100

screen = pygame.display.set_mode()

width = screen.get_width()
height = screen.get_height()

print(width, height)


fenetre = pygame.display.set_mode(width, height) #taille de la fentre
pygame.display.set_caption("Loup-Garou") #titre de la fenêtre



fond = pygame.image.load("fond.jpg").convert() #image de fond
fenetre.blit(fond, (0,0))
perso = pygame.image.load("loup.png").convert_alpha()
fenetre.blit(perso, (200,300))
running = True

while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fenetre.blit(fond, (0,0))

    # Mise à jour de l'affichage
    pygame.display.update()
