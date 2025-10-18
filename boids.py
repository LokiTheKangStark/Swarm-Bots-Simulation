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
framerate = 60

dt = 0.1
class Particle:
    def __init__(self,id):
        self.id = id
        self.pos = V2(x=random.randint(0,window_width),y=random.randint(0,window_height))
        self.vel = V2(x=0,y=0)
        self.acc = V2(x=0,y=0)
    def drawParticle(self):
        pygame.draw.circle(window,"White",(self.pos.x, self.pos.y), 10)

nop = 25
particles = []
max_vel = 10
for i in range(nop):
    p = Particle(i+1) 
    particles.append(p)

particles_array = np.array(particles)

i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill('Blue')

    for p in particles_array:
        p.pos += p.vel*dt
        p.vel += p.acc*dt
        if(p.vel.length() > max_vel):
            p.vel = V2(0,0)
        p.drawParticle()

        #Boundary Conditions
        if(p.pos.x > window_width):
            p.pos.x = 0
        elif(p.pos.x<0):
            p.pos.x = window_width-1
        if(p.pos.y > window_height):
            p.pos.y = 0
        elif(p.pos.y<0):
            p.pos.y = window_height-1
    
    #Separation Conditions
    for i in range(nop):
        F = V2(0,0)
        for j in range(i,nop):
            if i == j: continue
            displacement_vector = particles_array[i].pos - particles_array[j].pos
            mod = displacement_vector.length()
            if(mod < 50 and mod>0):
                # F += V2(particles_array[i].pos/mod, particles_array[j].pos/mod)
                F += displacement_vector/(mod**1.5)
        particles_array[i].acc+=F

    pygame.display.update()
    clock.tick(framerate)