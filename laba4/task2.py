import pygame
from pygame.draw import *
from math import pi
#colors
COLOR_BROWN = (82, 69, 16)
COLOR_LIGHT_BROWN = (124, 102, 29)
COLOR_ORANGE = (188, 117, 66)
COLOR_LIGHT_ORANGE = (214, 172, 140)

COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (143, 168, 50)
COLOR_GRAY = (153, 153, 153)
COLOR_DARK_GREY = (106, 94, 84)
COLOR_LIGHT_GREY = (239, 216, 216)
COLOR_CLEAR_BLUE = (102, 209, 250)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (153, 203, 220)
COLOR_LIGHT_BLUE = (221, 254, 232)
pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 900))

rect(screen, COLOR_BROWN, (0, 0, 600, 400))
rect(screen, COLOR_LIGHT_BROWN, (0, 400, 600, 700))

# because pygame have not int() inside
def ellipse1(sf, cl, coords):
    ellipse(sf, cl, (int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])))


def ellipse2(sf, cl, coords, wid):
    ellipse(sf, cl, (int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])), int(wid))


def rect1(sf, cl, coords):
    rect(sf, cl, (int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])))


def draw_window(scale):
    surface = pygame.Surface((scale * 290, scale * 430))
    surface.fill(COLOR_LIGHT_BLUE)
    rect1(surface, COLOR_BLUE, (scale * 10, scale * 7, scale * 130, scale * 100))
    rect1(surface, COLOR_BLUE, (scale * 10 + scale * 140, scale * 7, scale * 130, scale * 100))
    rect1(surface, COLOR_BLUE, (scale * 10, scale * 7 + scale * 110, scale * 130, scale * 300))
    rect1(surface, COLOR_BLUE, (scale * 10 + scale * 140, scale * 7 + scale * 110, scale * 130, scale * 300))
    return surface


def draw_cat(scale, chirality, color):
    if color == 'orange':
        COLOR_IN = COLOR_ORANGE
        COLOR_EAR = COLOR_LIGHT_ORANGE
        COLOR_EYE = COLOR_GREEN
    if color == 'gray':
        COLOR_IN = COLOR_DARK_GREY
        COLOR_EAR = COLOR_LIGHT_GREY
        COLOR_EYE = COLOR_CLEAR_BLUE
    surface = pygame.Surface((scale * 600, scale * 430))

    surface.fill(COLOR_LIGHT_BROWN)
    # tail
    surface1 = pygame.Surface((scale * 300, scale * 300))
    surface1.fill(COLOR_LIGHT_BROWN)

    ellipse1(surface1, COLOR_IN, (0, 0, scale * 300, scale * 80))

    surface2 = pygame.transform.rotate(surface1, -30)
    surface.blit(surface2, (scale * 250, scale * 40))
    # body
    ellipse1(surface, COLOR_IN, (scale * 70, scale * 10, scale * 350, scale * 200))
    # back paw
    ellipse1(surface, COLOR_IN, (scale * 320, scale * 90, scale * 140, scale * 140))

    ellipse1(surface, COLOR_IN, (scale * 420, scale * 180, scale * 40, scale * 110))
    # right paw
    ellipse1(surface, COLOR_IN, (scale * 90, scale * 170, scale * 80, scale * 40))
    # left paw
    ellipse1(surface, COLOR_IN, (scale * 50, scale * 110, scale * 40, scale * 80))

    # head
    ellipse1(surface, COLOR_IN, (scale * 10, scale * 20, scale * 140, scale * 140))
    # ears
    polygon(surface, COLOR_IN,
            ([int(scale * 7), int(scale * 15)], [int(scale * 25), int(scale * 60)], [int(scale * 50), int(scale * 40)]))

    polygon(surface, COLOR_EAR,
            (
                [int(scale * 12), int(scale * 20)], [int(scale * 27), int(scale * 55)],
                [int(scale * 45), int(scale * 40)]))

    polygon(surface, COLOR_IN, (
        [int(160 * scale - scale * 7), int(scale * 15)], [int(160 * scale - scale * 25), int(scale * 60)],
        [int(160 * scale - scale * 50), int(scale * 40)]))
    polygon(surface, COLOR_EAR,
            ([int(160 * scale - scale * 12), int(scale * 20)], [int(160 * scale - scale * 27), int(scale * 55)],
             [int(160 * scale - scale * 45), int(scale * 40)]))

    # eyes
    ellipse1(surface, COLOR_EYE, (scale * 40, scale * 70, scale * 40, scale * 40))
    ellipse1(surface, COLOR_BLACK, (scale * 60, scale * 70, scale * 8, scale * 40))
    surface_eye1 = pygame.Surface((scale * 10, scale * 10))
    surface_eye1.fill(COLOR_EYE)
    ellipse1(surface_eye1, COLOR_WHITE, (0, 0, scale * 15, scale * 5))
    surface_eye2 = pygame.transform.rotate(surface_eye1, -45)
    surface.blit(surface_eye2, (scale * 50, scale * 80))
    ellipse1(surface, COLOR_EYE, (scale * 60 + scale * 40, scale * 70, scale * 40, scale * 40))
    ellipse1(surface, COLOR_BLACK, (scale * 60 + scale * 60, scale * 70, scale * 8, scale * 40))
    surface.blit(surface_eye2, (scale * 60 + scale * 50, scale * 80))
    # nose
    polygon(surface, COLOR_EAR, (
        [int(scale * 80), int(scale * 110)], [int(scale * 90), int(scale * 110)], [int(scale * 85), int(scale * 120)]))
    # mouth
    line(surface, COLOR_BLACK, [int(scale * 85), int(scale * 120)], [int(scale * 85), int(scale * 130)])
    arc(surface, COLOR_BLACK, (int(scale * 85), int(scale * 120), int(scale * 15), int(scale * 15)), pi, 0)
    arc(surface, COLOR_BLACK, (int(scale * 72), int(scale * 120), int(scale * 15), int(scale * 15)), pi, 0)
    # whiskers
    line(surface, COLOR_BLACK, [int(0), int(scale * 120)], [int(scale * 70), int(scale * 123)])
    line(surface, COLOR_BLACK, [int(0), int(scale * 130)], [int(scale * 70), int(scale * 130)])
    line(surface, COLOR_BLACK, [int(0), int(scale * 140)], [int(scale * 70), int(scale * 135)])

    line(surface, COLOR_BLACK, [int(180 * scale - 0), int(scale * 120)],
         [int(180 * scale - scale * 70), int(scale * 123)])
    line(surface, COLOR_BLACK, [int(180 * scale - 0), int(scale * 130)],
         [int(180 * scale - scale * 70), int(scale * 130)])
    line(surface, COLOR_BLACK, [int(180 * scale - 0), int(scale * 140)],
         [int(180 * scale - scale * 70), int(scale * 135)])
    if chirality == 'left':
        return surface
    if chirality == 'right':
        return pygame.transform.flip(surface, True, False)


def draw_ball(scale, chirality):
    surface = pygame.Surface((scale * 400, scale * 200))
    surface.fill(COLOR_LIGHT_BROWN)
    ellipse1(surface, COLOR_GRAY, (scale * 200, 0, scale * 200, scale * 200))
    arc(surface, COLOR_BLACK, (int(scale * 210), int(scale * 30), int(scale * 200), int(scale * 200)), 0, pi / 2)
    arc(surface, COLOR_BLACK, (int(scale * 180), int(scale * 40), int(scale * 200), int(scale * 200)), pi * 0.2, pi / 2)
    arc(surface, COLOR_BLACK, (int(scale * 160), int(scale * 50), int(scale * 200), int(scale * 200)), pi * 0.1, pi / 2)
    arc(surface, COLOR_BLACK, (int(scale * 250), int(scale * 120), int(scale * 200), int(scale * 200)), pi / 2,
        pi - pi * 0.2)
    arc(surface, COLOR_BLACK, (int(scale * 230), int(scale * 110), int(scale * 200), int(scale * 200)), pi / 2,
        pi - pi * 0.2)
    arc(surface, COLOR_BLACK, (int(scale * 190), int(scale * 100), int(scale * 200), int(scale * 200)), pi / 2,
        pi - pi * 0.2)

    line(surface, COLOR_GRAY, (int(0), int(scale*190)) ,(int(scale*300), int(scale*180)), 1)

    if chirality == 'left':
        return surface
    if chirality == 'right':
        return pygame.transform.flip(surface, True, False)
    pass


screen.blit(draw_cat(0.2, 'right', 'orange'), (30, 420))
screen.blit(draw_ball(0.2, 'left'), (170, 420))
screen.blit(draw_cat(0.5, 'left', 'orange'), (300, 420))
screen.blit(draw_cat(0.4, 'right', 'gray'), (30, 520))

screen.blit(draw_ball(0.2, 'right'), (450, 550))
screen.blit(draw_ball(0.4, 'right'), (350, 610))
screen.blit(draw_cat(0.2, 'right', 'orange'), (450, 590))
screen.blit(draw_ball(0.7, 'left'), (50, 650))
screen.blit(draw_ball(0.2, 'left'), (50, 630))
screen.blit(draw_cat(0.2, 'right', 'gray'), (30, 720))
screen.blit(draw_cat(0.15, 'left', 'orange'), (350, 700))
screen.blit(draw_ball(0.3, 'right'), (450, 700))
screen.blit(draw_ball(0.2, 'left'), (350, 750))
screen.blit(draw_cat(0.15, 'left', 'gray'), (450, 780))

screen.blit(draw_window(0.6), (-100, 20))
screen.blit(draw_window(0.6), (150, 20))
screen.blit(draw_window(0.6), (400, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
picture = '8'
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
