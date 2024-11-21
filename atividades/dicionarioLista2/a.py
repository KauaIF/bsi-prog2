arq = open("mega_sena.txt",'r')
linha = arq.readline()[:-1].split("\t")
print(linha)