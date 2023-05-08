# São importados as bibliotecas e os scripts externos.
import pygame
import random
import tela
import projeteis
import atributo_tiro
import asteroides
import jogador
import configuracoes
import colisoes
import atributo_vida
import sons
import buraco

# É iniciado o pygame aqui. 
pygame.init()

# Controle de velocidade. 
clock = pygame.time.Clock()
FPS = 60
sons.mixer.music.play(-1)

while configuracoes.rodar:

    clock.tick(FPS)

    if not tela.gameover and configuracoes.start:
        if not configuracoes.pausado:
            tela.contagem_ast += 1
            if tela.contagem_ast > sons.ast_prog[0][1]:
                tela.densidade_ast = 100
            if tela.densidade_ast > 30 and tela.contagem_ast % 150 == 0:
                tela.densidade_ast -= 1
            #aparecimento dos asteroides 
            if tela.contagem_ast % tela.densidade_ast == 0:
                if tela.contagem_ast <= sons.ast_prog[0][0] or tela.contagem_ast > sons.ast_prog[0][1]:
                    ran = random.choice([1,1,1,2,2,3])
                    tela.cometas.append(asteroides.Asteroide(ran))
                elif sons.ast_prog[1][0] < tela.contagem_ast < sons.ast_prog[2][0]:
                    tela.densidade_ast = 20
                    ran = random.choice([1,1,1,2,2,3])
                    tela.cometas.append(asteroides.Asteroide(ran))
                
            #aparecimento do atributo de tiros multiplos
            if tela.contagem_ast % 6234 == 0 and tela.contagem_ast >= sons.ast_prog[1][0]:
                tela.multiplos_tiros.append(atributo_tiro.Infinitos(configuracoes.raio))
            if tela.contagem_ast % 2221 == 0:
                tela.nenhum_tiro.append(atributo_tiro.Infinitos(configuracoes.raio_reverso))
            if tela.contagem_ast % 5000 == 0 and tela.vidas < 3:
                tela.vidas_extras.append(atributo_vida.Vida())

            if tela.contagem_ast > sons.ast_prog[3][0]:
                colisoes.c_buraco(buraco.bur,jogador.player)

            # Aqui é como os projeteis são chamados.
            for d in tela.tiros:
                d.mover_disparo()
            
            for a in tela.cometas:
                a.x += a.xvelocidade
                a.y += a.yvelocidade
                eixo_x = a.x
                eixo_y = a.y
                #Checagem de colisão com a nave e diminuição das vidas
                if jogador.player.visivel:
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
            
            for n in tela.nenhum_tiro:
                n.x += n.xvelocidade
                n.y += n.yvelocidade
                if colisoes.atributo_t_reverso(n,jogador.player):
                    break

            for e in tela.vidas_extras:
                e.x += e.xvelocidade
                e.y += e.yvelocidade
                if colisoes.atributo_vida(e,jogador.player):
                    tela.l_nav_vida = l_nav_vida = [pygame.Rect(10 + i*30, 10, configuracoes.sprite_vidas.get_width(), configuracoes.sprite_vidas.get_height()) for i in range(tela.vidas)]
                    break

            if tela.vidas <= 0:
                tela.gameover = True
                sons.s_derrota.play()
            #vai verificar qnt tempo ja se passou desde que o tiro multiplo foi coletado
            if tela.multiplos_inicio != -1 :
                # vai ver se passou de 500 
                if tela.contagem_ast - tela.multiplos_inicio > 500:
                    tela.tiros_rapidos = False
                    tela.zero_tiros = False
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
                    if tela.contagem_ast % 2 == 0:
                        tela.tiros.append(projeteis.Disparos())
                        sons.s_tiro.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                configuracoes.rodar = False
            # Os disparos foram inseridos aqui para impedir que o jogador dispare infinitas vezes.  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not tela.gameover:
                        if not tela.tiros_rapidos and not tela.zero_tiros:
                            tela.tiros.append(projeteis.Disparos())
                            sons.s_tiro.play()
                elif event.key == pygame.K_p:
                    if configuracoes.pausado:
                        sons.mixer.music.unpause()        
                        configuracoes.pausado = False
                    else:
                        sons.mixer.music.pause()
                        configuracoes.pausado = True
            
    else:
        if tela.gameover:
            sons.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    configuracoes.rodar = False
                    
        elif not configuracoes.start:
            tela.contagem_ast += 1
            #aparecimento dos asteroides
            if tela.contagem_ast % 75 == 0:
                ran = random.choice([1,1,1,2,2,3])
                tela.cometas.append(asteroides.Asteroide(ran))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    configuracoes.rodar = False

    tela.tela()
    #print(jogador.player.visivel)
pygame.quit()