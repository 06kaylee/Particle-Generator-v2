import pygame, sys, math, random
from pygame.locals import *
from spark import Spark

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Particle Generator')
screen = pygame.display.set_mode((500, 500), 0, 32)

sparks = []


while True:
    # Background 
    screen.fill((0,0,0))

    for i, spark in sorted(enumerate(sparks), reverse=True):
        spark.move(1)
        spark.draw(screen)
        # remove the spark if they have disappeared (size = 0)
        if not spark.alive:
            sparks.pop(i)

    # get the mouse position and set that position to the spark location
    mx, my = pygame.mouse.get_pos()

    # generate 10 sparks and add them to the sparks array
    for i in range(10):
        sparks.append(Spark([mx, my], math.radians(random.randint(0, 360)), random.randint(3, 6), (255, 255, 255), 2))

    # quit game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # updating
    pygame.display.update()
    clock.tick(60)