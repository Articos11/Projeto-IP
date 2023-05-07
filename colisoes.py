import tela
import asteroides
def nave_ast(nave,ast):
    if (nave.x >= ast.x and nave.x <= ast.x + ast.w) or (nave.x + nave.largura >= ast.x and nave.x + nave.largura <= ast.x + ast.w):
        if (nave.y >= ast.y and nave.y <= ast.y + ast.h) or (nave.y + nave.altura >= ast.y and nave.y + nave.altura <= ast.y + ast.h):
            tela.vidas -= 1
            for v in tela.l_nav_vida:
                if tela.l_nav_vida.index(v) == len(tela.l_nav_vida) - 1:
                    tela.l_nav_vida.pop(tela.l_nav_vida.index(v))
            tela.cometas.pop(tela.cometas.index(ast))
            return True

def projetil_ast(projetil,ast):
    # Irá checar se o disparo colide com a largura total do asteroide.
    if (projetil.x >= ast.x and projetil.x <= ast.x + ast.w) or projetil.x + projetil.lar_disparo >= ast.x and projetil.x + projetil.lar_disparo <= ast.x + ast.w:
        # Se sim, irá checar em qual altura o disparo colidiu com o asteroide. 
        if (projetil.y >= ast.y and projetil.y <= ast.y + ast.h) or projetil.y + projetil.alt_disparo >= ast.y and projetil.y + projetil.alt_disparo <= ast.y + ast.h:
            # Aqui iremos dividir o asteroide em niveis diferentes.
            if ast.categoria == 3:
                tela.pontos += 200
                novo_asteroide_1 = asteroides.Asteroide(2)
                novo_asteroide_2 = asteroides.Asteroide(2)
                novo_asteroide_1.x = ast.x 
                novo_asteroide_2.x = ast.x
                novo_asteroide_1.y = ast.y
                novo_asteroide_2.x = ast.y
                tela.cometas.append(novo_asteroide_1)
                tela.cometas.append(novo_asteroide_2)
            elif ast.categoria == 2:
                tela.pontos += 100
                novo_asteroide_1 = asteroides.Asteroide(1)
                novo_asteroide_2 = asteroides.Asteroide(1)
                novo_asteroide_1.x = ast.x 
                novo_asteroide_2.x = ast.x
                novo_asteroide_1.y = ast.y
                novo_asteroide_2.x = ast.y
                tela.cometas.append(novo_asteroide_1)
                tela.cometas.append(novo_asteroide_2)
            else:
                tela.pontos += 50
            tela.cometas.pop(tela.cometas.index(ast))
            tela.tiros.pop(tela.tiros.index(projetil))
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
                return True
    if (nave.x >= atributo.x and nave.x <= atributo.x + atributo.w) or (nave.x + nave.largura >= atributo.x and nave.x + nave.largura <= atributo.x + atributo.w):
        if (nave.y >= atributo.y and nave.y <= atributo.y + atributo.h) or (nave.y + nave.altura >= atributo.y and nave.y + nave.altura <= atributo.y + atributo.h):
            tela.tiros_rapidos = True
            tela.multiplos_tiros.pop(tela.multiplos_tiros.index(atributo))
            tela.multiplos_inicio = tela.contagem_ast
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
                return True
    if (nave.x >= atributo.x and nave.x <= atributo.x + atributo.w) or (nave.x + nave.largura >= atributo.x and nave.x + nave.largura <= atributo.x + atributo.w):
        if (nave.y >= atributo.y and nave.y <= atributo.y + atributo.h) or (nave.y + nave.altura >= atributo.y and nave.y + nave.altura <= atributo.y + atributo.h):
            tela.vidas_extras.pop(tela.vidas_extras.index(atributo))
            tela.vidas += 1
            return True