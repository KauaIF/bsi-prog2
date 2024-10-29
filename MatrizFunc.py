import random
def geraMat(lines,columns,min,max):
    matriz = list()
    for i in range(lines):
        line = list()
        for i in range(columns):
            line.append(random.randrange(min,max))
        matriz.append(line)
    return matriz
def printMat(mat):
    saida = ""
    for i in mat:
        for j in i:
            saida += f"{j:2d}, "
        saida = saida[:-2]+'\n'
    print(saida)

def extrai(Matriz_ini,linha_ini,coluna_ini,tamanho_matriz):
    if linha_ini+tamanho_matriz> len(Matriz_ini):
        return None
    saida = []
    for i in range(linha_ini,linha_ini+tamanho_matriz):
        insere_linha = []
        for j in range(coluna_ini,coluna_ini+tamanho_matriz):
            insere_linha.append(Matriz_ini[i][j])
        saida.append(insere_linha)
    return saida

def insere(Matriz_ini,linha_ini,coluna_ini,m):
    linhas_mi = len(m)
    colunas_mi = len(m[0])
    if linha_ini+linhas_mi> len(Matriz_ini):
        return None
    for i in range(linha_ini,linha_ini+linhas_mi):
        for j in range(coluna_ini,coluna_ini+colunas_mi):
            Matriz_ini[i][j] = m[i][j]
    return Matriz_ini


def main():
    m = geraMat(3,3,1,100)
    printMat(m)
    printMat(extrai(m,1,1,2))
    printMat(insere(m,1,1,[[99,99],[99,99]]))
if __name__=="__main__":
    main()