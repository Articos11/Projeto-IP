#import pygame
import random
import configuracoes

class Asteroide(object) :
    def __init__(self, categoria):
        self.categoria = categoria
        if self.categoria == 1:
            self.imagem = configuracoes.asteroide_50
        elif self.categoria == 2:
            self.imagem = configuracoes.asteroide_100
        else:
            self.imagem = configuracoes.asteroide_150
        self.w = 50*categoria
        self.h = 50*categoria
        self.ranPoint = random.choice([(random.randrange(0, configuracoes.largura-self.w), random.choice([-1 * self.h - 5, configuracoes.altura+5])),(random.choice([-1*self.w - 5, configuracoes.largura+5]), random.randrange(0, configuracoes.altura-self.h))])
        self.x, self.y = self.ranPoint
        if self.x < configuracoes.largura // 2:
            self.xdirecao = 1
        else :
            self.xdirecao = -1
        if self.y < configuracoes.altura // 2:
            self.ydirecao = 1
        else :
            self.ydirecao = -1
        self.xvelocidade = self.xdirecao * random.randrange(1,3)
        self.yvelocidade = self.ydirecao * random.randrange(1,3)

    def draw(self, janela):
        #pygame.draw.rect(janela, (0, 0, 255), [self.x, self.y, self.w, self.h])
        janela.blit(self.imagem,(self.x, self.y))

    def checarForaTela(self):
        if self.x < -50 or self.x > configuracoes.largura + 50 or self.y > configuracoes.altura +50 or self.y < -50:
            return True