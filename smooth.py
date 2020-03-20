import pygame
import random
import sys

from simulation import NBodySimulation

pygame.init()

screen = pygame.display.set_mode((640,480))

w = 640
h = 480
mid_x = w//2
mid_y = h//2

sim = NBodySimulation(w, h)
sim.create_body(m=20, x=mid_x, y=mid_y)
sim.create_body(m=10, x=mid_x+100, y=mid_y-100, vy=40, vx=-10)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

colors = [
    red,
    green,
    blue,
    darkBlue,
    black,
    pink
]

for state in sim.start():
    i = 0
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
    # erase the screen
    screen.fill(black)
    for body in state:
        x = int(body['x'])
        y = int(body['y'])
        m = int(body['m'])
        pygame.draw.circle(screen, colors[i], (x,y), m//2, 0)
        i += 1 % len(state)
    pygame.display.update()
