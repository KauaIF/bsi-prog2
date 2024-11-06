"""
Construa   um   relatório   de   Propritários   x   Veiculos contendo para cada Nome, e-mail de proprietário a lsta de placas, modelo, marca de veículos que ele possui.
"""
def Readtable(arq_name:str)->list:
    arq = open(arq_name,"rt")
    
    arq.readline()
    conteudo = []
    linha = arq.readline().strip()
    while linha != '':
        conteudo.append(linha.split(','))
        linha = arq.readline().strip()
    arq.close()
    return conteudo

def Union():
    pass

def main():
    prop = []
    cars = []

    prop = Readtable("proprietarios.txt")
    cars = Readtable("carros.txt")
    retorno = Union()

    print(cars)
if __name__=="__main__":
    main()