"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for indice, nome in enumerate(lista):
   print(indice, nome, lista[indice])

#for item in enumerate(lista):
#   indice, nome = item
#   print(indice, nome)

