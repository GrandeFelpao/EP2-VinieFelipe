## Exercício 1 - Define Posições
def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = []

    for i in range(tamanho):
        posicoes.append([linha, coluna])

        if orientacao == "vertical":
            linha += 1
        if orientacao=="horizontal":
            coluna += 1

    return posicoes

## Exercício 2 - Preenche Frota---------------------------------------------------------------------------------------------------

def define_posicoes(linha, coluna, orientacao, tamanho):
    coordenadas = []
    for i in range(int(tamanho)):
        coordenadas.append([linha, coluna])
        if orientacao == "vertical":
            linha += 1
        if orientacao=="horizontal":
            coluna += 1
    return coordenadas


def preenche_frota(frota,nome_do_navio,linha, coluna, orientacao, tamanho):
    nova_posicao=[]
    nova_posicao.append(define_posicoes(linha, coluna, orientacao, tamanho))

    if nome_do_navio not in frota:
        frota[nome_do_navio]=nova_posicao

    else:
        posicao=frota[nome_do_navio]
        posicao.append(define_posicoes(linha, coluna, orientacao, tamanho))
        frota[nome_do_navio]=posicao
    return frota

## Exercício 3 - Faz Jogada------------------------------------------------------------------------------------

def faz_jogada(tabuleiro, linha, coluna):
    
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    
    return tabuleiro

## Exercíico 4 - Posiciona Frota-----------------------------------------------------------------------------------

def posiciona_frota(informacoes):
    tabuleiro = [[0] * 10 for _ in range(10)]

    for posicoes in informacoes.values():
        for posicao in posicoes:
            for coordenada in posicao:
                x, y = coordenada
                tabuleiro[x][y] = 1

    return tabuleiro

## Exercício 5 - Quantas embarcações afundadas?-------------------------------------------------------------------------------------

def afundados(frota, tabuleiro):
    afundados = []

    for posicoes in frota.values():
        for posicao in posicoes:
            afundado = True
            for coordenada in posicao:
                x, y = coordenada
                if tabuleiro[x][y] != 'X':
                    afundado = False
                    break
            if afundado:
                afundados.append(1)
    resultado = len(afundados)

    return resultado

## Exercício 6 - Posição Válida-----------------------------------------------------------------------------------------------------
def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = []

    for i in range(tamanho):
        posicoes.append([linha, coluna])

        if orientacao == "vertical":
            linha += 1
        if orientacao=="horizontal":
            coluna += 1

    return posicoes

def posicao_valida (frota,linha,coluna,orientacao,tamanho):
    posicao_do_barco=define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicao_do_barco:
        if posicao[0]>9 or posicao[1]>9:
            return False
        for posicao_existente in frota:
            posicao_frota=frota[posicao_existente]
            for barcos in posicao_frota:
                for coordenadas in barcos:
                    if coordenadas==posicao:
                        return False
    return True

## Exercício 7 - Posicionando Frota-------------------------------------------------------------------------------------------------------------

def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = []

    for i in range(tamanho):
        posicoes.append([linha, coluna])

        if orientacao == "vertical":
            linha += 1
        if orientacao=="horizontal":
            coluna += 1

    return posicoes

def posicao_valida (frota,linha,coluna,orientacao,tamanho):
    posicao_do_barco=define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicao_do_barco:
        if posicao[0]>9 or posicao[1]>9:
            return False
        for posicao_existente in frota:
            posicao_frota=frota[posicao_existente]
            for barcos in posicao_frota:
                for coordenadas in barcos:
                    if coordenadas==posicao:
                        return False
    return True

def preenche_frota(frota,nome_do_navio,linha, coluna, orientacao, tamanho):
    nova_posicao=[]
    nova_posicao.append(define_posicoes(linha, coluna, orientacao, tamanho))

    if nome_do_navio not in frota:
        frota[nome_do_navio]=nova_posicao

    else:
        posicao=frota[nome_do_navio]
        posicao.append(define_posicoes(linha, coluna, orientacao, tamanho))
        frota[nome_do_navio]=posicao
    return frota

tamanho_dos_navios={'porta-aviões':4 ,'navio-tanque':3,'contratorpedeiro':2,'submarino':1}

quantidade_de_navios={'porta-aviões':1 ,'navio-tanque':2,'contratorpedeiro':3,'submarino':4}

frota={'porta-aviões':[] ,'navio-tanque':[],'contratorpedeiro':[],'submarino':[]}

for tipo_de_navio,quantidade in quantidade_de_navios.items():
    for quant in range(quantidade):
        navio_foi_validado=False
        while navio_foi_validado==False:
            print (f'Insira as informações referentes ao navio {tipo_de_navio} que possui tamanho {tamanho_dos_navios[tipo_de_navio]}')
            linha=int(input('linha: '))
            coluna=int(input('coluna: '))
            if tipo_de_navio !='submarino':
                orientacao=int(input('qual orientação que deseja posicionar a sua embarcação'))
                if orientacao==1:
                    orientacao='vertical'
                else:
                    orientacao='horizontal'
            else:
                orientacao = 'horizontal'
            navio_foi_validado=posicao_valida(frota,linha,coluna,orientacao,tamanho_dos_navios[tipo_de_navio])
            if not navio_foi_validado:
                print('Esta posição não está válida!')
            else:
                frota=preenche_frota(frota,tipo_de_navio,linha,coluna,orientacao,tamanho_dos_navios[tipo_de_navio])
print(frota)