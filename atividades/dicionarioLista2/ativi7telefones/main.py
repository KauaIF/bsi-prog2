import os
#função que abre o arquivo e registra os dados
def carregar(n_arq:str)->dict:
    #dicionario a ser preenchido 'D'
    arq = open(n_arq,'rt')
    D = {}
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
    arq.close()
    #retorna um dicionário com os números e quantas vezes apareceram
    return D
def inserir(arq,tel,nome,email):
    base = carregar(arq)
    if bool(base.get(tel,False)):
        ans = input("O contato já existe deseja substituir? [s/N]\n")
        if ans=='s':
            base[tel] = [nome,email]
            a = open(arq,"wt")
            for i in base.keys():
                escreva = i
                escreva += f",{base[i][0]},{base[i][1]}"
                a.write(f"{escreva}\n")
            print("atualizado com sucesso")
        else:
            print('ação cancelada')
    else:
        a = open(arq,"at")
        a.write(f"\n{tel},{nome},{email}")
        print('inserido com sucesso')
    a.close()
    input("Pressione qualquer tecla para prosseguir")

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