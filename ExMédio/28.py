'''
28. 

Crie uma funcao que receba uma lista e retorne a soma de todos os elementos numericos

'''
def soma (lista):
    return sum(lista)

lista_user = []
    
while True:
    user = (input('Digite elementos númericos: '))
    nms = float(user)
    lista_user.append(nms)
    saida = input('\nDigite "SAIR" quando desejar parar de adicionar: ').lower()
    if saida == "sair":
        break
    
resultado = soma(lista_user)
print(f'A soma dos elementos na lista é: {resultado} ')
    
    