def main()->None:
    lista = list()
    vendas = float()
    
    lista = [0,0,0,0,0,0,0,0,0]
    vendas = float(input("valor de vendas: "))
    while vendas>200:
        pos = int((vendas-200)//100)
        if pos>=8:
            lista[8] = lista[8]+1
        else:
            lista[pos] = lista[pos]+1
        vendas = float(input("valor de vendas: "))
    dicio = dict()
    dicio["$200 - $299"]=lista[0]
    dicio["$300 - $399"]=lista[1]
    dicio["$400 - $499"]=lista[2]
    dicio["$500 - $599"]=lista[3]
    dicio["$600 - $699"]=lista[4]
    dicio["$700 - $799"]=lista[5]
    dicio["$200 - $899"]=lista[6]
    dicio["$200 - $999"]=lista[7]
    dicio["$1000 em diante"]=lista[8]
    print(dicio)
if __name__ == "__main__":
    main()