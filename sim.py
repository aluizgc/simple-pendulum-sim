import numpy as np 
import math as mt 
import pygame, sys

pygame.init()
pygame.display.set_caption('Simulação Pêndulo Simples')
tela = pygame.display.set_mode((500,500))

while True:
    tela.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    tempo = 0.02*pygame.time.get_ticks()
    g = 9.81
    l = 100
    a = (1/4)*mt.pi
    theta = a*np.sin(mt.sqrt(g/l)*tempo)
    x = l*np.cos(theta)
    y = l*np.sin(theta)

    pygame.draw.line(tela, (0,0,0), (250,250), (250+int(y), 250+int(x)))
    pygame.draw.circle(tela, (0,0,255), (250+int(y),250+int(x)), 10)
    pygame.display.flip()
