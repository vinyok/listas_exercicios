'''
30. 

Dada uma lista de strings, crie uma nova lista com o tamanho (numero de caracteres)
de cada string.


'''

lista_user = []
def num_caracteres(lista):
    
    while True: 
        user = input('Escreva palavras: ')
        lista_user.append(user)
        sair = input('Digite: "parar", caso deseje parar de adicionar elementos: ').lower()
        if sair == "parar":
            break
        l_tamanho = [len(i) for i in lista_user]
        
        
    
resultado = num_caracteres(lista_user)
print(resultado)