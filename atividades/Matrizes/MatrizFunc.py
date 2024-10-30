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

def insere(Matriz_ini,linha_ini,coluna_ini,inserida):
    linhas_matriz_inserida = len(inserida)
    colunas_matriz_inserida = len(inserida[0])
    if linha_ini+linhas_matriz_inserida> len(Matriz_ini):
        return None
    for i in range(linha_ini,linha_ini+linhas_matriz_inserida):
        for j in range(coluna_ini,coluna_ini+colunas_matriz_inserida):
            Matriz_ini[i][j] = inserida[i-linha_ini][j-coluna_ini]
    return Matriz_ini

def deslocaEsq(Matriz):
    for linha in Matriz:
        linha.pop(0)
        linha.append(0)
    return Matriz

def deslocaDir(Matriz):
    for linha in Matriz:
        linha.pop(-1)
        linha.insert(0,0)
    return Matriz

def rotEsq(Matriz):
    for linha in Matriz:
        linha.append(linha[0])
        linha.pop(0)
    return Matriz

def rotDir(Matriz):
    for linha in Matriz:
        linha.insert(0,linha[-1])
        linha.pop()
    return Matriz

def vizinhos(m,l,c):
    retorno = []
    if l!=0 and c!=0:
        if (l!=len(m)-1) and c!=len(m[0]):
            print('oi')
        else: print('ultima coluna/linha')
    else: print("primeira linha/coluna")


def main():
    #m = geraMat(3,3,1,100)
    m = [[5,4,1,8,3,6],[3,0,5,6,7,4],[9,1,2,8,4,3],[4,5,1,9,0,2],[9,0,7,4,1,3]]
    printMat(m)
    #printMat(extrai(m,1,1,2))
    #printMat(insere(m,1,2,[[1,1,1],[1,1,1],[1,1,1]]))
    #printMat(deslocaEsq(m))
    #printMat(deslocaDir(m))
    #printMat(rotEsq(m))
    #printMat(rotDir(m))
    vizinhos(m,5,1)
if __name__=="__main__":
    main()