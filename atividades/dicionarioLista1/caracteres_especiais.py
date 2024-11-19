txt = input()
dicio = {}
dicio['a'] = "àáâäæãåā"
dicio['A'] = "ÀÁÂÄÆÃÅĀ"

dicio['e'] = "èéêëẽ"
dicio['E'] = "ÈÉÊËẼ"

dicio['i'] = "ìíîïĩ"
dicio['I'] = "ÌÍÎÏĨ"

dicio['o'] = "òóôöõ"
dicio['U'] = "ÒÓÔÖÕ"

dicio['u'] = "ùúûüũ"
dicio['U'] = "ÙÚÛÜŨ"

dicio['c'] = "ç"
dicio['C'] = "Ç"

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