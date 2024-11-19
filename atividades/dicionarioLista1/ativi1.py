dicio = {'a':'a','b':'b','c':None,'d':'d'}
excluir = []
for k,v in dicio.items():
	if v == None:
		excluir.append(k)
for i in excluir:
	del dicio[i]
print(dicio)
