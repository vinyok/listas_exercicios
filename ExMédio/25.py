'''
25. 

Solicite uma frase ao usu´ario e retorne uma lista com todas as palavras (use split).

'''

def palavras(frase):
    lista = frase_user.split()
    return lista

frase_user = str (input('Escreva uma frase: '))
resultado = palavras(frase_user)
print(resultado)