''' altura > 1.75 e peso > 70'''

def func(lis):
    saida = {}
    for i in lis:
        k,v = i[0],i[1]
        aux = saida.get(k,None)
        if aux == None:
            saida[k] = [v]
        else: saida[k].append(v)
    return saida
def main():
	lis = [('amarelo', 1), ('azul', 2), ('amarelo', 3), ('azul', 4), ('vermelho', 1)]
	print(func(lis))
if __name__=="__main__":main()