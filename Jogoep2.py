def define_posicoes(linha, coluna, orientacao, tamanho):

    coordenadas = []

    for i in range(tamanho):
        coordenadas.append([linha, coluna])

        if orientacao == "vertical":
            linha += 1
        if orientacao=="horizontal":
            coluna += 1

    return coordenadas