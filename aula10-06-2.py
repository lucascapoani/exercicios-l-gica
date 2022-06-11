'''
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

"""
vetorA = [1,2,3,4,5,6,7,8,9,10]

soma = 0
for numero in vetorA:
    soma = soma + (numero * numero)

print(soma)
"""

vetorA = []

for x in range (10):
    while True:
        try:
            vetorA.append(int(input("Número: ")))
            break
        except:
            print("Erro")

soma = 0
for numero in vetorA:
    soma = soma + (numero * numero)

print(soma)
