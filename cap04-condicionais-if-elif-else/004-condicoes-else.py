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