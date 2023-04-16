import pygame, time
import utils, display

def main(screen, clock, screenSize):
    running = True

    #test-----]
    button1 = utils.button.Button('appuis sur espace', (300, 200), 300)
    #---------
    
    logo = pygame.image.load('assets/image/logo_0.9.png')
    xLogo = (screenSize[0] - int(logo.get_width())) // 2
    yLogo = (screenSize[1] - int(logo.get_height())) // 5
    
    settingsButton = pygame.image.load('assets/image/icon/settings.png')
    xSettingsButton = screenSize[0] - settingsButton.get_width() -20
    ySettingsButton = screenSize[1] - (screenSize[1] - 20)
        
    while running:
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #si touche préssée
                if pygame.mouse.get_pressed()[0]: #si clique gauche
                    if xSettingsButton <= mouse[0] <= xSettingsButton + settingsButton.get_width() and ySettingsButton <= mouse[1] <= ySettingsButton + settingsButton.get_height():
                        utils.clickEffect.zoom(screen, settingsButton, (xSettingsButton, ySettingsButton))
                        display.settings.main(screen, clock, screenSize)
                
            #test
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.join.main(screen, clock, screenSize)
            
        if button1.click: #click button test
            button1.click = False
            display.join.main(screen, clock, screenSize)
        
        screen.fill("purple")   
        
        screen.blit(logo, (xLogo, yLogo)) #affichage du logo
        
        #test
        button1.draw(screen)
        
        screen.blit(settingsButton, (xSettingsButton, ySettingsButton)) #affichage du bouton paramètre
        #affichage du bouton des statistiques
        #affichage des boutons de jeu

        pygame.display.flip()

        clock.tick(120)  # limits FPS to 60

    pygame.quit()