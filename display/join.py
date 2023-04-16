import pygame
import utils, display

def main(screen, clock, screenSize):
    running = True
            
    #test
    buttonsTab = []
    button1 = utils.button.Button('appuis sur espace',(200, 100), 300, 40, elevation=7, color=2, fontSize=15)
    buttonsTab.append(button1)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.home.main(screen, clock, screenSize)
                    
        screen.fill("grey")

        # RENDER YOUR GAME HERE
        utils.button.buttons_draw(screen, buttonsTab)
        
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()