# São importados as bibliotecas e os scripts externos.
import pygame
import math

# É iniciado o pygame aqui. 
pygame.init()

##################### CONFIGURAÇÕES JANELA #####################
altura = 600
largura = 800

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Into the void')
background = pygame.image.load("Assets/starbg.png").convert()
background = pygame.transform.scale(background, (largura, altura))
sprite_jogador = pygame.image.load("Assets/apontada_frente.png")
sprite_jogador = pygame.transform.scale(sprite_jogador, (100, 100))

# Controle de velocidade. 
clock = pygame.time.Clock()
FPS = 60
rodar = True


####################### CONTROLES JOGADOR #######################
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
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.frente = (self.x + self.cosseno * self.largura//2, self.y - self.seno * self.altura//2)

    def virarDireita(self):
        self.angulo -= 3
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.frente = (self.x + self.cosseno * self.largura//2, self.y - self.seno * self.altura//2)

    def moverFrente(self):
        self.x += self.cosseno * 6
        self.y -= self.seno * 6
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.frente = (self.x + self.cosseno * self.largura//2, self.y - self.seno * self.altura//2)

    def moverTras(self):
        self.x -= self.cosseno * 6
        self.y += self.seno * 6
        self.rotacao = pygame.transform.rotate(self.imagem, self.angulo)
        self.rotacaoRect = self.rotacao.get_rect()
        self.rotacaoRect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angulo + 90))
        self.seno = math.sin(math.radians(self.angulo + 90))
        self.frente = (self.x + self.cosseno * self.largura//2, self.y - self.seno * self.altura//2)


############################## DISPAROS ##############################
class Disparos(object):
    def __init__(self):
        # Com isso, sempre irá ser pego a posição da 'ponta' da nave para os disparos. 
        self.apontar = player.frente
        self.x, self.y = self.apontar
        # Aqui é definido o tamanho do projétil. Lar = Largura. Alt = Altura. Aumentar os valores aumenta o tamanho do projetil. 
        self.lar_disparo = 6
        self.alt_disparo = 6
        self.c = player.cosseno
        self.s = player.seno
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
        if self.x < -50 or self.x > largura or self.y > altura or self.y < -50:
            return True

############################# LOOP DO JOGO ##################################

# Variavel de controle de mapa. 
i = 0

# É criada uma função para que a tela seja 'refeita' a cada frame.
def tela():
    global i
    display.fill((0,0,0))
    display.blit(background, (i, 0))
    display.blit(background, (largura+i, 0))
    if (i ==- largura):
        display.blit(background, (largura+i, 0))
        i = 0
    i -= 5

    for d in disparo_jogador:
        d.desenhar_disparo(display)
        if d.checarForaTela():
            disparo_jogador.pop(disparo_jogador.index(d))

    player.draw(display)
    pygame.display.update()

player = Jogador()
disparo_jogador = []

gameover = False
while rodar:

    clock.tick(FPS)

    if not gameover:
        # Aqui é como os disparos são chamados. 
        for d in disparo_jogador:
            d.mover_disparo()
        
        # Aqui as teclas são pressionadas e podem ser seguradas para movimentos continuos.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.virarEsquerda()
        if keys[pygame.K_RIGHT]:
            player.virarDireita()
        if keys[pygame.K_UP]:
            player.moverFrente()
        if keys[pygame.K_DOWN]:
            player.moverTras()

        # Esse bloco irá impedir que o jogador saia das dimensões da tela. 
        if player.x <= 35:
            player.x = 35
        if player.x >= 765:
            player.x = 765
        if player.y <= 30:
            player.y = 30
        if player.y >= 575:
            player.y = 575

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
        # Os disparos foram inseridos aqui para impedir que o jogador dispare infinitas vezes.  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    disparo_jogador.append(Disparos())

    tela()    

pygame.quit()