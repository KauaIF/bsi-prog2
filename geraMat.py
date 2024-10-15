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
def main():
    m = geraMat(5,10,1,100)
    printMat(m)
if __name__=="__main__":
    main()