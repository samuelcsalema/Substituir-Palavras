texto = input('Texto: ').split()
original = input('Palavra que deseja substituir: ')
substituta = input('Palavra para substituir: ')


for i in range(len(texto)):
    texto[i] = texto[i].replace(original, substituta)
    
print(' '.join(texto))