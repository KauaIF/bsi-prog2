'''
Lista de dicionários na entrada:
[{'id': '#FF0000', 'cor': 'vermelho'}, {'id': '#800000', 'cor': 'marrom'}, {'id': '#FFFF00',
'cor': 'amarelo'}, {'id': '#808000', 'cor': 'oliva'}]
Lista de dicionários na saída (removido dicionário com id #FF0000):
[{'id': '#800000', 'cor': 'marrom'}, {'id': '#FFFF00', 'cor': 'amarelo'}, {'id': '#808000',
'cor': 'oliva'}]

'''

def func(lis:dict,id):
    saida = []
    #para cada item da lista
    for i in lis:
        if i['id']!=id:
            #registre todos diferentes do id que recebi
            saida.append(i)
    #retorna a lista sem um id específico
    return saida
def main():
	lis = [{'id': '#FF0000', 'cor': 'vermelho'}, {'id': '#800000', 'cor': 'marrom'}, {'id': '#FFFF00','cor': 'amarelo'}, {'id': '#808000', 'cor': 'oliva'}]
	print(func(lis,'#FF0000'))
if __name__=="__main__":main()