lista_de_tarefas = []
menu = ''


while True:
    menu = input('Você deseja [i]nserir, [d]eltar, [v]isualizar? ')

    if menu == 'i':
        tarefa = input('Digite a tarefa que deseja registrar: ')
        lista_de_tarefas.append(tarefa)

    elif menu == 'v':
        indices = range(len(lista_de_tarefas))
        for indice in indices:
            print(indice, lista_de_tarefas[indice])

    elif menu == 'd':
        deletar = int(input('Informe a tarefa que deseja remover com o número correspondente: '))
        del lista_de_tarefas[indice]
        break
    continue
                