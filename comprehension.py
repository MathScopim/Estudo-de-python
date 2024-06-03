# List Comprehension em Python
# List comprehension é uma forma rapida para criar listas
# A partir de iteráveis.
# print (list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
    ]

print(lista)