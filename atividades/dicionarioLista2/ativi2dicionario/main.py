#função que abre o arquivo e registra os dados
def func(n_arq:str)->dict:
    #dicionario a ser preenchido 'D'
    D = {}
    arq = open(n_arq,'rt')
    linha = arq.readline()
    while linha != "":
        #Para toda linha não vazia vou retirar a quebra de linha do
        #ultimo caracter (linha[:-1] faz isso) e 
        #formar uma lista dividindo os conteúdos
        #pelo "\t" (que é o caracter TAB)
        lst = linha.strip().split(",")
        #lst representa uma linha da minha tabela no formato de uma lista
        D[lst[1]]=lst[0]
        #leia uma nova linha e começe o ciclo de novo
        linha = arq.readline()
    #retorna um dicionário com os números e quantas vezes apareceram
    return D
def main():
    resultado = func("dic-pt-en.txt")
    entrada = input("").lower()
    while entrada != '':
        print(resultado.get(entrada,"tradução indisponível"))
        entrada = input("").lower()
if __name__=="__main__":main()