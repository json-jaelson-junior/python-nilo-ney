"""
CAPÍTULO 3

Operadores relacionais

Testando os comandos que o autor pediu nas páginas 94 e 95:
"""

### Tabela de operadores relacionais

"""
    Operador        Operação

       ==           Igualdade
       >            Maior que
       <            Menor que
       !=           Diferente
       >=           Maior ou igual
       <=           Menor ou igual
"""

# Exemplo 1

a = 1
b = 5
c = 2
d = 1

print(a == b) # False
print(b > a) # True
print(a < b) # True
print(a == d) # True
print(b >= a) # True
print(c <= b) # True
print(d != a) # False
print(d != b) # True

# Exemplo 2

nota = 8
media = 7
aprovado = nota >= media

print(aprovado) # True

"""
### EXERCÍCIO

Exercício 3.2 - Complete a tabela a seguir, respondendo True ou False.

Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

    Expressão       Resultado
    
    a == c          True ou False
    a < b           True ou False
    d > b           True ou False
    c != f          True ou False
    a == b          True ou False
    c < d           True ou False
    b > a           True ou False
    c >= f          True ou False
    f >= c          True ou False
    c <= c          True ou False
    c <= f          True ou False
"""

#Resolução do exercício:

a = 4
b = 10
c = 5.0
d = 1
f = 5

print(a == c) # False
print(a < b) # True
print(d > b) # False
print(c != f) # False
print(a == b) # False
print(c < d) # False
print(b > a) # True
print(c >= f) # True
print(f >= c) # True
print(c <= c) # True
print(c <= f) # True