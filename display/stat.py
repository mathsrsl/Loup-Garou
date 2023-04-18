import pygame, json
import utils, display

def main(screen, clock, screenSize):
    running = True
    
    #creation of the title
    titleFont = pygame.font.Font('./assets/font/inter/static/Inter-Black.ttf', 30)
    titleText = titleFont.render("Your statistics", True, (255, 255, 255))
    text_width_title = titleText.get_rect().width
    
    #creation of the text
    textFont = pygame.font.Font('./assets/font/inter/static/Inter-Regular.ttf', 20)
    nbWinText = textFont.render("Number of wins", True, (255, 255, 255))
    nbGameText = textFont.render("Number of games played", True, (255, 255, 255))
    nbWolfText = textFont.render("Number of times one is a werewolf", True, (255, 255, 255))
    nbVillagerText = textFont.render("Number of times being a villager", True, (255, 255, 255))
    nbWitchText = textFont.render("Number of times being a witch", True, (255, 255, 255))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    display.home.main(screen, clock, screenSize)

        screen.fill("black")

        screen.blit(titleText, (screenSize[0]//2 - (text_width_title // 2), 150))

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
