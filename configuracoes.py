import pygame
import menu
import tela

#Configurações de tela
altura = 650
largura = 1024
display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Into the Void')
icone = pygame.image.load("Assets/Cinza.png")
pygame.display.set_icon(icone)
background = pygame.image.load("Assets/starbg.png").convert()
background = pygame.transform.scale(background, (largura, altura))

#Relacionados aos menus do jogo (Pause e Start)
logo = pygame.image.load("Assets/titulo_transparente.png").convert_alpha()
logo = pygame.transform.scale(logo, (350,350))
start = False
pausado = False
rodar = True

#Botões
    #Jogar
im_Jogar = pygame.image.load("Assets/Botoes/Botao_play.png").convert_alpha()
im_Jogar = pygame.transform.scale(im_Jogar, (140, 70))
im_Jogar_apert = pygame.image.load("Assets/Botoes/Botao_play_apertado.png").convert_alpha()
im_Jogar_apert = pygame.transform.scale(im_Jogar_apert, (140, 70))
botao_Jogar = menu.Botao(largura / 2, altura / 1.8, im_Jogar, 1, im_Jogar_apert)
    #Menu
im_Menu = pygame.image.load("Assets/Botoes/Botao_menu.png").convert_alpha()
im_Menu = pygame.transform.scale(im_Menu, (140, 70))
im_Menu_apert = pygame.image.load("Assets/Botoes/Botao_menu_apertado.png").convert_alpha()
im_Menu_apert = pygame.transform.scale(im_Menu_apert, (140, 70))
botao_Menu = menu.Botao(largura / 2, altura / 3, im_Menu, 1, im_Menu_apert)
    #Resumir
im_Resumir = pygame.image.load("Assets/Botoes/Botao_resumir.png").convert_alpha()
im_Resumir = pygame.transform.scale(im_Resumir, (140, 70))
im_Resumir_apert = pygame.image.load("Assets/Botoes/Botao_resumir_apertado.png").convert_alpha()
im_Resumir_apert = pygame.transform.scale(im_Resumir_apert, (140, 70))
botao_Resumir = menu.Botao(largura / 2, altura / 2, im_Resumir, 1, im_Resumir_apert)
    #Sair
        #Botão Sair quando esta pausado
im_Sair = pygame.image.load("Assets/Botoes/Botao_sair.png").convert_alpha()
im_Sair = pygame.transform.scale(im_Sair, (140, 70))
im_Sair_apert = pygame.image.load("Assets/Botoes/Botao_sair_apertado.png").convert_alpha()
im_Sair_apert = pygame.transform.scale(im_Sair_apert, (140, 70))
botao_Sair_pause = menu.Botao(largura / 2, altura / 1.5, im_Sair, 1, im_Sair_apert)
        #Botão Sair no menu inicial
botao_Sair_iniciar = menu.Botao(largura / 2, altura / 1.4, im_Sair, 1, im_Sair_apert)


#Sprites relacionadas ao Jogador e aos asteroides
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
explosao_ast = pygame.image.load("Assets/explosao_2.png")
raio_reverso = pygame.image.load("Assets/nenhum_disp.png")
raio_reverso = pygame.transform.scale(raio_reverso, (50,50))

def reset():
    tela.gameover = False
    tela.contagem_ast = 0
    tela.densidade_ast = 100
    tela.vidas = 3
    tela.pontos = 0
    tela.l_nav_vida = [pygame.Rect(10 + i*30, 10, sprite_vidas.get_width(), sprite_vidas.get_height()) for i in range(tela.vidas)]
    tela.cometas.clear()
    tela.tiros.clear()
    tela.multiplos_tiros.clear()
    tela.vidas_extras.clear()
    tela.explosoes.clear()
    tela.nenhum_tiro.clear()
    tela.tiros_rapidos = False