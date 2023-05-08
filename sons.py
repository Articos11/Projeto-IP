import pygame
from pygame import mixer
import configuracoes
mixer.init()
mixer.music.load("Assets/Musica/menu.wav")
mixer.music.set_volume(1)

def mudar_musica():
    if configuracoes.start:
        mixer.music.unload()
        mixer.music.load("Assets/Musica/theme.wav")
        mixer.music.play(0,0,0)
    elif not configuracoes.start:
        mixer.music.unload()
        mixer.music.load("Assets/Musica/menu.wav")
        mixer.music.play(-1,0,0)

s_tiro = pygame.mixer.Sound("Assets/Musica/blaster.wav")
mixer.Sound.set_volume(s_tiro, 0.3)
s_atributo_tiro = pygame.mixer.Sound("Assets/Musica/energise.wav")
s_atributo_vida = pygame.mixer.Sound("Assets/Musica/life.wav")
s_n_tiro = pygame.mixer.Sound("Assets/Musica/shutdown.wav")
s_bomba = pygame.mixer.Sound("Assets/Musica/seismic_charge.wav")
s_explosao = pygame.mixer.Sound("Assets/Musica/explosion.wav")
mixer.Sound.set_volume(s_explosao, 0.5)
s_menu = pygame.mixer.Sound("Assets/Musica/menu.wav")
s_derrota = pygame.mixer.Sound("Assets/Musica/defeat.wav")


#sincronia com a musica
ast_prog = [[11113,12980],[11304],[19319],[20160],[22446]]