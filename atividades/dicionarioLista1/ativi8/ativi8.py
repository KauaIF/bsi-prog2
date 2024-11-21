def func(n_arq):
    D = {}
    arq = open(n_arq,'rt')
    linha = arq.readline()
    while linha != "":
        lst = linha.strip().split(',')
        cep = int(lst[0])
        num = int(lst[1])
        if cep in D:
            D[cep].append(num)
        else:
            D[cep] = [num]
        linha = arq.readline()
    return D
def main():
	print(func("ceps.txt"))
if __name__=="__main__":main()