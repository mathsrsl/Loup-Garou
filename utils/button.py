import pygame

"""
mettre a jour la classe permettant de redesigner le bouton et de pouvoir détecter s'il est cliquer directement avec la classe
faire aussi une méthode pour l'afficher
lors de la création du bouton, on demande le texte, widht, height, position sur la page, la couleur du texte, la couleur du fonc,
la couleur quand c'est cliqué ou hover, la font eventuelelment, la font size et éventuellement la hauteur de relief
"""

def buttons_draw(screen, buttonsTab): #draws all the buttons in the list
    for b in buttonsTab:
        b.draw(screen)
            
def isClicked(screen, button):
	#ou methode
    return False

class Button():
    def __init__(self, text, pos, width, height=70, elevation=5, idColor=0, fontSize=25, border_radius=20, pawDisplaying=True):
        #Core attributes 
        self.bgColor = [
            ('#000000', '#A7A7A7', '#414141'), 
            ('#1997EA', '#101278', '#38B0FF'), 
            ('#6C1FAD', '#290B47', '#9F2DFF')   
        ]
        self.pressed = False
        self.click = False
        self.height = height
        self.width = width
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_x_pos = pos[0]
        self.original_y_pos = pos[1]
        self.idColor = idColor
        self.fontSize = fontSize
        self.border_radius = border_radius
        self.pawDisplaying = pawDisplaying
        
        #button color
        if self.idColor-1 > len(self.bgColor):
            self.color = self.bgColor[0][0], self.bgColor[0][1], self.bgColor[0][2], 0
        else: 
            self.color = self.bgColor[idColor][0], self.bgColor[idColor][1], self.bgColor[idColor][2], idColor
        
        #top rectangle
        self.top_rect = pygame.Rect(pos, (self.width, self.height))
        self.top_color = self.color[0]
        
        #bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (self.width, self.height))
        self.bottom_color = self.color[1]
        
        #text
        self.text_font = pygame.font.Font('./assets/font/inter/static/Inter-Black.ttf', self.fontSize)	#Font
        self.text = text
        self.text_surf = self.text_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
    
    def change_text(self, newtext):
        self.text_surf = self.text_font.render(newtext, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        
    def draw(self, screen):
        # elevation logic
        self.top_rect.x = self.original_x_pos - (self.dynamic_elecation // 2)
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        
        self.text_rect.center = self.top_rect.center 
    
        self.bottom_rect.midtop = (int(self.top_rect.midtop[0] + self.dynamic_elecation//2), self.top_rect.midtop[1] + self.dynamic_elecation)
        self.bottom_rect.height = self.top_rect.height
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=self.border_radius)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=self.border_radius)
        screen.blit(self.text_surf, self.text_rect)
        
        if self.pawDisplaying:
            self.pawImage = pygame.image.load(f'./assets/image/icon/patte_{self.color[3]}.png')
            self.xPositionImage = self.original_x_pos + self.width - self.pawImage.get_size()[0] - self.dynamic_elecation
            self.yPositionImage = self.original_y_pos + self.height - self.pawImage.get_size()[1] - self.dynamic_elecation
            screen.blit(self.pawImage, (self.xPositionImage, self.yPositionImage))
        
        self.check_click()
        
    def check_click(self):
        self.mouse = pygame.mouse.get_pos()
        # print(mouse) #---------------------------------------
        if self.top_rect.collidepoint(self.mouse):
            self.top_color = self.color[2]                
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    # pygame.time.delay(150)
                    self.pressed = False
                    self.change_text(self.text)
                    self.click = True
                    
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = self.color[0]