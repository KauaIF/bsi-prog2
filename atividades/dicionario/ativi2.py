def dicioMaiorQue170(dicio):
	saida = {}
	for k,v in dicio.items():
		if v >= 170:
			saida[k] = v
	return saida
def main():
	dicio = {'a':1,'b':180,'c':190,'d':2}
	print(dicioMaiorQue170(dicio))
if __name__=="__main__":main()
