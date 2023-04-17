import pygame, json
import utils, display
from screeninfo import get_monitors

"""
bouton back/echap/retour
bouton 1000x600
bouton 1280x720
bouton 1920x1080
bouton fullscreen
si taille inférieur ou egale grisé bouton et écrire message
"""

def main(screen, clock, screenSize):
    #--- basic game settings for the reload of game ---
    pygame.init()
    
    with open("data.json", "r") as f:
        data = json.load(f)
        screenSize = data['settings']['screenSize']['size']
        isFullScreen = data['settings']['screenSize']['full']
        
    if isFullScreen:
        screen = pygame.display.set_mode()
        screenSize[0], screenSize[1] = screen.get_size()
    else:
        screen = pygame.display.set_mode(screenSize)
        
    pygame.display.set_caption("Loup-Garou") #titre de la fenêtre
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    image = pygame.image.load("./assets/image/logo.ico").convert()
    pygame.display.set_icon(image)

    clock = pygame.time.Clock()
    
    #--- settings display ---
    running = True
    
    # get the size of the computer screen
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height
    
    # calculation of buttons positions
    centre = screenSize[0] // 2
    button_1000_x = centre - 350
    button_1280_x = centre - 100
    button_1920_x = centre + 150
    button_fullScreen_x = centre - 100
    button_size_y = screenSize[1] // 2
    button_fullScreen_y = screenSize[1] // 1.5
    
    # creation of buttons
    button_1000 = utils.button.Button("1000x600", (button_1000_x, button_size_y), 200)
    button_1280 = utils.button.Button("1280x720", (button_1280_x, button_size_y), 200)
    button_1920 = utils.button.Button("1920x1080", (button_1920_x, button_size_y), 200)
    button_fullScreen = utils.button.Button("Full Screen", (button_fullScreen_x, button_fullScreen_y), 200)
    
    button_back = pygame.image.load('assets/image/icon/settings.png')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.home.main(screen, clock, screenSize)
                    
        screen.fill("black")
        
        #buttons display
        button_1000.draw(screen)
        button_1280.draw(screen)
        button_1920.draw(screen)
        button_fullScreen.draw(screen)
        
        # set the button for the current screen size in purple
        if isFullScreen:
            button_fullScreen.set_color(2)
        elif screenSize[0] == 1000:
            button_1000.set_color(2)
        elif screenSize[0] == 1280:
            button_1280.set_color(2)
        elif screenSize[0] == 1920:
            button_1920.set_color(2)
        
        # change the screen size if a button is clicked and reload the page
        if button_1000.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['size'] = [1000, 600]
                if data['settings']['screenSize']['full']:
                    data['settings']['screenSize']['full'] = False
                json.dump(data,f)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
        
        if button_1280.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['size'] = [1280, 700]
                if data['settings']['screenSize']['full']:
                    data['settings']['screenSize']['full'] = False
                json.dump(data,f)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
        
        if button_1920.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['size'] = [1920, 1080]
                if data['settings']['screenSize']['full']:
                    data['settings']['screenSize']['full'] = False
                json.dump(data,f)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
            
        if button_fullScreen.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['full'] = True
                json.dump(data,f)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
        
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()