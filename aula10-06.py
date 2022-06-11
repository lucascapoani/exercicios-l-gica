'''
Faça um programa que receba a temperatura média de cada mês do
ano e armazene-as em uma lista. Após isto, calcule a média anual
das temperaturas e mostre todas as temperaturas acima da média
anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

'''
lista_mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
lista_temp = []
soma_meses = 0

for i in range (len(lista_mes)):
    mes = input(f'Digite a temperatura média do mês de {lista_mes[i]}')
    lista_temp.append(mes)
print(lista_temp)

media = round(sum(lista_temp) / 12, 1)
print(f"A média anual das temperaturas digitadas foi {media}")
'''

lista_temperaturas = []
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

for mes in range (12):
    temperatura = int(input("Temperatura: "))
    lista_temperaturas.append(temperatura)

soma = sum(lista_temperaturas)
media = soma / 12

for temperatura in lista_temperaturas:
    if temperatura > media:
        print(temperatura)

for indice in range(12):
    if lista_temperaturas[indice] > media:
        print(lista_temperaturas[indice], meses[indice])




        







    
    

