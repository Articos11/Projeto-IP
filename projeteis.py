import pygame
import configuracoes
import jogador

class Disparos(object):
    def __init__(self):
        self.imagem = configuracoes.disparo_jogador
        # Com isso, sempre irá ser pego a posição da 'ponta' da nave para os disparos. 
        self.apontar = jogador.player.frente
        self.x, self.y = self.apontar
        self.angulo = jogador.player.angulo
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.lar_disparo = 4
        self.alt_disparo = 4
        self.rotacaoRect.center = (self.x - (self.lar_disparo//2), self.y - (self.alt_disparo//2))
        # Aqui é definido o tamanho do projétil. Lar = Largura. Alt = Altura. Aumentar os valores aumenta o tamanho do projetil. 
        self.c = jogador.player.cosseno
        self.s = jogador.player.seno
        # Aqui é definido a velocidade da bala. Para aumentar, aumenta o valor da multiplicação. Pra diminuir, só diminuir o valor. 
        self.velX = self.c * 20
        self.velY = self.s * 20

    def mover_disparo(self):
        self.x += self.velX
        self.y -= self.velY

    def desenhar_disparo(self, display):
        # A primeira tupla é um valor RGB. Os valores vão de 0 a 255. Alterar os valores irá mudar a cor do disparo. Contanto que não seja branco (255,255,255) ou preto (0,0,0), pode colocar qualquer um.
        #pygame.draw.rect(display, (255, 0, 0), [self.x, self.y, self.lar_disparo, self.alt_disparo])
        display.blit(self.rotacao,(self.x - 25, self.y - 25))

    # Isso aqui deleta qualquer disparo fora da tela pra economizar memória.
    def checarForaTela(self):
        if self.x < -50 or self.x > configuracoes.largura + 50 or self.y > configuracoes.altura +50 or self.y < -50:
            return True