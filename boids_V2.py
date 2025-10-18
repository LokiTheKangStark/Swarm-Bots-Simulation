import pygame
import sys
from pygame import Vector2 as V2
import random
import numpy as np, math as m

pygame.init()

window_width = 820
window_height = 620
window = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()
framerate = 120

dt = 0.1 

nop = 69
particles = []
for i in range(nop):
    p = V2(x=random.randint(10,window_width-10), y=random.randint(10,window_height-10))
    particles.append(p)

def drawParticle(p, color):
    pygame.draw.circle(window, color, (p.x, p.y), 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill('Dark Blue')

    for i in range(nop):
        drawParticle(particles[i], "White")
        # particles[i]
    
    for i in range(nop):
        F = V2(0,0)
        for j in range(nop):
            if(i == j):continue
            ds = particles[j] - particles[i]
            mag = ds.length()
            print(f"mag = {mag}")
            if(mag < 50 and mag > 0):
                F += (-ds)/(mag*2)
                print(F)
        particles[i] += F

    pygame.display.update()
    clock.tick(framerate)