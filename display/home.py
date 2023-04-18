import pygame, time
import utils, display

""" 
reste a faire:
* mettre fond
* mettre blur ou filtre d'assombrissement sur le fond
* bouton echap
* bouton du jeu ...
"""

def main(screen, clock, screenSize):
    running = True
    
    #logo
    logo = pygame.image.load('assets/image/logo_0.9.png')
    xLogo = (screenSize[0] - int(logo.get_width())) // 2
    yLogo = (screenSize[1] - int(logo.get_height())) // 5
    
    #buttons
    settingsButton = pygame.image.load('assets/image/icon/settings.png')
    xSettingsButton = screenSize[0] - settingsButton.get_width() -20
    ySettingsButton = screenSize[1] - (screenSize[1] - 20)
    
    statisticButton = pygame.image.load('assets/image/icon/stat.png')
    xStatisticButton = xSettingsButton - settingsButton.get_width() - 20
    yStatisticButton = ySettingsButton
    
    exitButton = pygame.image.load('assets/image/icon/exit.png')
    positionExitButton = (20, screenSize[1] - (screenSize[1] - 20))
        
    while running:
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("purple")   
        
        screen.blit(logo, (xLogo, yLogo)) #affichage du logo
        
        #buttons display
        screen.blit(settingsButton, (xSettingsButton, ySettingsButton))
        screen.blit(statisticButton, (xStatisticButton, yStatisticButton))
        screen.blit(exitButton, positionExitButton)
            #affichage des boutons de jeu ------

        #buttons clicked
        if utils.click.isClicked(settingsButton, (xSettingsButton, ySettingsButton)):
            utils.click.zoom(screen, settingsButton, (xSettingsButton, ySettingsButton))
            display.settings.main(screen, clock, screenSize)
        if utils.click.isClicked(statisticButton, (xStatisticButton, yStatisticButton)):
            utils.click.zoom(screen, statisticButton, (xStatisticButton, yStatisticButton))
            display.stat.main(screen, clock, screenSize)
        if utils.click.isClicked(exitButton, positionExitButton):
            utils.click.zoom(screen, exitButton, positionExitButton)
            running = False
            
        pygame.display.flip()

        clock.tick(120)  # limits FPS to 60

    pygame.quit()