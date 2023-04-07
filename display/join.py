import pygame
import utils, display

def main(screen, clock, screeSize):
    running = True

    #création et gestion des boutons
    def buttons_draw(screen):
        for b in buttons:
            b.draw(screen)
            

    buttons = []
    button1 = utils.button.Button('Test 2', 200, 40, (100, 100), 5)
    buttons.append(button1)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        display.home.main(screen, clock, screeSize)
                    
        screen.fill("red")

        # RENDER YOUR GAME HERE
        buttons_draw(screen)
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    
# if __name__ == "__main__":
#     main(screen, clock)