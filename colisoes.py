import tela
import sons
import asteroides
import jogador
def nave_ast(nave,ast):
    categoria = ast.categoria
    if (nave.x >= ast.x and nave.x <= ast.x + ast.w) or (nave.x + nave.largura >= ast.x and nave.x + nave.largura <= ast.x + ast.w):
        if (nave.y >= ast.y and nave.y <= ast.y + ast.h) or (nave.y + nave.altura >= ast.y and nave.y + nave.altura <= ast.y + ast.h):
            tela.vidas -= 1
            jogador.player.visivel = False
            for v in tela.l_nav_vida:
                if tela.l_nav_vida.index(v) == len(tela.l_nav_vida) - 1:
                    tela.l_nav_vida.pop(tela.l_nav_vida.index(v))
            tela.explosoes.append(asteroides.Explosao(ast.x,ast.y,categoria))
            tela.cometas.pop(tela.cometas.index(ast))
            sons.s_explosao.play()
            return True

def projetil_ast(projetil,ast):
    categoria = ast.categoria
    # Irá checar se o disparo colide com a largura total do asteroide.
    if (projetil.x >= ast.x and projetil.x <= ast.x + ast.w) or projetil.x + projetil.lar_disparo >= ast.x and projetil.x + projetil.lar_disparo <= ast.x + ast.w:
        # Se sim, irá checar em qual altura o disparo colidiu com o asteroide. 
        if (projetil.y >= ast.y and projetil.y <= ast.y + ast.h) or projetil.y + projetil.alt_disparo >= ast.y and projetil.y + projetil.alt_disparo <= ast.y + ast.h:
            # Aqui iremos dividir o asteroide em niveis diferentes.
            tela.pontos += 50*ast.categoria
            tela.explosoes.append(asteroides.Explosao(ast.x,ast.y,categoria))
            tela.cometas.pop(tela.cometas.index(ast))
            tela.tiros.pop(tela.tiros.index(projetil))
            sons.s_explosao.play()
            return True

def atributo_tiro(atributo,nave):
    for d in tela.tiros:
        # Irá checar se o disparo colide com a largura total da imagem dos tiros multiplos.
        if (d.x >= atributo.x and d.x <= atributo.x + atributo.w) or d.x + d.lar_disparo >= atributo.x and d.x + d.lar_disparo <= atributo.x + atributo.w:
            # Se sim, irá checar em qual altura o disparo colidiu com o objeto. 
            if (d.y >= atributo.y and d.y <= atributo.y + atributo.h) or d.y + d.alt_disparo >= atributo.y and d.y + d.alt_disparo <= atributo.y + atributo.h:
                tela.tiros_rapidos = True
                tela.multiplos_tiros.pop(tela.multiplos_tiros.index(atributo))
                tela.multiplos_inicio = tela.contagem_ast
                tela.tiros.pop(tela.tiros.index(d))
                sons.s_atributo_tiro.play()
                return True
    if (nave.x >= atributo.x and nave.x <= atributo.x + atributo.w) or (nave.x + nave.largura >= atributo.x and nave.x + nave.largura <= atributo.x + atributo.w):
        if (nave.y >= atributo.y and nave.y <= atributo.y + atributo.h) or (nave.y + nave.altura >= atributo.y and nave.y + nave.altura <= atributo.y + atributo.h):
            tela.tiros_rapidos = True
            tela.multiplos_tiros.pop(tela.multiplos_tiros.index(atributo))
            tela.multiplos_inicio = tela.contagem_ast
            sons.s_atributo_tiro.play()
            return True
        
def atributo_t_reverso(atributo,nave):
    for d in tela.tiros:
        # Irá checar se o disparo colide com a largura total da imagem dos tiros multiplos.
        if (d.x >= atributo.x and d.x <= atributo.x + atributo.w) or d.x + d.lar_disparo >= atributo.x and d.x + d.lar_disparo <= atributo.x + atributo.w:
            # Se sim, irá checar em qual altura o disparo colidiu com o objeto. 
            if (d.y >= atributo.y and d.y <= atributo.y + atributo.h) or d.y + d.alt_disparo >= atributo.y and d.y + d.alt_disparo <= atributo.y + atributo.h:
                tela.zero_tiros = True
                tela.nenhum_tiro.pop(tela.nenhum_tiro.index(atributo))
                tela.multiplos_inicio = tela.contagem_ast
                tela.tiros.pop(tela.tiros.index(d))
                sons.s_n_tiro.play()
                return True
    if (nave.x >= atributo.x and nave.x <= atributo.x + atributo.w) or (nave.x + nave.largura >= atributo.x and nave.x + nave.largura <= atributo.x + atributo.w):
        if (nave.y >= atributo.y and nave.y <= atributo.y + atributo.h) or (nave.y + nave.altura >= atributo.y and nave.y + nave.altura <= atributo.y + atributo.h):
            tela.zero_tiros = True
            tela.nenhum_tiro.pop(tela.nenhum_tiro.index(atributo))
            tela.multiplos_inicio = tela.contagem_ast
            sons.s_n_tiro.play()
            return True
        
def atributo_vida(atributo,nave):
    for d in tela.tiros:
        # Irá checar se o disparo colide com a largura total da imagem da vida extra.
        if (d.x >= atributo.x and d.x <= atributo.x + atributo.w) or d.x + d.lar_disparo >= atributo.x and d.x + d.lar_disparo <= atributo.x + atributo.w:
            # Se sim, irá checar em qual altura o disparo colidiu com o objeto. 
            if (d.y >= atributo.y and d.y <= atributo.y + atributo.h) or d.y + d.alt_disparo >= atributo.y and d.y + d.alt_disparo <= atributo.y + atributo.h:
                tela.vidas_extras.pop(tela.vidas_extras.index(atributo))
                tela.tiros.pop(tela.tiros.index(d))
                tela.vidas += 1
                sons.s_atributo_vida.play()
                return True
    if (nave.x >= atributo.x and nave.x <= atributo.x + atributo.w) or (nave.x + nave.largura >= atributo.x and nave.x + nave.largura <= atributo.x + atributo.w):
        if (nave.y >= atributo.y and nave.y <= atributo.y + atributo.h) or (nave.y + nave.altura >= atributo.y and nave.y + nave.altura <= atributo.y + atributo.h):
            tela.vidas_extras.pop(tela.vidas_extras.index(atributo))
            tela.vidas += 1
            sons.s_atributo_vida.play()
            return True
        
def c_buraco(buraco,nave):
    for d in tela.tiros:
        # Irá checar se o disparo colide com a largura total da imagem da vida extra.
        if (d.x >= buraco.x and d.x <= buraco.x + buraco.largura) or d.x + d.lar_disparo >= buraco.x and d.x + d.lar_disparo <= buraco.x + buraco.largura:
            # Se sim, irá checar em qual altura o disparo colidiu com o objeto. 
            if (d.y >= buraco.y and d.y <= buraco.y + buraco.altura) or d.y + d.alt_disparo >= buraco.y and d.y + d.alt_disparo <= buraco.y + buraco.altura:
                tela.tiros.pop(tela.tiros.index(d))
                return True
    for a in tela.cometas:
        if (a.x >= buraco.x and a.x <= buraco.x + buraco.largura) or a.x + a.w >= buraco.x and a.x + a.w <= buraco.x + buraco.largura:
            # Se sim, irá checar em qual altura o disparo colidiu com o objeto. 
            if (a.y >= buraco.y and a.y <= buraco.y + buraco.altura) or a.y + a.h >= buraco.y and a.y + a.h <= buraco.y + buraco.altura:
                tela.cometas.pop(tela.cometas.index(a))
                return True
    if (nave.x >= buraco.x and nave.x <= buraco.x + buraco.largura) or (nave.x + nave.largura >= buraco.x and nave.x + nave.largura <= buraco.x + buraco.largura):
        if (nave.y >= buraco.y and nave.y <= buraco.y + buraco.altura) or (nave.y + nave.altura >= buraco.y and nave.y + nave.altura <= buraco.y + buraco.altura):
            tela.vidas -= 10
            return True