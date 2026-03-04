"""
### CAPÍTULO 3 ###

Expressões lógicas

Testando os comandos que o autor pediu na página 99:
"""

### Ordem de avaliação da expressão

"""
Toda expressão será avaliada primeiro por not, depois and e por último or:

1° not: True of False and not True
2° and: True of False and False
3° or: True of False
"""

# Exemplo 1

salario = 1000
idade = 18

print(salario > 1000 and idade > 18) # False
print(100 > 1000 and 20 > 18) # False and True = False

# Exemplo 2

print(salario > 1000 and idade > 18) # False
print(2000  > 1000 and 30 > 18) # True and True = True

"""
### EXERCÍCIOS ###

Exercício 3.4 - Escreva uma expressão para determinar se uma pessoa deve ou não pagar importo.

Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
"""

# Resolução do exercício:

salario = float(1900)
paga_importo = salario > 1200

print(paga_importo) # True

"""
Exercício 3.5 - Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir:

          A       B       C       D

1:        1       2       True    False
2:        10      3       False   False
3:        5       1       True    True
"""

# Resolução do exercício:

a1 = 1
b1 = 2
c1 = True
d1 = False

print(a1 > b1 and c1 or d1) #False

a2 = 10
b2 = 3
c2 = False
d2 = False

print(a2 > b2 and c2 or d2) #False

a3 = 5
b3 = 1
c3 = True
d3 = True

print(a3 > b3 and c3 or d3) #True

"""
Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.

Para ser aprovado, todas as médias do aluno devem ser maiores que 7.

Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
"""

# Resolução do exercício:

materia1 = float(7)
materia2 = float(8)
materia3 = float(6.5)
aprovado_ou_reprovado = materia1 >= 7 and materia2 >= 7 and materia3 >= 7

print(aprovado_ou_reprovado) # False