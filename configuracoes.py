import pygame

altura = 600
largura = 800

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Into the void')
background = pygame.image.load("Assets/starbg.png").convert()
background = pygame.transform.scale(background, (largura, altura))
sprite_jogador = pygame.image.load("Assets/apontada_frente.png")
sprite_jogador = pygame.transform.scale(sprite_jogador, (100, 100))
asteroide = pygame.image.load("Assets/asteroide.png")
asteroide = pygame.transform.scale(asteroide, (80,80))
disparo_jogador = pygame.image.load("Assets/laser1.png")
disparo_jogador = pygame.transform.scale(disparo_jogador, (20,20))