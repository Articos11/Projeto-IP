import pygame
import configuracoes
class Botao():
    def __init__(self, x, y, im_botao, escala_bot):
        largura_bot = im_botao.get_width()
        altura_bot = im_botao.get_height()
        self.im_botao = pygame.transform.scale(im_botao, (int(largura_bot * escala_bot), int(altura_bot * escala_bot)))
        self.im_bot_rect = self.im_botao.get_rect()
        self.im_bot_rect.midtop = (x, y)
        self.clicou = False

    def desenhar_bot(self, superficie):        
        acao = False
        pos_mouse = pygame.mouse.get_pos()

        if not self.clicou and self.im_bot_rect.collidepoint(pos_mouse) and pygame.mouse.get_pressed()[0]:
            self.clicou = True
            acao = True
        elif self.clicou and not pygame.mouse.get_pressed()[0]:
            self.clicou = False

        superficie.blit(self.im_botao, (self.im_bot_rect.x, self.im_bot_rect.y))

        if self.clicou:
            acao = True

        return acao