def CriaDicio(l1,l2,Lvalue):
	saida = {}
	for i in range(len(l1)):
		#conte quantos itens tem na primeira lista
		#esse vai ser o número de vezes que você deve:
		#registrar no dicionario saida, cuja chave é 
		#o primeiro valor da lista1, o valor 
		#correspondente da Lvalue (lista de valores)
		saida[l1[i]] = {l2[i]:Lvalue[i]}
	return saida

def main():
	PKeys = ['S001', 'S002', 'S003', 'S004']
	SKeys = ['Pedra da Cebola', 'Praça do Papa', 'Costa Pereira', 'Reserva Paulo Vinhas']
	ValueList = [85, 98, 89, 92]
	d = CriaDicio(PKeys,SKeys,ValueList)
	print(d)
if __name__=="__main__":main()
