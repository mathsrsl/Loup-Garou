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

    #test-----]
    button1 = utils.button.Button('appuis sur espace', (300, 200), 300)
    #---------
    
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
        
    while running:
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #test ----
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.join.main(screen, clock, screenSize)
        
        if button1.isClicked():
            display.join.main(screen, clock, screenSize)
        # ----
        
        screen.fill("purple")   
        
        screen.blit(logo, (xLogo, yLogo)) #affichage du logo
        
        button1.draw(screen) #test
        
        screen.blit(settingsButton, (xSettingsButton, ySettingsButton)) #affichage du bouton paramètre
        screen.blit(statisticButton, (xStatisticButton, yStatisticButton)) #affichage du bouton des statistiques
        #affichage des boutons de jeu

        #if settings button is clicked
        if utils.click.isClicked(settingsButton, (xSettingsButton, ySettingsButton)):
            utils.click.zoom(screen, settingsButton, (xSettingsButton, ySettingsButton))
            display.settings.main(screen, clock, screenSize)
        #if statistic button is clicked
        if utils.click.isClicked(statisticButton, (xStatisticButton, yStatisticButton)):
            utils.click.zoom(screen, statisticButton, (xStatisticButton, yStatisticButton))
            display.stat.main(screen, clock, screenSize)
            
        pygame.display.flip()

        clock.tick(120)  # limits FPS to 60

    pygame.quit()