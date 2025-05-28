'''
24. 


Separe uma lista de n´umeros em duas: uma com pares e outra com ´ımpares.

'''

def par_ou_impar(numeros):
    nums_pares = []
    nums_impers = []
    for n in numeros:
        if n % 2 == 0:
            nums_pares.append(n)
        else:
            nums_impers.append(n)
    return nums_pares, nums_impers
numero_user = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
resultado = par_ou_impar(numero_user)
print("Lista de pares: ",resultado[0])
print("Lista de Impares: ",resultado[1])
    