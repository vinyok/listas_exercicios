'''
23. 


Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a ordem.

'''

lista = []

def adicionando_elementos():
    

    while True: 
        user_l = input('Adicione elementos na lista: ')
        sair = str (input('\nDigite "parar" para parar de adicionar elementos: ')).lower()
        lista.append(user_l)
        set(lista)
        if sair == "parar":
            break
    

def removendo_se_igual():
    lista_unica = []
    for i in lista:
        if i not in lista_unica:
            lista_unica.append(i)

    return(lista_unica)

def final():
    adicionando_elementos()
    resultado = removendo_se_igual()
    print(resultado)

if __name__ == "__main__":
    final()