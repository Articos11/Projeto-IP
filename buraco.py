import pygame
import configuracoes


class Hole(object):
    def __init__(self):
        self.x = configuracoes.largura - 300
        self.y = configuracoes.altura - 1025
        self.imagens = []
        for i in range(1, 8):
            imagem = pygame.image.load(f"Assets/Buraco_Negro/frame-{i}.png")
            imagem = pygame.transform.scale(imagem, (500,1500))
            self.imagens.append(imagem)
        self.index = 0
        self.imagem = self.imagens[self.index]
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        self.rect = self.imagem.get_rect()
        self.rect.center = (self.x + 175,self.y)
        self.contador = 0

    def update(self):
        duracao = 8
        self.contador += 1
    
        if self.contador >= duracao and self.index < len(self.imagens) - 1:
            self.contador = 0
            self.index += 1
            self.imagem = self.imagens[self.index]

        if self.index >= len(self.imagens) - 1 and self.contador >= duracao:
            self.contador = 0
            self.index = 0
            self.imagem = self.imagens[self.index]
        
    def draw(self,display):
        #pygame.draw.rect(display, (0, 255, 0), [self.x + 175, self.y, self.largura, self.altura])
        display.blit(self.imagem, (self.x,self.y))

bur = Hole()