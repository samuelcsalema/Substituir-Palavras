#Apenas substitui se for palavra separada

texto = input('Texto: ').split()
localizar = input('Localizar: ')
substituta = input('Substituir: ')

for i in range(len(texto)):
    if texto[i].lower() == localizar.lower():
        texto[i] = substituta
    
print(' '.join(texto))