import pygame, json, time
import display, utils


pygame.init()

with open("data.json", "r") as f:
        data = json.load(f)
        screenSize = data['settings']['screenSize']['size']
        isFullScreen = data['settings']['screenSize']['full']

if isFullScreen:
    screen = pygame.display.set_mode()
else: screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Loup-Garou") #titre de la fenêtre
pygame.mouse.set_cursor(*pygame.cursors.arrow)
image = pygame.image.load("./assets/image/icon.ico").convert()
pygame.display.set_icon(image)

clock = pygame.time.Clock()


#affichage du logo
logo = pygame.image.load("assets/image/icon.png")
#coordonnées de l'image
x = (screenSize[0] - logo.get_width()) // 2
y = (screenSize[1] - logo.get_height()) // 2
# Afficher l'image pendant 2 secondes
start_time = time.time()
#effet zoom
zoom, direction = 1.0, -1


while time.time() - start_time < 1.5:
    screen.fill("white") # fond blanc
    
    if time.time() -start_time > 0.5:
        zoom += 0.002 * direction
        if zoom < 0:
            zoom =0
    
    # Redimensionner l'image en fonction du facteur de zoom
    new_width = int(logo.get_width()/3 * zoom)
    new_height = int(logo.get_height()/3 * zoom)
    logo_zoomed = pygame.transform.scale(logo, (new_width, new_height))

    # Coordonnées de l'image zoomée dans la fenêtre
    x_zoomed = (screenSize[0] - new_width) // 2
    y_zoomed = (screenSize[0] - new_height) // 2
    
    # Afficher l'image zoomée
    screen.blit(logo_zoomed, (x_zoomed, y_zoomed))
    
    pygame.display.flip() #rafraichir
    
display.home.main(screen, clock, screenSize)