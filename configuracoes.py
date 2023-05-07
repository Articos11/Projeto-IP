import pygame
import menu
import tela

altura = 650
largura = 1024

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Into the Void')
icone = pygame.image.load("Assets/Cinza.png")
pygame.display.set_icon(icone)

im_Voltar = pygame.image.load("Assets/Bot_voltar.png").convert_alpha()
im_Voltar = pygame.transform.scale(im_Voltar, (140, 70))
botao_Voltar = menu.Botao(largura / 2, altura / 3, im_Voltar, 1)
im_Sair = pygame.image.load("Assets/Bot_sair.png").convert_alpha()
botao_Sair = menu.Botao(largura / 2, altura / 2, im_Sair, 1)

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
raio = pygame.transform.scale(raio, (50,50))
extra_vida = pygame.image.load("Assets/vidas.png")
extra_vida = pygame.transform.scale(extra_vida, (50,50))

pausado = False

def reset():
    tela.gameover = False
    tela.contagem_ast = 0
    tela.vidas = 3
    tela.pontos = 0
    tela.l_nav_vida = [pygame.Rect(10 + i*30, 10, sprite_vidas.get_width(), sprite_vidas.get_height()) for i in range(tela.vidas)]
    tela.cometas.clear()
    tela.tiros.clear()
    tela.multiplos_tiros.clear()
    tela.vidas_extras.clear()
    tela.tiros_rapidos = False