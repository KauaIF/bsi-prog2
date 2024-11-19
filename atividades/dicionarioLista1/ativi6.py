''' altura > 1.75 e peso > 70'''

def func(dicio:dict):
    chaves = []
    valores = []
    saida = []

    for k,v in dicio.items():
        chaves.append(k)
        valores.append(v)
    
    for v in range(len(valores[0])):
        d = {}
        for c in chaves:
             d[c] = dicio[c][v]
        saida.append(d)
    return saida
def main():
	dicio = {'Ciência': [88, 89, 62, 95], 'Linguagem': [77, 78, 84, 80]}
	print(func(dicio))
if __name__=="__main__":main()