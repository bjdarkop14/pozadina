import pygame
pygame.init()
import timeit

APPLICATION_x_size = 500
APPLICATION_y_size = 500

clock = pygame.time.set_timer(pygame.USEREVENT,10)    # load clock

# a color can be: (0 to 255, 0 to 255, 0 to 255)
My_light_blue_color = (190, 190, 255)
My_light_red_color = (182, 0, 0)
FONT = pygame.font.Font(None, 32)

screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Crta')
pygame.mouse.set_visible(True)
black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
black_square_that_is_the_size_of_the_screen.fill((0, 0, 0))
screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))
pygame.display.flip()

def Crtaj(playerX, playerY, Surface, Color):
    pygame.draw.rect(Surface, Color, (playerX, playerY, 4, 4))


done = False
while not done:
    playerX = 194
    playerY = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.USEREVENT:
            Crtaj(playerX,playerY,screen,My_light_red_color)
            playerX = playerX + 10
            playerY = playerY + 10
    pygame.display.flip()