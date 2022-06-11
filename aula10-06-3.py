'''
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão
ser compostos pelos elementos
intercalados dos dois outros vetores.
'''

listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [11,22,33,44,55,66,77,88,99,100]
listaC = []

for indice in range (10):
    listaC.append(listaA[indice])
    listaC.append(listaB[indice])

print(listaC)
