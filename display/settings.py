import pygame
import utils, display

def main(screen, clock, screenSize):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.home.main(screen, clock, screenSize)
                    
        screen.fill("blue")
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()