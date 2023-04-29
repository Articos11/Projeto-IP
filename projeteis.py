import pygame
import configuracoes
import jogador

class Disparos(object):
    def __init__(self):
        # Com isso, sempre irá ser pego a posição da 'ponta' da nave para os disparos. 
        self.apontar = jogador.player.frente
        self.x, self.y = self.apontar
        # Aqui é definido o tamanho do projétil. Lar = Largura. Alt = Altura. Aumentar os valores aumenta o tamanho do projetil. 
        self.imagem = configuracoes.disparo_jogador
        self.lar_disparo = 4
        self.alt_disparo = 4
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
        pygame.draw.rect(display, (255, 0, 0), [self.x, self.y, self.lar_disparo, self.alt_disparo])

    # Isso aqui deleta qualquer disparo fora da tela pra economizar memória.
    def checarForaTela(self):
        if self.x < -50 or self.x > configuracoes.largura or self.y > configuracoes.altura or self.y < -50:
            return True