# São importados as bibliotecas e os scripts externos.
import pygame
import random
import asteroides
import jogador
import configuracoes
import projeteis

# É iniciado o pygame aqui. 
pygame.init()

# Controle de velocidade. 
clock = pygame.time.Clock()
FPS = 60
rodar = True

# Variavel de controle de mapa.
i = 0
vidas = 3
pontos = 0
l_nav_vida = [pygame.Rect(10 + i*30, 10, configuracoes.sprite_vidas.get_width(), configuracoes.sprite_vidas.get_height()) for i in range(vidas)]

# É criada uma função para que a tela seja 'refeita' a cada frame.
def tela():
    global i
    #Fonte e renderização dos pontos
    f_pontos = pygame.font.SysFont('arial', 20)
    parte_pontos = f_pontos.render(f'{str(pontos)}', 1, (255, 255, 255))
    f_gameover = pygame.font.SysFont('arial', 60)
    texto_g_o = f_gameover.render(f'GAMEOVER', 1, (255, 0, 0))
    f_tentar_nov = pygame.font.SysFont('arial', 40)
    tentar_nov = f_tentar_nov.render(f'Pressione Espaço para jogar de novo', 1, (255, 255, 255))
    #Background
    configuracoes.display.fill((0,0,0))
    configuracoes.display.blit(configuracoes.background, (i, 0))
    configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
    if (i ==- configuracoes.largura):
        configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
        i = 0
    i -= 2
    #Desenho dos cometas
    for a in cometas:
        a.draw(configuracoes.display)
    for d in tiros:
        d.desenhar_disparo(configuracoes.display)
        if d.checarForaTela():
            tiros.pop(tiros.index(d))
    #Blit das vidas e dos pontos
    for nave in l_nav_vida:
        configuracoes.display.blit(configuracoes.sprite_vidas, nave)
    if gameover: #Texto gameover e tentar novamente
        configuracoes.display.blit(texto_g_o, (configuracoes.largura//2-texto_g_o.get_width()//2, configuracoes.altura//3-texto_g_o.get_height()//3))
        configuracoes.display.blit(tentar_nov, (configuracoes.largura//2-tentar_nov.get_width()//2, configuracoes.altura//2-tentar_nov.get_height()//2))
    configuracoes.display.blit(parte_pontos, (25, 50))
    jogador.player.draw(configuracoes.display)
    pygame.display.update()


tiros = []
cometas = []
contagem_ast = 0
gameover = False

while rodar:

    clock.tick(FPS)
    contagem_ast += 1

    if not gameover:
        if contagem_ast % 75 == 0:
            ran = random.choice([1,1,1,2,2,3])
            cometas.append(asteroides.Asteroide(ran))
        # Aqui é como os disparos são chamados.
        for d in tiros:
            d.mover_disparo()
        
        for a in cometas:
            a.x += a.xvelocidade
            a.y += a.yvelocidade
                                #Checagem de colisão com a nave e diminuição das vidas
            if (jogador.player.x >= a.x and jogador.player.x <= a.x + a.w) or (jogador.player.x + jogador.player.largura >= a.x and jogador.player.x + jogador.player.largura <= a.x + a.w):
                if (jogador.player.y >= a.y and jogador.player.y <= a.y + a.h) or (jogador.player.y + jogador.player.altura >= a.y and jogador.player.y + jogador.player.altura <= a.y + a.h):
                    vidas -= 1
                    for v in l_nav_vida:
                        if l_nav_vida.index(v) == len(l_nav_vida) - 1:
                            l_nav_vida.pop(l_nav_vida.index(v))
                    cometas.pop(cometas.index(a))
                    break

            # Checagem de colisão com disparos.
            for d in tiros:
                # Irá checar se o disparo colide com a largura total do asteroide.
                if (d.x >= a.x and d.x <= a.x + a.w) or d.x + d.lar_disparo >= a.x and d.x + d.lar_disparo <= a.x + a.w:
                    # Se sim, irá checar em qual altura o disparo colidiu com o asteroide. 
                    if (d.y >= a.y and d.y <= a.y + a.h) or d.y + d.alt_disparo >= a.y and d.y + d.alt_disparo <= a.y + a.h:
                        # Aqui iremos dividir o asteroide em niveis diferentes.
                        if a.categoria == 3:
                            pontos += 200
                            novo_asteroide_1 = asteroides.Asteroide(2)
                            novo_asteroide_2 = asteroides.Asteroide(2)
                            novo_asteroide_1.x = a.x 
                            novo_asteroide_2.x = a.x
                            novo_asteroide_1.y = a.y
                            novo_asteroide_2.x = a.y
                            cometas.append(novo_asteroide_1)
                            cometas.append(novo_asteroide_2)
                        elif a.categoria == 2:
                            pontos += 100
                            novo_asteroide_1 = asteroides.Asteroide(1)
                            novo_asteroide_2 = asteroides.Asteroide(1)
                            novo_asteroide_1.x = a.x 
                            novo_asteroide_2.x = a.x
                            novo_asteroide_1.y = a.y
                            novo_asteroide_2.x = a.y
                            cometas.append(novo_asteroide_1)
                            cometas.append(novo_asteroide_2)
                        else:
                            pontos += 50

                        cometas.pop(cometas.index(a))
                        tiros.pop(tiros.index(d))
        if vidas <= 0:
            gameover = True

        # Aqui as teclas são pressionadas e podem ser seguradas para movimentos continuos.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            jogador.player.virarEsquerda()
        if keys[pygame.K_RIGHT]:
            jogador.player.virarDireita()
        if keys[pygame.K_UP]:
            jogador.player.moverFrente()
        if keys[pygame.K_DOWN]:
            jogador.player.moverTras()
        if keys[pygame.K_ESCAPE]:
            rodar = False

        # Esse bloco irá impedir que o jogador saia das dimensões da tela. 
        if jogador.player.x <= 35:
            jogador.player.x = 35
        if jogador.player.x >= 765:
            jogador.player.x = 765
        if jogador.player.y <= 30:
            jogador.player.y = 30
        if jogador.player.y >= 575:
            jogador.player.y = 575

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
        # Os disparos foram inseridos aqui para impedir que o jogador dispare infinitas vezes.  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    tiros.append(projeteis.Disparos())
                else:
                    #Esse bloco será a parte de game over, para voltar a jogar basta apertar a tecla "espaço"
                    gameover = False
                    vidas = 3
                    pontos = 0
                    l_nav_vida = [pygame.Rect(10 + i*30, 10, configuracoes.sprite_vidas.get_width(), configuracoes.sprite_vidas.get_height()) for i in range(vidas)]
                    cometas.clear()
    tela() 

pygame.quit()