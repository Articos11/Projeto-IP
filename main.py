# São importados as bibliotecas e os scripts externos.
import pygame
import random
import tela
import menu
import projeteis
import atributo_tiro
import asteroides
import jogador
import configuracoes

# É iniciado o pygame aqui. 
pygame.init()

# Controle de velocidade. 
clock = pygame.time.Clock()
FPS = 60
rodar = True

while rodar:

    clock.tick(FPS)

    if not tela.gameover:
        if configuracoes.pausado:
            if configuracoes.botao_Voltar.desenhar_bot(configuracoes.display):
                configuracoes.pausado = False
            elif configuracoes.botao_Sair.desenhar_bot(configuracoes.display):
                rodar = False
        else:
            tela.contagem_ast += 1
            #aparecimento dos asteroides
            if tela.contagem_ast % 75 == 0:
                ran = random.choice([1,1,1,2,2,3])
                tela.cometas.append(asteroides.Asteroide(ran))
            #aparecimento do atributo de tiros multiplos
            if tela.contagem_ast % 1050 == 0:
                tela.multiplos_tiros.append(atributo_tiro.variavel_auxiliar)

            # Aqui é como os disparos são chamados.
            for d in tela.tiros:
                d.mover_disparo()
            
            for a in tela.cometas:
                a.x += a.xvelocidade
                a.y += a.yvelocidade
                                    #Checagem de colisão com a nave e diminuição das tela.vidas
                if (jogador.player.x >= a.x and jogador.player.x <= a.x + a.w) or (jogador.player.x + jogador.player.largura >= a.x and jogador.player.x + jogador.player.largura <= a.x + a.w):
                    if (jogador.player.y >= a.y and jogador.player.y <= a.y + a.h) or (jogador.player.y + jogador.player.altura >= a.y and jogador.player.y + jogador.player.altura <= a.y + a.h):
                        tela.vidas -= 1
                        for v in tela.l_nav_vida:
                            if tela.l_nav_vida.index(v) == len(tela.l_nav_vida) - 1:
                                tela.l_nav_vida.pop(tela.l_nav_vida.index(v))
                        tela.cometas.pop(tela.cometas.index(a))
                        break

                # Checagem de colisão com disparos.
                for d in tela.tiros :
                    # Irá checar se o disparo colide com a largura total do asteroide.
                    if (d.x >= a.x and d.x <= a.x + a.w) or d.x + d.lar_disparo >= a.x and d.x + d.lar_disparo <= a.x + a.w:
                        # Se sim, irá checar em qual altura o disparo colidiu com o asteroide. 
                        if (d.y >= a.y and d.y <= a.y + a.h) or d.y + d.alt_disparo >= a.y and d.y + d.alt_disparo <= a.y + a.h:
                            # Aqui iremos dividir o asteroide em niveis diferentes.
                            if a.categoria == 3:
                                tela.pontos += 200
                                novo_asteroide_1 = asteroides.Asteroide(2)
                                novo_asteroide_2 = asteroides.Asteroide(2)
                                novo_asteroide_1.x = a.x 
                                novo_asteroide_2.x = a.x
                                novo_asteroide_1.y = a.y
                                novo_asteroide_2.x = a.y
                                tela.cometas.append(novo_asteroide_1)
                                tela.cometas.append(novo_asteroide_2)
                            elif a.categoria == 2:
                                tela.pontos += 100
                                novo_asteroide_1 = asteroides.Asteroide(1)
                                novo_asteroide_2 = asteroides.Asteroide(1)
                                novo_asteroide_1.x = a.x 
                                novo_asteroide_2.x = a.x
                                novo_asteroide_1.y = a.y
                                novo_asteroide_2.x = a.y
                                tela.cometas.append(novo_asteroide_1)
                                tela.cometas.append(novo_asteroide_2)
                            else:
                                tela.pontos += 50

                            tela.cometas.pop(tela.cometas.index(a))
                            tela.tiros.pop(tela.tiros.index(d))
                            break 
            
                for t in tela.multiplos_tiros:
                    t.x += t.xvelocidade
                    t.y += t.yvelocidade
                    
                    for d in tela.tiros:
                        # Irá checar se o disparo colide com a largura total da imagem dos tela.tiros multiplos.
                        if (d.x >= t.x and d.x <= t.x + t.w) or d.x + d.lar_disparo >= t.x and d.x + d.lar_disparo <= t.x + t.w:
                            # Se sim, irá checar em qual altura o disparo colidiu com o objeto. 
                            if (d.y >= t.y and d.y <= t.y + t.h) or d.y + d.alt_disparo >= t.y and d.y + d.alt_disparo <= t.y + t.h:
                                tela.tiros_rapidos = True
                                tela.multiplos_tiros.pop(tela.multiplos_tiros.index(t))
                                tela.multiplos_inicio = tela.contagem_ast
                                tela.tiros.pop(tela.tiros.index(d))
                                break
            if tela.vidas <= 0:
                tela.gameover = True
            #vai verificar qnt tempo ja se passou desde que o tiro multiplo foi coletado
            if tela.multiplos_inicio != -1 :
                # vai ver se passou de 500 
                if tela.contagem_ast - tela.multiplos_inicio > 500:
                    tela.tiros_rapidos = False
                    tela.multiplos_inicio = -1

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

            if keys[pygame.K_SPACE]:
                if tela.tiros_rapidos:
                    tela.tiros.append(projeteis.Disparos())

            # Esse bloco irá impedir que o jogador saia das dimensões da tela. 
            if jogador.player.x <= 35:
                jogador.player.x = 35
            if jogador.player.x >= (configuracoes.largura - 55):
                jogador.player.x = (configuracoes.largura - 55)
            if jogador.player.y <= 30:
                jogador.player.y = 30
            if jogador.player.y >= (configuracoes.altura - 50):
                jogador.player.y = (configuracoes.altura - 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
            # Os disparos foram inseridos aqui para impedir que o jogador dispare infinitas vezes.  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not tela.gameover:
                        if not tela.tiros_rapidos:
                            tela.tiros.append(projeteis.Disparos())
                elif event.key == pygame.K_p:
                    configuracoes.pausado = True
                    #else:
                    #   rodar = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #Esse bloco será a parte de game over, para voltar a jogar basta apertar a tecla "espaço"
                    tela.gameover = False
                    #tela.contagem_ast = 0
                    tela.vidas = 3
                    tela.pontos = 0
                    tela.l_nav_vida = [pygame.Rect(10 + i*30, 10, configuracoes.sprite_vidas.get_width(), configuracoes.sprite_vidas.get_height()) for i in range(tela.vidas)]
                    tela.cometas.clear()
                elif event.key == pygame.K_ESCAPE:
                    rodar = False
    print(rodar)
    tela.tela()
pygame.quit()