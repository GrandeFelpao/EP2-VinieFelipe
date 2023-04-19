# Define posições-------------------------------------------------------------------------------------------------
def define_posicoes(linha, coluna, orientacao, tamanho):

    coordenadas = []

    for i in range(tamanho):
        coordenadas.append([linha, coluna])

        if orientacao == "vertical":
            linha += 1
        if orientacao=="horizontal":
            coluna += 1

    return coordenadas

# Preenche frota--------------------------------------------------------------------------------------------------

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

