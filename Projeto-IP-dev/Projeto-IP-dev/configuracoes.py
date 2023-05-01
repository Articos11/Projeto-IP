import pygame

altura = 650
largura = 1024

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Into the Void')
icone = pygame.image.load("Assets/Cinza.png")
pygame.display.set_icon(icone)
background = pygame.image.load("Assets/starbg.png").convert()
background = pygame.transform.scale(background, (largura, altura))
sprite_jogador = pygame.image.load("Assets/nave_espacial.png")
sprite_jogador = pygame.transform.scale(sprite_jogador, (100, 100))
sprite_vidas = pygame.image.load("Assets/apontada_frente.png")
sprite_vidas = pygame.transform.scale(sprite_vidas, (30, 30))
asteroide_50 = pygame.image.load("Assets/asteroide_50.png")
asteroide_100 = pygame.image.load("Assets/asteroide_100.png")
asteroide_150 = pygame.image.load("Assets/asteroide_150.png")
disparo_jogador = pygame.image.load("Assets/laser1.png")
disparo_jogador = pygame.transform.scale(disparo_jogador, (50,50))
raio = pygame.image.load("Assets/mult_disp.png")

