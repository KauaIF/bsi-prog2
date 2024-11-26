#função que abre o arquivo e registra os dados
def carregar(n_arq:str)->dict:
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
def inserir(arq,nome,tel):
    pass

def main():
    resultado = carregar("telefones.txt")
    print(
            """Selecione\n1)para inserir dados\n2)para ler dados\n3)para deletar dados"""
        )
    entrada = input("").lower()
    while entrada != '':
        if entrada == 1:
            inserir("telefones.txt",input("nome: "),input("tel: "))
        print(
            """Selecione\n1)para inserir dados\n2)para ler dados\n3)para deletar dados"""
        )
        entrada = input("")
if __name__=="__main__":main()