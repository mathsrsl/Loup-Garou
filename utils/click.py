import pygame

def isClicked(surface, position):
    """returns if a surface is clicked

    Args:
        surface (pygame element): generally corresponds to a logo, an image, a geometric shape, a text ...
        position (tuple): a tuple of 2 int corresponding to the position (x, y) in pixels of the element 

    Returns:
        bool: returns True if the surface of the element is clicked 
    """
    mouse = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if position[0] <= mouse[0] <= position[0] + surface.get_width() and position[1] <= mouse[1] <= position[0] + surface.get_height():
            return True
    return False

def zoom(screen, image, position):
    """Used to zoom in on an image by 20% for 0.2 sec

    Args:
        screen,
        image,
        position (tuple)
    """
    zoom_out_factor=1.1
    
    image_width, image_height = image.get_size() # Récupère les dimensions de l'image
    
    # Calcule les nouvelles dimensions après le zoom
    zoomed_out_width = int(image_width * zoom_out_factor)
    zoomed_out_height = int(image_height * zoom_out_factor)
    
    # Calcule les nouvelles positions pour centrer l'image
    zoomed_out_x = position[0] + (image_width - zoomed_out_width) // 2
    zoomed_out_y = position[1] + (image_height - zoomed_out_height) // 2
    
    # Effectue l'effet de dézoom
    image = pygame.transform.scale(image, (zoomed_out_width, zoomed_out_height))
    screen.blit(image, (zoomed_out_x, zoomed_out_y))
    pygame.display.update()
    pygame.time.delay(100)
