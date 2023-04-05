import pygame
import ctypes 

pygame.init()

user32 = ctypes.windll.user32 
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

taille = (screensize)
fenetre = pygame.display.set_mode(screensize) #taille de la fentre
pygame.display.set_caption("Loup-Garou") #titre de la fenêtre



fond = pygame.image.load("fond.jpg").convert() #image de fond
perso = pygame.image.load("loup.png").convert_alpha()

running = True

while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fenetre.blit(fond, (0,0))

    # Mise à jour de l'affichage
    pygame.display.update()
