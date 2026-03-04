"""
### CAPÍTULO 4 ###

Condições - If 01

Testando os comandos que o autor pediu nas páginas 118, 119 e 120:
"""

### If

# If nada mais é do que um "se"; se a condição for verdadeira, faça tal coisa

### Programa 4.1: Lê dois valores e imprime qual é o maior

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b: #1
    print("O primeiro valor é maior!") #2

if b > a: #3
    print("O segundo valor é maior!") #4

"""
### EXERCÍCIO ###

Exercício 4.1 - Analise o Programa 4.1. Responda o que acontece se o primeiro e o segundo valor forem iguais? Explique.
"""

# Resolução do exercício:

print("Como as condições pedem que um número seja maior que o outro para ser exibido, nada será exibido na tela.")