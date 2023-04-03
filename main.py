import pygame

pygame.init()

fenetre = pygame.display.set_mode((400, 400)) #taille de la fentre
pygame.display.set_caption("Loup-Garou") #titre de la fenêtre

fond = pygame.image.load("fond.jpg").convert() #image de fond

running = True
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fenetre.blit(fond, (0,0))

    # Mise à jour de l'affichage
    pygame.display.update()
