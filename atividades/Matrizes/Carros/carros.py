"""
Construa   um   relatório   de   Propritários   x   Veiculos contendo para cada Nome, e-mail de proprietário a lsta de placas, modelo, marca de veículos que ele possui.
"""

# assim?
# [nome,email,[[placa1,modelo1,marca1],[placa2,modelo2,marca2]]]
# ou assim? 
# [nome,email,[[placa1,placa2,placa3],[modelo1,modelo2,modelo3],[marca1,marca2,marca3]]]
# vou optar pelo primeiro

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

def Union(prop:list,cars:list)->list:
    merged = []
    for person in prop:
        cell = []
        cell.append(person[1])
        cell.append(person[2])
        for car in cars:
            if car[3]== person[0]:
                cell.append([car[0],car[1],car[2]])
        merged.append(cell)
    return merged

def main():
    prop = []
    cars = []

    prop = Readtable("proprietarios.txt")
    cars = Readtable("carros.txt")

    for i in Union(prop,cars):
        print(i)
if __name__=="__main__":
    main()