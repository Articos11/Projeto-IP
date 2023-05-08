import pygame
import math
import configuracoes


class Jogador(object):
    def __init__(self):
        self.imagem = configuracoes.sprite_jogador
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        # Posição X do jogador.
        self.x = configuracoes.largura//2 - 50
        # Posição Y do jogador. 
        self.y = configuracoes.altura//2 - 50
        # Aqui serão gerados os controles de rotação da nave.
        # Alterar o valor do ângulo irá mudar a posição inicial da nave ao redor do próprio eixo.
        self.angulo = 0
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        # Rect é o indicador de colisão da nave. 
        self.rotacaoRect = self.imagem.get_rect()
        self.rotacaoRect.center = (self.x + 50, self.y + 50)
        # Aqui são criadas variáveis para controlar o centro 'gravitacional' da nave. Sua rotação, por assim dizer.
        self.cosseno = math.cos(math.radians(self.angulo))
        self.seno = math.sin(math.radians(self.angulo))
        self.frente = (self.x + 50 + self.cosseno * self.largura//2, self.y + 50 - self.seno * self.largura//2)
        self.visivel = True
        self.contador = 0


    def draw(self, display):
        #pygame.draw.rect(display, (0, 255, 0), [self.x, self.y, self.largura, self.altura])
        if 18 < self.contador < 36 or 54 < self.contador < 72 or self.visivel:
            display.blit(self.rotacao, self.rotacaoRect)

    def virarEsquerda(self):
        self.angulo += 3
        self.angulo = self.angulo%360
        player.calcular()


    def virarDireita(self):
        self.angulo -= 3
        self.angulo = self.angulo%360
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
        self.rotacaoRect.center = (self.x + 50, self.y + 50)
        self.cosseno = math.cos(math.radians(self.angulo))
        self.seno = math.sin(math.radians(self.angulo))
        self.frente = (self.x + 50 + self.cosseno * self.largura//2, self.y + 50 - self.seno * self.largura//2)

    def update(self):
        if not self.visivel:
            self.contador += 1

player = Jogador()