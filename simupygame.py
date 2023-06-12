#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:50:57 2023

@author: aboroa
"""

import pygame
import sys

pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir la pantalla
size = (1800, 200)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Movimiento Rectilíneo Uniforme Acelerado")

# Definir variables
x = 0
y = 0
velocity = 0
acceleration = 0.1

# Definir reloj
clock = pygame.time.Clock()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Actualizar la velocidad y la posición
    velocity += acceleration
    x += velocity

    # Dibujar la pantalla
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [x, y, 50, 50])

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar 60 milisegundos
    clock.tick(60)
