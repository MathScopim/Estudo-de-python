""" 
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definiçao
def soma(x, y, z):
    print(f'{x=} + y={y} {z=}', '|', 'x + y + z = ', x + y + z) 



soma(1, 2, 3)
soma(x=1, y=2, z=5)

print(1, 2, 3, sep='-')
