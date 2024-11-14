''' altura > 1.75 e peso > 70'''

def dicioMaiorQue170(dicio):
	saida = {}
	for k,v in dicio.items():
		if (v[0] > 1.75) and (v[1] > 70):
			saida[k] = v
	return saida
def main():
	dicio = {'César': (1.77, 72), 'Aldo': (1.67, 65), 'Maria': (1.65, 68), 'Pedro':
(1.72, 66)}
	print(dicioMaiorQue170(dicio))
if __name__=="__main__":main()