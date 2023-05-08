import configuracoes
import random

class Infinitos(object):
    def __init__(self):
        self.img = configuracoes.raio
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        #para que o atributo venha de lugares aleatorios 
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
        self.xvelocidade = self.xdirecao
        self.yvelocidade = self.ydirecao

    def draw(self, janela):
        #pygame.draw.rect(janela, (255, 0, 0), [self.x, self.y, self.w, self.h])
        janela.blit(self.img,(self.x, self.y))

    def checarForaTela(self):
        if self.x < -100 or self.x > configuracoes.largura + 100 or self.y > configuracoes.altura + 100 or self.y < -100:
            return True