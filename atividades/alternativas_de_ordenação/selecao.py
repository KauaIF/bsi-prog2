'''selection sort geek for geek'''
def crescente(a:int|float|str,b:int|float|str)->bool:
    return a<b

def selecao(lst=[1,5,6,4,3,2,1],comparador:function=crescente):
    i = 0
    j = 0

    for i in range(len(lst)-1):
        ndx_menor = i 
        for j in range(i+1,len(lst)):
            if comparador(lst[j],lst[ndx_menor]):
                ndx_menor = j
        aux = lst[ndx_menor]
        lst[ndx_menor] = lst[i]
        lst[i] = aux
    return lst

def main():
    lst = [1,5,6,4,3,2,1]
    print(lst)
    print('\n\n\n')
    selecao(lst)
    print(lst)
if __name__=="__main__":main()
