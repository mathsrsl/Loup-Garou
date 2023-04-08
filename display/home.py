import pygame
import utils, display

def main(screen, clock, screenSize):
    running = True

    #test
    # buttonsTab = []
    # button1 = utils.button.Button('appuis sur espace', 300, 40, (200, 100), 5)
    # buttonsTab.append(button1)
    
    logo = pygame.image.load('assets/image/logo.png')
    logo_resized = pygame.transform.scale(logo, (logo.get_width() // 1.5, logo.get_height() // 1.5))
    
    settingsButton = pygame.image.load('assets/image/icon/settings.png')
    settingsButton_resized = pygame.transform.scale(settingsButton, (settingsButton.get_width() // 1.5, settingsButton.get_height() // 1.5))
        #resize directement sur figma

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            #test
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.join.main(screen, clock, screenSize)
        

        screen.fill("purple")
        #affichage du logo
        xLogo = (screenSize[0] - int(logo_resized.get_width())) // 2
        yLogo = (screenSize[1] - int(logo_resized.get_height())) // 5
        screen.blit(logo_resized, (xLogo, yLogo))
        #affichage du bouton paramètre
        xSettingsButton = screenSize[0] - int(0.05*screenSize[0]) - settingsButton_resized.get_width()
        ySettingsButton = screenSize[1] - (screenSize[1] - int(0.05*screenSize[0]))
        screen.blit(settingsButton_resized, (xSettingsButton, ySettingsButton))

        # test
        # utils.button.buttons_draw(screen, buttonsTab)


        pygame.display.flip()

        clock.tick(120)  # limits FPS to 60

    pygame.quit()