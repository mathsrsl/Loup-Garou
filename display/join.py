import pygame
import utils, display

def main(screen, clock, screenSize):
    running = True
            
    #test
    button1 = utils.button.Button('appuis sur espace',(200, 100), 300, height=40, clickable=False, elevation=7, idColor=2, fontSize=15, borderRadius=12, pawDisplaying=False, colorText='#F3A8AF')
    button2 = utils.button.Button('appuis sur espace',(200, 300), 300)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.home.main(screen, clock, screenSize)
                if event.key == pygame.K_1:
                    button2.set_text('vroum la voiture')
                if event.key == pygame.K_2:
                    button2.set_color_text('#12F148')
                if event.key == pygame.K_3:
                    button2.set_clickable(False)
                if event.key == pygame.K_4:
                    button2.set_clickable(True)
                if event.key == pygame.K_5:
                    button1.set_clickable(True)
                if event.key == pygame.K_6:
                    button1.set_clickable(False)                     
                    
        screen.fill("grey")

        # RENDER YOUR GAME HERE
        button1.draw(screen)
        button2.draw(screen)
        
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()