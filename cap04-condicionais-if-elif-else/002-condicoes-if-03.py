"""
### CAPÍTULO 4 ###

Condições - If 03

Testando os comandos que o autor pediu nas páginas 121, 122 e 123:
"""

### If

# If nada mais é do que um "se"; se a condição for verdadeira, faça tal coisa

### Programa 4.3: Cálculo do Imposto de Renda

salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario #1
imposto = 0

if base > 3000: #2
    imposto = imposto + ((base - 3000) * 0.35) #3
    base = 3000 #4

if base > 1000: #5
    imposto = imposto + ((base - 1000) * 0.20) #6

print(f"Salário: R$ {salario:6.2f} Imposto a pagar: R$ {imposto:6.2f}")

"""
### EXERCÍCIOS ###

Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.
"""

# Resolução do exercício:

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
maior_numero = numero1
menor_numero = numero1

if numero2 > numero1 and numero2 > numero3:
    maior_numero = numero2

if numero3 > numero1 and numero3 >= numero2:
    maior_numero = numero3

if numero2 < numero1 and numero2 < numero3:
    menor_numero = numero2

if numero3 < numero1 and numero3 <= numero2:
    menor_numero = numero3 

print(f"O maior número é o número {maior_numero}.")
print(f"O menor número é o número {menor_numero}.")

"""
Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

# Resolução do exercício:

salario = float(input("Digite o valor do seu salário: "))

if salario > 1250:
    print(f"O aumento do seu salário foi de R$ {salario * 0.10:.2f} e o valor do seu novo salário é de R$ {salario + (salario * 0.10):.2f}.")

if salario <= 1250:
    print(f"O aumento do seu salário foi de R$ {salario * 0.15:.2f} e o valor do seu novo salário é de R$ {salario + (salario * 0.15):.2f}.")