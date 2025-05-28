'''
29. 


Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.
'''

def menu_interativo():
    lista = []
    while True:
        print('\nMenu Interativo. ')
        print('\nAdicionar. Digite "add", para adicionar elementos na lista. ')
        print('Adicionar. Digite "remove", para remover elementos na lista. ')
        print('Adicionar. Digite "listar", para listar elementos na lista. ')
        print('Adicionar. Digite "sair", para sair do progama. ')
        escolha = input('\nEscolha: ').lower()

        if escolha == "add":
            elemento_add = input('Digite um elemento para ser adicionado: ')
            lista.append(elemento_add)
            print(f'O elemento "{elemento_add}" foi adicionado. ')
        
        elif escolha == "remove":
            remover = input('Digite um elemento para ser removido: ')
            if remover in lista:
                lista.remove(remover)
                print(f'O elemento {remover} foi removido da lista. ')
            else:
                print(f'O elemento "{escolha}" não está na lista. ')
            
        elif escolha == "listar":
            print(f'A lista final é: {lista}')
        elif escolha == "sair":
            print("Progama fechado! ")
            break

menu_interativo()
            
            
