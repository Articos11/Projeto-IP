import pygame
import random
import configuracoes
import tela
import sons

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
        self.rany = random.randint(50,600)
        if tela.contagem_ast < sons.ast_prog[2][0]:
            self.x, self.y = self.ranPoint
        else:
            self.x = -30
            self.y = self.rany
        if self.x < configuracoes.largura // 2:
            self.xdirecao = 1
        else:
            if tela.contagem_ast < sons.ast_prog[2][0]:
                self.xdirecao = -1
            else:
                self.xdirecao = 1
        if self.y < configuracoes.altura // 2:
            if tela.contagem_ast < sons.ast_prog[2][0]:
                self.ydirecao = 1
            else:
                self.ydirecao = 0
        else :
            if tela.contagem_ast < sons.ast_prog[2][0]:
                self.ydirecao = -1
            else:
                self.ydirecao = 0
        self.xvelocidade = self.xdirecao * random.randrange(1,3)
        self.yvelocidade = self.ydirecao * random.randrange(1,3)

    def draw(self, display):
        #pygame.draw.rect(display, (0, 0, 255), [self.x, self.y, self.w, self.h])
        display.blit(self.imagem,(self.x, self.y))

    def checarForaTela(self):
        if self.x < -100 or self.x > configuracoes.largura + 100 or self.y > configuracoes.altura +100 or self.y < -100:
            return True
        
class Explosao(object):
    def __init__(self, x, y,categoria):
        self.categoria = categoria
        tamanho = 50*categoria
        self.imagem = configuracoes.explosao_ast
        self.imagem = pygame.transform.scale(self.imagem, (tamanho,tamanho))
        self.x = x
        self.y = y
        self.rect = self.imagem.get_rect()
        #self.rect.center = (x, y)
        self.contador = 0
        self.velocidade = 30
    
    def update(self):
        self.contador += 1
    
    def draw(self, display):
        display.blit(self.imagem,(self.x, self.y))