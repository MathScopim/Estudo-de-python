import importlib

import aula98_m 

print(aula98_m.variavel)

for i in range(10):
    importlib.reload
    print(i)

print('fim')