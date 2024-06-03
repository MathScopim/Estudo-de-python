# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
# Vantagen : você tem o namespace do módulo
# Desvantagens: nomes grandes


# Partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
#from sys import exit, platform

#print(platform)

# Alias 1 import nome_modulo as apelido
# Alias 2 from nome_modulo import objeto as apelido
# Vantagens: Você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: Importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import *

print(platform)
exit()