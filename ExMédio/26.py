'''
26. 


Inverta os elementos de uma lista sem usar o m´etodo reverse.

'''

def invertendo_lista_sem_reverse(lista):
    lista_inversa = lista[::-1]
    return lista_inversa

entrada_user = (input('Digite números para serem invertidos: '))
lista_user = entrada_user.split()
resultado = invertendo_lista_sem_reverse(lista_user)
print(resultado)    
    