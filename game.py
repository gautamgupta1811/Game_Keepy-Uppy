import pygame
import random
pygame.init()


height = 480
width = 640

screen = pygame.display.set_mode((width, height))

# colors
green = 0, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
black = 0, 0, 0
white = 255, 255, 255

# clock
clock = pygame.time.Clock()
FPS = 30
count = 0


def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(count), True, black)
    screen.blit(text, (100, 10))


# ball parameter
move_ball_Y = -100
ball_y = height - 80
ball_X = width//2
Flag = False
while True:
    screen.fill(white)
    score(count)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse_x, mouse_y, 5, 5)
    ground = pygame.draw.rect(screen, green, [0, height - 50, width, height])
    circle = pygame.draw.circle(screen, black, [ball_X, ball_y], 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if circle.colliderect(mouse_rect):
                ball_y += move_ball_Y
                ball_X += random.choice([-25, 0, 25])
                Flag = True
                count += 1
    if Flag:
        ball_y += 10

    if ball_y == height - 80:
        Flag = False
        count = 0
    if ball_X <= 30:
        ball_X = 30
    if ball_X >= width - 30:
        ball_X = width - 30
    clock.tick(FPS)
    pygame.display.update()
