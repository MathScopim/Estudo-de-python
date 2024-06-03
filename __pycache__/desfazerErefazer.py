def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
tarefas = []
tarefas_refazer = []






while True:
    print('Comandos: listar, refazer, desfazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        print(2)
        continue
    elif tarefa == 'desfazer':
        print(3)
    else:
        print(4)