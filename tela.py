import pygame
import configuracoes
import jogador

tiros = []
cometas = []
multiplos_tiros = []
vidas_extras = []
contagem_ast = 0
gameover = False

# Variavel de controle de mapa.
i = 0

vidas = 3
pontos = 0
tiros_rapidos = False
multiplos_inicio = -1
l_nav_vida = [pygame.Rect(10 + i*30, 10, configuracoes.sprite_vidas.get_width(), configuracoes.sprite_vidas.get_height()) for i in range(vidas)]

# É criada uma função para que a tela seja 'refeita' a cada frame.
def tela():
    global i
    #Fonte e renderização dos pontos
    f_pontos = pygame.font.SysFont('arial black', 20)
    parte_pontos = f_pontos.render(f'{str(pontos)}', 1, (250, 253, 15))
    #Game Over
    f_gameover = pygame.font.SysFont('kabel ultra', 100)
    texto_g_o = f_gameover.render(f'GAMEOVER', 1, (153, 50, 204))
    f_tentar_nov = pygame.font.SysFont('arial', 40)
    tentar_nov = f_tentar_nov.render(f'Pressione Espaço para jogar de novo', 1, (255, 255, 255))
    sair = f_tentar_nov.render(f'ou Esc para sair', 1, (255, 255, 255))
    #Jogo pausado
    fonte_Jogo_p = pygame.font.SysFont('kabel ultra', 70)
    jogo_pausado = fonte_Jogo_p.render(f'Jogo Pausado', 1, (153, 50, 204))
    deseja_fazer = fonte_Jogo_p.render(f'O que deseja fazer?', 1, (153, 50, 204))

    #Background
    if configuracoes.start:
        configuracoes.display.fill((0,0,0))
        configuracoes.display.blit(configuracoes.background, (i, 0))
        configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
        if not configuracoes.pausado:
            if not gameover:   
                if (i ==- configuracoes.largura):
                    configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
                    i = 0
                i -= 2
                #Desenho dos objetos
                for a in cometas:
                    a.draw(configuracoes.display)
                    if a.checarForaTela():
                        cometas.pop(cometas.index(a))
                for d in tiros:
                    d.desenhar_disparo(configuracoes.display)
                    if d.checarForaTela():
                        tiros.pop(tiros.index(d))
                for t in multiplos_tiros:
                    t.draw(configuracoes.display)
                    if t.checarForaTela():
                        multiplos_tiros.pop(multiplos_tiros.index(t))
                for e in vidas_extras:
                    e.draw(configuracoes.display)
                    if e.checarForaTela():
                        vidas_extras.pop(vidas_extras.index(e))
                #barra de contagem de tempo que o jogador tera com o tiros rapidos
                if tiros_rapidos :
                    #quadrado preto
                    pygame.draw.rect(configuracoes.display, (0,0,0), [configuracoes.largura//2 -51, 19, 102, 22])
                    #barra que vai mudar com o tempo
                    pygame.draw.rect(configuracoes.display, (255,0,0), [configuracoes.largura//2 -50, 20, 100 - 100 * (contagem_ast-multiplos_inicio)/500, 20])
                #Blit das vidas e dos pontos
                jogador.player.draw(configuracoes.display)
            else: #Texto gameover e tentar novamente
                configuracoes.display.blit(texto_g_o, (configuracoes.largura//2-texto_g_o.get_width()//2, configuracoes.altura//3-texto_g_o.get_height()//3))
                configuracoes.display.blit(tentar_nov, (configuracoes.largura//2-tentar_nov.get_width()//2, configuracoes.altura//2-tentar_nov.get_height()//2))
                configuracoes.display.blit(sair, (configuracoes.largura//2-sair.get_width()//2, configuracoes.altura//2-sair.get_height()//2 + 50))
            
            configuracoes.display.blit(parte_pontos, (10, 50))
            for nave in l_nav_vida:
                configuracoes.display.blit(configuracoes.sprite_vidas, nave)
        else:
            configuracoes.display.blit(jogo_pausado, (configuracoes.largura//2-tentar_nov.get_width()/3.3, configuracoes.altura//10-tentar_nov.get_height()//2))
            configuracoes.display.blit(deseja_fazer, (configuracoes.largura//2-tentar_nov.get_width()/2.4, configuracoes.altura//4.5-tentar_nov.get_height()//2))
            configuracoes.botao_Resumir.desenhar_bot(configuracoes.display)
            configuracoes.botao_Menu.desenhar_bot(configuracoes.display)
            configuracoes.botao_Sair_pause.desenhar_bot(configuracoes.display)
            if configuracoes.botao_Resumir.clicado():
                configuracoes.botao_Resumir.desenhar_bot(configuracoes.display)
                configuracoes.pausado = False
            elif configuracoes.botao_Sair_pause.clicado():
                configuracoes.botao_Sair_pause.desenhar_bot(configuracoes.display)
                configuracoes.rodar = False
            elif configuracoes.botao_Menu.clicado():
                configuracoes.botao_Menu.desenhar_bot(configuracoes.display)
                configuracoes.start = False

        # Esse bloco irá impedir que o jogador saia das dimensões da tela. 
        if jogador.player.x <= 0:
            jogador.player.x = 0
        if jogador.player.x >= (configuracoes.largura-80):
            jogador.player.x = (configuracoes.largura-80)
        if jogador.player.y <= 0:
            jogador.player.y = 0
        if jogador.player.y >= (configuracoes.altura-80):
            jogador.player.y = (configuracoes.altura-80)
    else:
        configuracoes.display.fill((0,0,0))
        configuracoes.display.blit(configuracoes.background, (i, 0))
        configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
        if (i ==- configuracoes.largura):
            configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
            i = 0
        i -= 2
        #Desenho dos cometas
        for a in cometas:
            a.x += a.xvelocidade
            a.y += a.yvelocidade
            a.draw(configuracoes.display)
            if a.checarForaTela():
                cometas.pop(cometas.index(a))
        configuracoes.display.blit(configuracoes.logo, (configuracoes.largura//2-configuracoes.logo.get_width()//2.2, configuracoes.altura//4-configuracoes.logo.get_width()//2))
        configuracoes.botao_Jogar.desenhar_bot(configuracoes.display)
        configuracoes.botao_Sair_iniciar.desenhar_bot(configuracoes.display)
        
        if configuracoes.botao_Jogar.clicado():
            configuracoes.botao_Jogar.desenhar_bot(configuracoes.display)
            configuracoes.reset()
            configuracoes.start = True
            configuracoes.pausado = False
        if configuracoes.botao_Sair_iniciar.clicado():
            configuracoes.botao_Sair_iniciar.desenhar_bot(configuracoes.display)
            configuracoes.rodar = False

    pygame.display.update()