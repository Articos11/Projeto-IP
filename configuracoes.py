import pygame

altura = 600
largura = 800

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Into the void')
background = pygame.image.load("Assets/starbg.png").convert()
background = pygame.transform.scale(background, (largura, altura))
sprite_jogador = pygame.image.load("Assets/nave.png")
sprite_jogador = pygame.transform.scale(sprite_jogador, (100, 100))
asteroide_50 = pygame.image.load("Assets/asteroide_50.png")
asteroide_100 = pygame.image.load("Assets/asteroide_100.png")
asteroide_150 = pygame.image.load("Assets/asteroide_150.png")
disparo_jogador = pygame.image.load("Assets/laser1.png")
disparo_jogador = pygame.transform.scale(disparo_jogador, (20,20))
disparo_jogador_rect = disparo_jogador.get_rect()
disparo_jogador_rect.center = ((6,6))