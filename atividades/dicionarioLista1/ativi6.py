''' altura > 1.75 e peso > 70'''

def func(dicio:dict):
    chaves = []
    valores = []
    saida = []

    #para cada chave 'k' e valor 'v' do dicionario
    for k,v in dicio.items():
        #adicione a chave a lista de chaves e o valor a lista de valores
        chaves.append(k)
        valores.append(v)
    
    for v in range(len(valores[0])):
        #repita as seguintes ações o mesmo
        #número de vezes que a quantidade de valores
        d = {}
        for c in chaves:
            #para cada chave registrada
            #Registre em D o valor do cicionario de entrada na mesma chave
            d[c] = dicio[c][v]
        saida.append(d)
    return saida
def main():
	dicio = {'Ciência': [88, 89, 62, 95], 'Linguagem': [77, 78, 84, 80]}
	print(func(dicio))
if __name__=="__main__":main()