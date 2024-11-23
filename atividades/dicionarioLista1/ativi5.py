''' altura > 1.75 e peso > 70'''

def func(lis):
    saida = {}
    for i in lis:
        #Para cada par de tuplas na lista
        k,v = i[0],i[1]
        #k recebe a chave (que é uma cor) e v recebe o valor
        aux = saida.get(k,None)
        #aux serve pra ver se já está registrado
        if aux == None:
            #se for uma cor aparecendo pela primeira vez 
            #crie o registro
            saida[k] = [v]
        else: saida[k].append(v)
        #se essa cor já apareceu antes, apenas adicione
        #ao registro existente
    return saida
def main():
	lis = [('amarelo', 1), ('azul', 2), ('amarelo', 3), ('azul', 4), ('vermelho', 1)]
	print(func(lis))
if __name__=="__main__":main()