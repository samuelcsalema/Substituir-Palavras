texto = input('Texto: ').split()
localizar = input('Localizar: ')
substituta = input('Substituir: ')

for i in range(len(texto)):
    texto[i] = texto[i].replace(original, localizar)
    
print(' '.join(texto))