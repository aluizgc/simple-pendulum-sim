import numpy as np 
import math as mt 
import pygame, sys
from funcSlider import slider 

pygame.init()
pygame.display.set_caption('Simulação Pêndulo Simples')
screen = pygame.display.set_mode((500,500))
g = 9.81
l = 100
a = (1/4)*mt.pi
while True:
    screen.fill((255,255,255))
    button = pygame.mouse.get_pressed()

#Sliders
    if button[0] != 0:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        l = x
    

# Controles 
    pygame.draw.rect(screen, (255,0,0),(l,5,10,25)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    time = 0.02*pygame.time.get_ticks()
    theta = a*np.sin(mt.sqrt(g/l)*time)
    x = l*np.cos(theta)
    y = l*np.sin(theta)

    
    pygame.draw.line(screen, (0,0,0), (250,250), (250+int(y), 250+int(x)))
    pygame.draw.circle(screen, (0,0,255), (250+int(y),250+int(x)), 10)
    pygame.display.flip()
