'''
22. 

Crie uma fun¸c˜ao que recebe uma lista e retorna uma nova lista com apenas os
elementos ´unicos.


'''

def listas_elementos(lista):
    lista_func = []
    for i in lista:
        if i not in lista_func:
            lista_func.append(i)
    return lista_func

lista_user = [0, 0, 1, 3, 4, 4]
resultado = listas_elementos(lista_user)
print(resultado)
    
    