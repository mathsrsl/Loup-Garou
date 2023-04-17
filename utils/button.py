import pygame

def buttons_draw(screen, buttonsTab): #draws all the buttons in the list
    for b in buttonsTab:
        b.draw(screen)
            
def isClicked(screen, button):
	#ou methode
    return False

class Button():
    def __init__(self, text, pos, width, height=70, elevation=5, clickable=True, idColor=1, fontSize=25, border_radius=20, pawDisplaying=True, colorText = '#FFFFFF'):
        #Core attributes 
        self.bgColor = [
            ('#000000', '#A7A7A7', '#616161'), 
            ('#1997EA', '#101278', '#38B0FF'), 
            ('#6C1FAD', '#290B47', '#9F2DFF')   
        ]
        self.pressed = False
        self.click = False
        self.clickable = clickable
        self.height = height
        self.width = width
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.pos = pos
        self.original_x_pos = pos[0]
        self.original_y_pos = pos[1]
        self.idColor = idColor
        self.fontSize = fontSize
        self.border_radius = border_radius
        self.pawDisplaying = pawDisplaying
        self.colorText = colorText
        self.text = text
        
    def draw(self, screen):
        self.screen = screen
        
        #button color
        if self.idColor-1 > len(self.bgColor) and self.clickable == True:
            self.color = self.bgColor[0][0], self.bgColor[0][1], self.bgColor[0][2], 0
        elif self.clickable == False:
            self.color = self.bgColor[0][2], self.bgColor[0][1], self.bgColor[0][2], 0
            
        else: 
            self.color = self.bgColor[self.idColor][0], self.bgColor[self.idColor][1], self.bgColor[self.idColor][2], self.idColor
        
        #top rectangle
        self.top_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.top_color = self.color[0]
        
        #bottom rectangle
        self.bottom_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.bottom_color = self.color[1]
        
        #text
        self.text_font = pygame.font.Font('./assets/font/inter/static/Inter-Black.ttf', self.fontSize)	#Font
        self.text_surf = self.text_font.render(self.text, True, self.colorText)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        
        # elevation logic
        self.top_rect.x = self.original_x_pos - (self.dynamic_elecation // 2)
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        
        self.text_rect.center = self.top_rect.center 
    
        self.bottom_rect.midtop = (int(self.top_rect.midtop[0] + self.dynamic_elecation//2), self.top_rect.midtop[1] + self.dynamic_elecation)
        self.bottom_rect.height = self.top_rect.height
        pygame.draw.rect(self.screen, self.bottom_color, self.bottom_rect, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius=self.border_radius)
        self.screen.blit(self.text_surf, self.text_rect)
        
        if self.pawDisplaying:
            self.pawImage = pygame.image.load(f'./assets/image/icon/patte_{self.color[3]}.png')
            self.xPositionImage = self.original_x_pos + self.width - self.pawImage.get_size()[0] - self.dynamic_elecation
            self.yPositionImage = self.original_y_pos + self.height - self.pawImage.get_size()[1] - self.dynamic_elecation
            self.screen.blit(self.pawImage, (self.xPositionImage, self.yPositionImage))
        
        self.check_click()
        
    def check_click(self):
        self.mouse = pygame.mouse.get_pos()
        # print(mouse) #---------------------------------------
        if self.clickable:
            if self.top_rect.collidepoint(self.mouse):
                self.top_color = self.color[2]                
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elecation = 0
                    self.pressed = True
                    self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
                else:
                    self.dynamic_elecation = self.elevation
                    if self.pressed == True: 
                        # pygame.time.delay(150)
                        self.pressed = False
                        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
                        self.click = True
            
            else:
                self.dynamic_elecation = self.elevation
                self.top_color = self.color[0]
    
    def isClicked(self):
        if self.click == True:
            self.click = False
            return True
        else: return False
    
    def set_text(self, newText):
        self.text = newText
        self.text_surf = self.text_font.render(self.text, True, self.colorText)
    
    def set_color_text(self, newColorText):
        self.colorText = newColorText
        self.text_surf = self.text_font.render(self.text, True, self.colorText)
    
    def set_clickable(self, value):
        if isinstance(value, bool):
            if self.clickable == True and value == False:
                self.oldColor = self.colorText
                self.colorText = '#FFFFFF'
            elif self.clickable == False and value == True:
                self.colorText = self.oldColor
            self.clickable = value     
        else:
            raise ValueError("La valeur doit être un booléen")