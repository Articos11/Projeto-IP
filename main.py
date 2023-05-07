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
import colisoes
import atributo_vida

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
            if tela.contagem_ast % 1800 == 0:
                tela.multiplos_tiros.append(atributo_tiro.Infinitos())
            if tela.contagem_ast % 2800 == 0 and tela.vidas < 3:
                tela.vidas_extras.append(atributo_vida.Vida())

            # Aqui é como os projeteis são chamados.
            for d in tela.tiros:
                d.mover_disparo()
            
            for a in tela.cometas:
                a.x += a.xvelocidade
                a.y += a.yvelocidade
                #Checagem de colisão com a nave e diminuição das vidas
                if colisoes.nave_ast(jogador.player,a):
                    break
                # Checagem de colisão com disparos.
                for d in tela.tiros :
                    if colisoes.projetil_ast(d,a):
                        break
            
            for t in tela.multiplos_tiros:
                t.x += t.xvelocidade
                t.y += t.yvelocidade
                if colisoes.atributo_tiro(t,jogador.player):
                    break

            for e in tela.vidas_extras:
                e.x += e.xvelocidade
                e.y += e.yvelocidade
                if colisoes.atributo_vida(e,jogador.player):
                    tela.l_nav_vida = l_nav_vida = [pygame.Rect(10 + i*30, 10, configuracoes.sprite_vidas.get_width(), configuracoes.sprite_vidas.get_height()) for i in range(tela.vidas)]
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
                    if configuracoes.pausado:
                        configuracoes.pausado = False
                    else:
                        configuracoes.pausado = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #Essa função será a parte de game over, para voltar a jogar basta apertar a tecla "espaço"
                    configuracoes.reset()
                elif event.key == pygame.K_ESCAPE:
                    rodar = False
    tela.tela()
    #print(tela.vidas_extras, tela.contagem_ast)
pygame.quit()