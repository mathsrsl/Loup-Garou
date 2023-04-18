import pygame, json
import utils, display

def main(screen, clock, screenSize):
    running = True
    
    #creation of the title
    titleFont = pygame.font.Font('./assets/font/inter/static/Inter-Black.ttf', 35)
    titleText = titleFont.render("Your statistics", True, (255, 255, 255))
    text_width_title = titleText.get_rect().width
    
    #creation of the text
    textFont = pygame.font.Font('./assets/font/inter/static/Inter-Regular.ttf', 18)
    textFontValues = pygame.font.Font('./assets/font/inter/static/Inter-Light.ttf', 18)
    nbWinText = textFont.render("Number of wins", True, (255, 255, 255))
    nbGameText = textFont.render("Number of games played", True, (255, 255, 255))
    nbWolfText = textFont.render("Number of times one is a werewolf", True, (255, 255, 255))
    nbVillagerText = textFont.render("Number of times being a villager", True, (255, 255, 255))
    nbWitchText = textFont.render("Number of times being a witch", True, (255, 255, 255))
    
    #creation of buttons
    button_reset = utils.button.Button("Reset the values", (screenSize[0]//2 - 125, screenSize[1]//3 + 300), 250)
    homeButton = pygame.image.load('assets/image/icon/home.png')
    positionHomeButton = (20, screenSize[1] - (screenSize[1] - 20))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    display.home.main(screen, clock, screenSize)

        screen.fill("black")
        
        #creation of the values here to refresh them
        with open("data.json", "r") as f:
            data = json.load(f)
            nbWin = data['game']['stat']['nbWin']
            nbGame = data['game']['stat']['nbGame']
            nbWolf = data['game']['stat']['nbWolf']
            nbVillager = data['game']['stat']['nbVillager']
            nbWitch = data['game']['stat']['nbWitch']
            
        nbWinValue = textFontValues.render(f"{nbWin}", True, (255, 255, 255))
        nbGameValue = textFontValues.render(f"{nbGame}", True, (255, 255, 255))
        nbWolfValue = textFontValues.render(f"{nbWolf}", True, (255, 255, 255))
        nbVillagerValue = textFontValues.render(f"{nbVillager}", True, (255, 255, 255))
        nbWitchValue = textFontValues.render(f"{nbWitch}", True, (255, 255, 255))

        #title display
        screen.blit(titleText, (screenSize[0]//2 - (text_width_title//2), screenSize[1]//6))
        
        #text display
        text_x_position = screenSize[0]//6
        text_y_position = screenSize[1]//3
        screen.blit(nbWinText, (text_x_position, text_y_position))
        screen.blit(nbGameText, (text_x_position, text_y_position +50))
        screen.blit(nbWolfText, (text_x_position, text_y_position +100))
        screen.blit(nbVillagerText, (text_x_position, text_y_position +150))
        screen.blit(nbWitchText, (text_x_position, text_y_position +200))
        
        #values display
        text_x_position_values = screenSize[0] - text_x_position
        screen.blit(nbWinValue, (text_x_position_values, text_y_position))
        screen.blit(nbGameValue, (text_x_position_values, text_y_position +50))
        screen.blit(nbWolfValue, (text_x_position_values, text_y_position +100))
        screen.blit(nbVillagerValue, (text_x_position_values, text_y_position +150))
        screen.blit(nbWitchValue, (text_x_position_values, text_y_position +200))
        
        #buttons display
        button_reset.draw(screen)
        if nbWin + nbGame + nbWolf + nbVillager + nbWitch == 0:
            button_reset.set_clickable(False)
        else:
            button_reset.set_clickable(True)

        screen.blit(homeButton, positionHomeButton)
            
        #buttons clicked
        if button_reset.isClicked():
            with open("data.json", "w") as f:
                data['game']['stat']['nbWin'] = 0
                data['game']['stat']['nbGame'] = 0
                data['game']['stat']['nbWolf'] = 0
                data['game']['stat']['nbVillager'] = 0
                data['game']['stat']['nbWitch'] = 0
                json.dump(data,f, indent=4)
                
        if utils.click.isClicked(homeButton, positionHomeButton):
            utils.click.zoom(screen, homeButton, positionHomeButton)
            display.home.main(screen, clock, screenSize)
        
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
