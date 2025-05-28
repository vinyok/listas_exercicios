'''
29. 

Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.

'''

lista = []

def menu():
    while True:
        print('\nMenu interativo. ')
        print('\nDigite: "add" para adicionar elementos na lista ')
        print('Digite: "remove" para remover elementos na lista ')
        print('Digite: "list" concluir a lista ')
        print('Digite: "quit" sair do menu ')
        escolha = str (input('\nEscolha: ')).lower()
    
        if escolha == "add":
            add = input('\nDigite um elemento para ser adicionado: ')
            print(f'{add} foi adicionado. ')
            lista.append(add)
    
        elif escolha == "remove":
            remove = input('\nDigite um elemento para ser removido: ')
            if remove in lista:
                lista.remove(remove)
    
        elif escolha == "list":
            print(f'\nAssim ficou a lista: {lista}')
            return lista
    
        elif escolha == "quit":
            print('\nProgama fechado. ')
            break
menu()
        
    
        
    
    
    