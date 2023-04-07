import pygame
import utils, display

def main(screen, clock, screeSize):
    running = True
            
    #test
    buttonsTab = []
    button1 = utils.button.Button('appuis sur espace', 300, 40, (200, 100), 5)
    buttonsTab.append(button1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            #test
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.join.main(screen, clock, screeSize)
        

        screen.fill("blue")

        # RENDER YOUR GAME HERE
        utils.button.buttons_draw(screen, buttonsTab)


        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()