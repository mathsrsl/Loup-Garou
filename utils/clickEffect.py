import pygame

def zoom(screen, image, position):
    """Used to zoom in on an image by 20% for 0.2 sec

    Args:
        screen,
        image,
        position (tuple)
    """
    zoom_out_factor=1.2
    
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
    pygame.time.delay(150)
