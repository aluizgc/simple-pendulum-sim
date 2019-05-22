# Importando pacotes
import numpy as np 
import math as mt 
import pygame, sys

# Inicializando pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption('Simulação de Pêndulo Simples')
screen = pygame.display.set_mode((500,500))

# Definição dos valores iniciais das variáveis 
g = 9.81 # gravidade
l = 100 # comprimento da corda (em cm)
a = 100 # coeficiente da amplitude 

# Definição da função slider para controle das variáveis
def slider(xmin,xmax,yposi,yposf,button,b):
    if button[0]!=0:
        pos = pygame.mouse.get_pos()
        xc = pos[0]
        yc = pos[1]
        if (xc < b-xmin) or (xc >b+xmax):
            pass
        if (yc>yposi and yc<yposf):
            if xc<xmin:
                xc = xmin   
            if xc>xmax:
                xc = xmax
            return(xc)
        else:
            return(b)
    if button[0] == 0:
        xc = b   
        return(xc)
        
# loop principal do pygame
while True:
    
    A = (a/100)*mt.pi # Amplitude
    screen.fill((255,255,255))
    amplitude = font.render(('Amplitude: {0:.2f}'.format(A)), True, (13,134,0))
    screen.blit(amplitude, (270,15))
    comprimento = font.render(('Comprimento: {} cm'.format(l)), True, (255,0,0))
    screen.blit(comprimento, (270,50))
    button = pygame.mouse.get_pressed()

# Sliders para L
    lpos = slider(1,230,50,75,button,l)
    l = lpos
    pygame.draw.line(screen, (235,235,235), (0,62), (230, 62))
    pygame.draw.rect(screen, (255,0,0),(l,50,8,25))

# Slider para A
    Apos = slider(0,100,10,35,button,a)
    a = Apos
    pygame.draw.line(screen, (235,235,235), (0,22), (100, 22))
    pygame.draw.rect(screen,(13,134,0),(a,10,8,25))

# Controles 
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    # Tempo e funções de posição da massa
    time = 0.02*pygame.time.get_ticks()
    theta = A*np.sin(mt.sqrt(g/l)*time)
    x = l*np.cos(theta)
    y = l*np.sin(theta)
    # Desenhando o pêndulo e atualizando o frame 
    pygame.draw.line(screen, (0,0,0), (250,250), (250+int(y), 250+int(x)))
    pygame.draw.circle(screen, (0,0,255), (250+int(y),250+int(x)), 10)
    pygame.display.flip()