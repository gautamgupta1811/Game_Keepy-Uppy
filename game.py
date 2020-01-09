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
flag2 = True


def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(count), True, white)
    screen.blit(text, (100, 10))


def home_screen(flag2):
    ball_y = height - 100
    ball_x = width // 2
    sound_count = 0
    background = pygame.image.load(r"assets/background/homescreen.jpeg")
    background = pygame.transform.scale(background, (width, height))
    sound_icon = pygame.image.load(r"assets/images/sound_icon.png")
    sound_icon = pygame.transform.scale(sound_icon, (50, 50))
    sound_rect = pygame.Rect(10, 400, sound_icon.get_width(), sound_icon.get_height())
    football = pygame.image.load("assets/images/football.png")
    football = pygame.transform.scale(football, (100, 100))
    font = pygame.font.Font("assets/font/font_1.ttf", 80)
    title = font.render("KEPPY-UPPY", True, white)
    font1 = pygame.font.Font("assets/font/font_1.ttf", 50)
    easy = font1.render("Beginner", True, white)
    medium = font1.render("Intermediate", True, white)
    difficult = font1.render("Expert", True, white)
    easy_rect = pygame.Rect(50, height//2, 190, height//2 + 50)
    medium_rect = pygame.Rect(220, height // 2, 400, 3*height // 4 + 50)
    difficult_rect = pygame.Rect(450, height // 2, 600, height // 2 + 50)
    bg_sound = pygame.mixer.Sound("assets/sounds/background.wav")
    while True:
        screen.fill(white)
        screen.blit(background, (0, 0))
        screen.blit(title, (width // 2 - 170, 20))
        screen.blit(football, (ball_x, ball_y))
        screen.blit(easy, (50, height//2))
        screen.blit(medium, (220, height // 2))
        screen.blit(difficult, (450, height // 2))
        screen.blit(sound_icon, (10, 400))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 5, 5)
        if flag2:
            bg_sound.play()
        elif not flag2:
            bg_sound.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_rect.colliderect(sound_rect) and sound_count == 0:
                    flag2 = False
                    sound_count = 1
                elif mouse_rect.colliderect(sound_rect) and sound_count == 1:
                    flag2 = True
                    sound_count = 0
                if mouse_rect.colliderect(easy_rect):
                    bg_sound.stop()
                    beginner(0)

                if mouse_rect.colliderect(medium_rect):
                    bg_sound.stop()
                    intermediate(0)

                if mouse_rect.colliderect(difficult_rect):
                    bg_sound.stop()
                    expert(0)

        pygame.display.update()


def beginner(count):
    background = pygame.image.load(r"assets/background/game.jpeg")
    background = pygame.transform.scale(background, (width, height))

    # ball parameter
    football = pygame.image.load("assets/images/football.png")
    football = pygame.transform.scale(football, (100, 100))
    move_ball_y = -100
    ball_y = height - 100
    ball_x = width//2
    flag = False
    ball_kick = pygame.mixer.Sound(r"assets/sounds/football_kick.wav")
    while True:

        screen.fill(white)
        screen.blit(background, (0, 0))
        score(count)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 5, 5)
        screen.blit(football, (ball_x, ball_y))
        circle = pygame.Rect(ball_x, ball_y, football.get_width(), football.get_width())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if circle.colliderect(mouse_rect):
                    ball_y += move_ball_y
                    ball_x += random.choice([-15, 0, 15])
                    flag = True
                    count += 1
                    if flag2:
                        ball_kick.play()
        if flag:
            ball_y += 5

        if ball_y == height - 100:
            flag = False
            count = 0
        if ball_x <= 30:
            ball_x = 30
        if ball_x >= width - 30:
            ball_x = width - 30
        clock.tick(FPS)
        pygame.display.update()


def intermediate(count):
    background = pygame.image.load(r"assets/background/game.jpeg")
    background = pygame.transform.scale(background, (width, height))

    # ball parameter
    football = pygame.image.load("assets/images/football.png")
    football = pygame.transform.scale(football, (100, 100))
    move_ball_y = -100
    ball_y = height - 100
    ball_x = width//2
    flag = False
    ball_kick = pygame.mixer.Sound(r"assets/sounds/football_kick.wav")
    while True:

        screen.fill(white)
        screen.blit(background, (0, 0))
        score(count)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 5, 5)
        screen.blit(football, (ball_x, ball_y))
        circle = pygame.Rect(ball_x, ball_y, football.get_width(), football.get_width())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if circle.colliderect(mouse_rect):
                    ball_y += move_ball_y
                    ball_x += random.choice([-10, 0, 15])
                    flag = True
                    count += 1
                    if flag2:
                        ball_kick.play()
        if flag:
            ball_y += 10

        if ball_y == height - 100:
            flag = False
            count = 0
        if ball_x <= 30:
            ball_x = 30
        if ball_x >= width - 30:
            ball_x = width - 30
        clock.tick(FPS)
        pygame.display.update()


def expert(count):
    background = pygame.image.load(r"assets/background/game.jpeg")
    background = pygame.transform.scale(background, (width, height))

    # ball parameter
    football = pygame.image.load("assets/images/football.png")
    football = pygame.transform.scale(football, (100, 100))
    move_ball_y = -100
    ball_y = height - 100
    ball_x = width//2
    flag = False
    ball_kick = pygame.mixer.Sound(r"assets/sounds/football_kick.wav")
    while True:

        screen.fill(white)
        screen.blit(background, (0, 0))
        score(count)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 5, 5)
        screen.blit(football, (ball_x, ball_y))
        circle = pygame.Rect(ball_x, ball_y, football.get_width(), football.get_width())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if circle.colliderect(mouse_rect):
                    ball_y += move_ball_y
                    ball_x += random.randint(-20, 20)
                    flag = True
                    count += 1
                    if flag2:
                        ball_kick.play()
        if flag:
            ball_y += 5

        if ball_y == height - 100:
            flag = False
            count = 0
        if ball_x <= 30:
            ball_x = 30
        if ball_x >= width - 30:
            ball_x = width - 30
        clock.tick(FPS)
        pygame.display.update()


home_screen(flag2)
