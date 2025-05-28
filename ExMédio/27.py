'''
27. 

Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao.

'''

pilha = []

for i in range(6):
    pilha.append(1)
    mais = len (pilha)
    pilha.append(mais)
    print(pilha)
