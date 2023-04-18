import pygame, json
import utils, display
from screeninfo import get_monitors

"""
reste à faire : 
* bouton back/echap/retour/home
* ajouter un fond
* mettre blur ou filtre d'assombrissement sur le fond
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
    
    # creation of a text in case of non conformity of the screen
    allCompatible = True
    infoFont = pygame.font.Font('./assets/font/inter/static/Inter-Regular.ttf', 15)
    infoText = infoFont.render("(Votre écran n'est pas compatible avec les dimensions inscrites sur les boutons grisés)", True, (194, 194, 194))
    text_width_info = infoText.get_rect().width
    
    #creation of the title
    titleFont = pygame.font.Font('./assets/font/inter/static/Inter-Black.ttf', 30)
    titleText = titleFont.render("Taille de la fenêtre", True, (255, 255, 255))
    text_width_title = titleText.get_rect().width
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    display.home.main(screen, clock, screenSize)
                    
        screen.fill("black")
        
        #display title
        screen.blit(titleText, (centre - (text_width_title // 2), button_size_y - 150))
        
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
            
        #disables buttons whose size is not compatible with the screen
        if screen_width <= 1920 or screen_height <= 1080:
            allCompatible = False
            button_1920.set_clickable(False)
        if screen_width <= 1280 or screen_height <= 700:
            allCompatible = False
            button_1280.set_clickable(False)
        if screen_width <= 1000 or screen_height <= 600:
            allCompatible = False
            button_1000.set_clickable(False)
            
        #displays explanations if sizes are incompatible
        if not allCompatible:
            screen.blit(infoText, (centre - (text_width_info // 2), button_size_y - 50))
        
        # change the screen size if a button is clicked and reload the page
        if button_1000.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['size'] = [1000, 600]
                if data['settings']['screenSize']['full']:
                    data['settings']['screenSize']['full'] = False
                json.dump(data,f, indent=4)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
        
        if button_1280.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['size'] = [1280, 700]
                if data['settings']['screenSize']['full']:
                    data['settings']['screenSize']['full'] = False
                json.dump(data,f, indent=4)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
        
        if button_1920.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['size'] = [1920, 1080]
                if data['settings']['screenSize']['full']:
                    data['settings']['screenSize']['full'] = False
                json.dump(data,f, indent=4)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
            
        if button_fullScreen.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['full'] = True
                json.dump(data,f, indent=4)
            pygame.quit()
            display.settings.main(screen, clock, (screenSize))
        
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()