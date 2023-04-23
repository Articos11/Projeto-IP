# Comando para importar o pygame no programa.
import pygame
from pygame.locals import *

# É ativado a biblioteca de pygame usando este comando.
pygame.init()

# Aqui é usado o comando para o tamanho da janela do jogo, nesse caso usando uma resolução
# baixa de 800x600
largura = 800
altura = 600
win = pygame.display.set_mode((largura, altura))

# Aqui são colocadas coisas relacionadas ao display do jogo.
pygame.display.set_caption("Into the Void")
background = pygame.image.load("images/background_terra.jpg")
background = pygame.transform.scale(background, (largura, altura))
spaceship = pygame.image.load("images/Cinza.png")
spaceship = pygame.transform.scale(spaceship, (80, 80))
# O i servirá para controlar o local da imagem de fundo.
i = 0 


# Essas são as coordenadas atuais do jogador.
jogador_x = 130
jogador_y = 270

# Essas são as dimensões do objeto.
largura_jogador = 20
altura_jogador = 20

# Velocidade do objeto. 
vel = 10
clock = pygame.time.Clock()

# Controlador do pygame para manter o jogo rodando.
run = True

def jogador():
    win.blit(spaceship, (jogador_x, jogador_y))

while run:
    
    win.fill((0,0,0))
    win.blit(background, (i, 0))
    win.blit(background, (largura+i, 0))
    if (i ==- largura):
        win.blit(background, (largura+i, 0))
        i = 0
    i -= 5
    
    # Irá encerrar o loop do jogo. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keys é a chave para caso alguma tecla seja pressionada. 
    keys = pygame.key.get_pressed()

    # Com essas configurações, o jogador é impedido de se mover demais para a esquerda.
    if keys[pygame.K_UP] and jogador_y > 0:
        jogador_y -= vel
    
    # Com essas configurações, o jogador é impedido de se mover demais para a dirieta. 
    if keys[pygame.K_DOWN] and jogador_y < 600 - altura_jogador:
       jogador_y += vel

    if keys[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= vel
    
    if keys[pygame.K_RIGHT] and jogador_x < 300 - largura_jogador:
        jogador_x += vel

    # Isso manterá os frames em 55, impedindo que o jogo se comporte de maneiras estranhas em monitores com refresh rate maiores.
    clock.tick(55)
    jogador()

    pygame.display.update()

# Fecha a janela
pygame.quit()