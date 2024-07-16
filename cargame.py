import pygame
from pygame.locals import *
import random

def restart_game():
    global jerry_loc, tom_loc, speed, counter, points, game_over
    jerry_loc.center = (left_lane, height * 0.8)
    tom_loc.center = (right_lane, height * 0.2)
    speed = 1
    counter = 0
    points = 0
    game_over = False
    screen.fill((60, 220, 0))
    pygame.display.update()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Game")
screen.fill((60, 220, 0))

pygame.display.update()

jerry = pygame.image.load("jerry Car.png")
jerry_loc = jerry.get_rect()
jerry_loc.center = (left_lane, height * 0.8)

tom = pygame.image.load("tom Car.png")
tom_loc = tom.get_rect()
tom_loc.center = (right_lane, height * 0.2)

font = pygame.font.SysFont('Times New Roman', 50)
game_over_font = pygame.font.SysFont('Times New Roman', 75)
button_font = pygame.font.SysFont('Times New Roman', 30)

counter = 0
points = 0
game_over = False

while running:
    if not game_over:
        counter += 1
        if counter == 5000:
            speed += 0.25
            counter = 0
            print("LEVEL UP! ", speed)
        tom_loc[1] += speed
        if tom_loc[1] > height:
            points += 1
            if random.randint(0, 1) == 0:
                tom_loc.center = (right_lane, -200)
            else:
                tom_loc.center = (left_lane, -200)

        if jerry_loc[0] == tom_loc[0] and tom_loc[1] > jerry_loc[1] - 165:
            game_over = True

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in [K_d, K_RIGHT] and jerry_loc.centerx != right_lane:
                    jerry_loc = jerry_loc.move([int(road_w / 2), 0])
                if event.key in [K_a, K_LEFT] and jerry_loc.centerx != left_lane:
                    jerry_loc = jerry_loc.move([-int(road_w / 2), 0])

        screen.fill((60, 220, 0))

        pygame.draw.rect(
            screen,
            (50, 50, 50),
            (width / 2 - road_w / 2, 0, road_w, height)
        )

        pygame.draw.rect(
            screen,
            (255, 240, 60),
            (width / 2 - roadmark_w / 2, 0, roadmark_w, height)
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height)
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height)
        )

        screen.blit(jerry, jerry_loc)
        screen.blit(tom, tom_loc)
        pygame.display.update()

    else:
        screen.fill((10, 10, 30))
        draw_text('GAME OVER!', game_over_font, (255, 0, 0), screen, width / 2, height / 2 - 50)
        draw_text(f'POINTS: {points}', font, (255, 255, 255), screen, width / 2, height / 2 + 20)

        restart_button = pygame.Rect(width / 2 - 100, height / 2 + 80, 200, 50)
        quit_button = pygame.Rect(width / 2 - 100, height / 2 + 150, 200, 50)

        pygame.draw.rect(screen, (0, 255, 0), restart_button)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)

        draw_text('Restart', button_font, (0, 0, 0), screen, restart_button.centerx, restart_button.centery)
        draw_text('Quit', button_font, (0, 0, 0), screen, quit_button.centerx, quit_button.centery)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    restart_game()
                if quit_button.collidepoint(event.pos):
                    running = False

pygame.quit()
