dicio = {'a':'a','b':'b','c':None,'d':'d'}
excluir = []
#para cada chave 'k' e valor 'v' do dicionario
for k,v in dicio.items():
	if v == None:
		#se o valor for none
		excluir.append(k)
		#adicione na lista de exclusão
for i in excluir:
	#leia a lista de exclusão e exclua os listados do dicionario
	del dicio[i]
print(dicio)
