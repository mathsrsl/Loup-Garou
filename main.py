import pygame
import utils.button as button

# pygame setup
pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height)) #si vide alors plein écran
pygame.display.set_caption("Loup-Garou") #titre de la fenêtre
image = pygame.image.load("logo.jpg").convert()
pygame.display.set_icon(image)
clock = pygame.time.Clock()
running = True

pygame.mouse.set_cursor(*pygame.cursors.arrow)

#création et gestion des boutons
def buttons_draw(screen):
    for b in buttons:
        b.draw(screen)
        

buttons = []
button1 = button.Button('Resume', 200, 40, (width, height), 5)
buttons.append(button1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill("purple")

    # RENDER YOUR GAME HERE
    


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()