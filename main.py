# Pygame game template

import pygame
import sys
import config # Import the config module
import shapes

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_text(screen, font_pose, text='No text', font_size=10, font_name='DejaVuSans.ttf', font_color= (0,0,0), italic=False, bold=False, rotation=0):
    pygame.font.init()
    font = pygame.font.Font(font_name, font_size)
    font.set_italic(italic)
    font.set_bold(bold)
    text_surface = font.render(text, True, font_color)
    if rotation != 0:
        text_surface = pygame.transform.rotate(text_surface, rotation)
    text_rect = text_surface.get_rect(center=(font_pose))
    screen.blit(text_surface, text_rect.topleft)

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    rotation = 0
   # ball = shapes.Circ(screen, config.GOLD, [600,400], 100, 5)
    x1 = 50
    y1 = 50
    size_x = 100
    size_y = 100
    change_x1 = 5
    change_y1 = 5
    #box = shapes.Rect(screen, config.ELECTRICLIME, x1 ,y1 ,200 , 300, 10)


    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        rotation += 10
        x1 += change_x1
        y1 += change_y1


        if x1 + size_x> config.WINDOW_WIDTH or x1 - 50 < 0:
            change_x1 = change_x1 * -1
        if y1 + size_y> config.WINDOW_HEIGHT or y1 - 50 < 0:
            change_y1 = change_y1 * -1

       # ball.draw()
        #box.draw()
        draw_text(screen, [x1,y1], 'SPINNNNNNNNNNNNNNNNNNNNNNNNN', 50, font_color=config.RICHMAROON, rotation=rotation)
        pygame.display.flip()
        
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()
