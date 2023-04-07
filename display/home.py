import pygame
import utils, display

def main(screen, clock, screeSize):
    running = True

    #création et gestion des boutons
    def buttons_draw(screen):
        for b in buttons:
            b.draw(screen)
            

    buttons = []
    button1 = utils.button.Button('appuis sur espace', 300, 40, (200, 100), 5)
    buttons.append(button1)


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
        buttons_draw(screen)


        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()