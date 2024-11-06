txt = input().lower() 
dicio = {}
dicio['a'] = "àáâäæãåā"
dicio['e'] = "èéêëẽ"
dicio['i'] = "ìíîïĩ"
dicio['o'] = "òóôöõ"
dicio['u'] = "ùúûüũ"
dicio['c'] = "ç"

saida = ""
especial = False
for letter in txt:
    for key,value in dicio.items():
        if letter in value:
            especial = True
            saida = saida + key
    if not(especial):
        saida = saida + letter
    especial = False
    
print(saida)