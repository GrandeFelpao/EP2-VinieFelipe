def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = []

    for i in range(tamanho):
        posicoes.append([linha, coluna])

        if orientacao == "vertical":
            linha += 1
        if orientacao=="horizontal":
            coluna += 1

    return posicoes