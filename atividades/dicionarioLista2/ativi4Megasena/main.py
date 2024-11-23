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
        lst = linha[:-1].split("\t")
        #lst representa uma linha da minha tabela no formato de uma lista
        for i in lst:
            #para cada item na linha da tabela
            #vou começar a contar quatas vezes aparece cada número
            if i in D:
                #Se esse número já apareceu antes, adiciona mai um no contador 
                D[i]+=1
            else:
                #Se esse número não apareceu antes, cria um contador no 1
                D[i] = 1
        #leia uma nova linha e começe o ciclo de novo
        linha = arq.readline()
    #retorna um dicionário com os números e quantas vezes apareceram
    return D
def main():
    resultado = func("mega_sena.txt")
    print(resultado)
if __name__=="__main__":main()