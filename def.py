"""
Introdução às funções (def) em python
Funções são trechos de código  usados para
replicar determinada ação ao longo do seu código.
elas podem receber valores para parâmetros (argumentos).
e retornar um valor específico.
Por padrão, funções python retornam none (nada).
"""


# def Print(a, b, c):
#    print('Várias1')
#    print('Várias2')
#    print('Várias3')
#    print('Várias4')

#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Luis')
saudacao()




