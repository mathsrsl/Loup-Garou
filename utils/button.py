import pygame

"""
mettre a jour la classe permettant de redesigner le bouton et de poouvoir détecter s'il est cliquer directement avec la classe
faire aussi une méthode pour l'afficher
lors de la création du bouton, on demande le texte, widht, height, position sur la page, la couleur du texte, la couleur du fonc,
la couleur quand c'est cliqué ou hover, la font eventuelelment, la font size et éventuellement la hauteur de relief
"""


buttons = []

def buttons_draw(screen, buttonsTab):
        for b in buttonsTab:
            b.draw(screen)

class Button():
	def __init__(self, text, width, height, pos, elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos, (width, height))
		self.top_color = '#015E5E'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos, (width, height))
		self.bottom_color = '#014A4A'
		#text
		self.text_font = pygame.font.Font('./assets/font/inconsolata.ttf', 30)	#Font
		self.text = text
		self.text_surf = self.text_font.render(text, True, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

	def change_text(self, newtext):
		self.text_surf = self.text_font.render(newtext, True, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

	def draw(self, screen):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
		pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse):
			self.top_color = '#02DADA'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.pressed = False
					self.change_text(self.text)
				
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#015E5E'