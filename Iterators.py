import sys
# Generator expression, Iterables e Iterators em Python
# Generator funções que sabe pausar em determinada ocasião

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(1000000)]
generator = [n for n in range(1000000)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))