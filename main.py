# São importados as bibliotecas e os scripts externos.
import pygame
import math

# É iniciado o pygame aqui. 
pygame.init()

############################## CONFIGURAÇÕES JANELA ######################### 
altura = 600
largura = 800

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Into the void')
background = pygame.image.load("Assets/starbg.png").convert()
background = pygame.transform.scale(background, (largura, altura))
sprite_jogador = pygame.image.load("Assets/apontada_frente.png")
sprite_jogador = pygame.transform.scale(sprite_jogador, (80, 80))
# Variavel de controle de mapa. 
i = 0

# Controle de velocidade. 
clock = pygame.time.Clock()
FPS = 60
rodar = True


####################### CONTROLES JOGADOR ###########################
class Jogador(object):
    def __init__(self):
        self.imagem = sprite_jogador
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        # Posição X do jogador.
        self.x = largura//2
        # Posição Y do jogador. 
        self.y = altura//2
        # Aqui serão gerados os controles de rotação da nave. 
        self.angulo = 0
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        # Rect é o indicador de colisão da nave. 
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        # Aqui são criadas variáveis para controlar o centro 'gravitacional' da nave. Sua rotação, por assim dizer.
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.frente = (self.x + self.cosseno * self.largura//2, self.y - self.seno * self.altura//2) 


    def draw(self, display):
        # display.blit(self.imagem, [self.x, self.y, self.largura, self.altura])
        display.blit(self.rotacao, self.rotacaoRect)

    def virarEsquerda(self):
        self.angulo += 3
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.head = (self.x + self.cosseno + self.largura//2, self.y + self.seno + self.altura//2)

    def virarDireita(self):
        self.angulo -= 3
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.head = (self.x + self.cosseno + self.largura//2, self.y + self.seno + self.altura//2)

    def moverFrente(self):
        self.x += self.cosseno * 6
        self.y -= self.seno * 6
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.head = (self.x + self.cosseno + self.largura//2, self.y + self.seno + self.altura//2)

    def moverTras(self):
        self.x -= self.cosseno * 6
        self.y += self.seno * 6
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.head = (self.x + self.cosseno + self.largura//2, self.y + self.seno + self.altura//2)

############################# LOOP DO JOGO ##################################

# É criada uma função para que a tela seja 'refeita' a cada frame.
def tela():
    global i
    display.fill((0,0,0))
    display.blit(background, (i, 0))
    display.blit(background, (largura+i, 0))
    if (i ==- largura):
        display.blit(background, (largura+i, 0))
        i = 0
    i -= 50

    player.draw(display)

player = Jogador()

gameover = False
while rodar:

    tela()

    clock.tick(FPS)

    if not gameover:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.virarEsquerda()
        if keys[pygame.K_RIGHT]:
            player.virarDireita()
        if keys[pygame.K_UP]:
            player.moverFrente()
        if keys[pygame.K_DOWN]:
            player.moverTras()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False

    pygame.display.update()

pygame.quit()