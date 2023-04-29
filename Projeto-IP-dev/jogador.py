import pygame
import math
import configuracoes


class Jogador(object):
    def __init__(self):
        self.imagem = configuracoes.sprite_jogador
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        # Posição X do jogador.
        self.x = configuracoes.largura//2
        # Posição Y do jogador. 
        self.y = configuracoes.altura//2
        # Aqui serão gerados os controles de rotação da nave.
        # Alterar o valor do ângulo irá mudar a posição inicial da nave ao redor do próprio eixo.
        self.angulo = 270
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        # Rect é o indicador de colisão da nave. 
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        # Aqui são criadas variáveis para controlar o centro 'gravitacional' da nave. Sua rotação, por assim dizer.
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.frente = (self.x + self.cosseno * self.largura//2, self.y - self.seno * self.altura//2) 


    def draw(self, display):
        display.blit(self.rotacao, self.rotacaoRect)

    def virarEsquerda(self):
        self.angulo += 3
        player.calcular()


    def virarDireita(self):
        self.angulo -= 3
        player.calcular()


    def moverFrente(self):
        self.x += self.cosseno * 6
        self.y -= self.seno * 6
        player.calcular()

    def moverTras(self):
        self.x -= self.cosseno * 6
        self.y += self.seno * 6
        player.calcular()

    def calcular(self):
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.frente = (self.x + self.cosseno * self.largura//2, self.y - self.seno * self.altura//2)

player = Jogador()