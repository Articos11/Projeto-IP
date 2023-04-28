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

############################# LOOP DO JOGO ##################################

# Variavel de controle de mapa.
i = 0

# É criada uma função para que a tela seja 'refeita' a cada frame.
def tela():
    global i
    configuracoes.display.fill((0,0,0))
    configuracoes.display.blit(configuracoes.background, (i, 0))
    configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
    if (i ==- configuracoes.largura):
        configuracoes.display.blit(configuracoes.background, (configuracoes.largura+i, 0))
        i = 0
    i -= 1
    for a in cometas:
        a.draw(configuracoes.display)
    for d in tiros:
        d.desenhar_disparo(configuracoes.display)
        if d.checarForaTela():
            tiros.pop(tiros.index(d))

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
        if contagem_ast % 25 == 0:
            ran = random.choice([1,1,2,2,2,3])
            cometas.append(asteroides.Asteroide(ran))
        # Aqui é como os disparos são chamados.
        for d in tiros:
            d.mover_disparo()
        
        for a in cometas:
            a.x += a.xvelocidade
            a.y += a.yvelocidade

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
    tela() 

pygame.quit()