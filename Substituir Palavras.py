#Substitui mesmo se estiver dentro de outra palavra

texto = input('Texto: ').split()
localizar = input('Localizar: ')
substituta = input('Substituir: ')

for i in range(len(texto)):
    texto[i] = texto[i].lower().replace(localizar.lower(), substituta)
    
print(' '.join(texto))