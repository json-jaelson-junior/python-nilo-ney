"""
### CAPÍTULO 4 ###

Condições - Else

Testando os comandos que o autor pediu na página 125:
"""

### Else

# Else é aplicado quando a condição do If é falsa.

### Programa 4.5: Carro novo ou velho, dependendo da idade com else

idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else: #1
    print("Seu carro é velho") #2

### Programa 4.6: Lê dois valores e imprime qual é o maior com else

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    print("O primeiro valor é maior!")
else:
    print("O segundo valor é maior!")

"""
### EXERCÍCIOS ###

Exercício 4.5 - Execute o Programa 4.5 e experimente alguns valores.
Verifique se os resultados foram os mesmos do Programa 4.2.
"""

# Resolução do exercício:

print("Sim, os resultados são iguais.")

"""
Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
"""

# Resolução do exercício:

quilometragem = float(input("Digite a distância da sua viagem: "))

if quilometragem <= 200:
    print(f"O valor da sua passagem é de R$ {quilometragem * 0.50:.2f}.")
else:
    print(f"O valor da sua passagem é de R$ {quilometragem * 0.45:.2f}.")

"""
Exercício 4.7 - Analise o Programa 4.3. Faz sentido usar o else nesse programa?
Explique sua resposta.

### Programa 4.3: Cálculo do Imposto de Renda

salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario #1
imposto = 0

if base > 3000: #2
    imposto = imposto + ((base - 3000) * 0.35) #3
    base = 3000 #4

if base > 1000: #5
    imposto = imposto + ((base - 1000) * 0.20) #6
"""

# Resolução do exercício:

print("Não faz sentido utilizar else no Programa 4.3, devido às faixas salariais que ele analisa.")

"""
Exercício 4.8 - Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else.
"""

# Resolução do exercício:

plano = input("Qual é o seu plano de celular? ")

if plano != "falopouco" and plano != "falomuito":
    print("Não conheço esse plano")
else:
    if plano == "falopouco":
        minutos_no_plano = 100
        extra = 0.20
        preco = 50
    else:
        minutos_no_plano = 500
        extra = 0.15
        preco = 99

    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    
    print(f"\nVocê vai pagar:")
    print(f"\nPreço do plano:     R$ {preco:.2f}")
    acrescimo = 0

    if minutos_consumidos > minutos_no_plano:
        acrescimo = extra * (minutos_consumidos - minutos_no_plano)

    print(f"Acréscimo:          R$ {acrescimo:.2f}")
    print(f"Total:              R$ {preco + acrescimo:.2f}")