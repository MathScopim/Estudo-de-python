# dir, hasattr e getattr em python
# dir - Mostra todos os nomes definidos dentro de string
# hasattr - Checa dinamicamente se o objeto tem um atributo
# getattr - Checa se  tem um nome em uma string
string = 'Mat'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)