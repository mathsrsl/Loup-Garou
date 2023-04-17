import pygame, json
import utils, display

"""
bouton back/echap/retour
bouton 1000x600
bouton 1280x720
bouton 1920x1080
bouton fullscreen
si taille inférieur ou egale grisé bouton et écrire message
"""

def main(screen, clock, screenSize):
    running = True
    
    with open("data.json", "r") as f:
        data = json.load(f)
        screenSize = data['settings']['screenSize']['size']
        isFullScreen = data['settings']['screenSize']['full']
        
    if isFullScreen:
        screen = pygame.display.set_mode()
        screenSize[0], screenSize[1] = screen.get_size()
    else:
        screen = pygame.display.set_mode(screenSize)
    
    centre = screenSize[0] // 2
    button_1000_x = centre - 350
    button_1280_x = centre - 100
    button_1920_x = centre + 150
    button_fullScreen_x = centre - 100
    
    button_1000 = utils.button.Button("1000x600", (button_1000_x, 300), 200)
    button_1280 = utils.button.Button("1280x720", (button_1280_x, 300), 200)
    button_1920 = utils.button.Button("1920x1080", (button_1920_x, 300), 200)
    button_fullScreen = utils.button.Button("Full Screen", (button_fullScreen_x, 400), 200)
    
    
    
    button_back = pygame.image.load('assets/image/icon/settings.png')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.home.main(screen, clock, screenSize)
                    
        screen.fill("black")
        
        button_1000.draw(screen)
        button_1280.draw(screen)
        button_1920.draw(screen)
        button_fullScreen.draw(screen)
        
        if button_1280.isClicked():
            with open("data.json", "w") as f:
                data['settings']['screenSize']['size'] = [1280, 700]
                json.dump(data,f)
            display.settings.main(screen, clock, (screenSize))
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()