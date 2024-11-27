import os
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
        D[lst[0]]=lst[1:]
        #leia uma nova linha e começe o ciclo de novo
        linha = arq.readline()
    #retorna um dicionário com os números e quantas vezes apareceram
    return D
def inserir(arq,tel,nome,email):
    base = carregar(arq)
    if bool(base.get(tel,False)):
        ans = input("O contato já existe deseja substituir? [s/N]")
        if ans=='s':
            base[tel] = [nome,email]
            a = open(arq,"wt")
            for i in base.keys():
                escreva = i
                for dado in base[i]:
                    escreva += f",{dado}"
                a.write(escreva)
        else:
            print('ação cancelada')
    else:
        print('aaa')
    input()

def main():
    os.system("cls")
    arquivo_ini = "telefones.txt"
    resultado = carregar(arquivo_ini)
    entrada = input("Selecione\n1)para inserir dados\n2)para ler dados\n3)para deletar dados\n").lower()
    while entrada != '':
        os.system("cls")
        if entrada == '1':
            inserir(arquivo_ini,input("tel: "),input("nome: "),input("email: "))
        if entrada == '2':
            print(carregar(arquivo_ini))
            input()
        os.system("cls")
        entrada = input("Selecione\n1)para inserir dados\n2)para ler dados\n3)para deletar dados\n").lower()
if __name__=="__main__":main()