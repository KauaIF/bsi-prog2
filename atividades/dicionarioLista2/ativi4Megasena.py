def func(n_arq):
    D = {}
    arq = open(n_arq,'rt')
    linha = arq.readline()
    while linha != "":
        lst = linha[:-1].split("\t")
        for i in lst:
            if i in D:
                D[i]+=1
            else:
                D[i] = 1
        linha = arq.readline()
    return D
def main():
	print(func("ceps.txt"))
if __name__=="__main__":main()