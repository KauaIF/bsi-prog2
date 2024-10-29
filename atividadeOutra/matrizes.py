import random
def geraMat(lines,columns,min,max):
    matriz = list()
    for i in range(lines):
        line = list()
        for i in range(columns):
            line.append(random.randrange(min,max))
        matriz.append(line)
    return matriz
def printMatriz(mat):
    saida = ""
    for i in mat:
        for j in i:
            saida += f"{j:2d}, "
        saida = saida[:-2]+'\n'
    print(saida)

def loadMat(nome_arq:str="matrizSalva.txt"):
    arq = open(nome_arq,"rt")
    m = []
    linha = arq.readline().strip()
    while linha != '':
        lst = [int(i) for i in linha.split()]
        m.append(lst)
        linha = arq.readline().strip()
    return m

def salvaMatriz(mat, nome_arq):
    arq = open(nome_arq, 'wt')
    if mat != None:
        linhas = len(mat)
        colunas = len(mat[0])

        for i in range(linhas):
            for j in range(colunas):
                arq.write(f"{mat[i][j]:2d} ")
            if i < (linhas-1):
                arq.write("\n")
    arq.close()

def main():
    m = geraMat(5,10,1,100)
    printMatriz(m)
    salvaMatriz(m,"matrizSalva.txt")
    loadMat()
if __name__=="__main__":
    main()