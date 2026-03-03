"""
CAPÍTULO 3

Operadores lógicos

Testando os comandos que o autor pediu nas páginas 96, 97 e 98:
"""

### Tabela de operadores lógicos

"""
    Operador Python     Operação
        
        not               não
        and               e
        or                ou
"""

### Operador not

"""
    V           not V

    True        False
    False       True
"""

# Exemplo

print(not True) # False
print(not False) # True

### Operador and

"""
    V1          V2          V1 e V2

    True        True        True
    True        False       False
    False       True        False
    False       False       False
"""

# Exemplo

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

### Operador or

"""
    V1          V2          V1 ou V2

    True        True        True
    True        False       True
    False       True        True
    False       False       False
"""

# Exemplo

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

"""
### EXERCÍCIO

Exercício 3.3 - Complete a tabela a seguir utilizando a = True, b = False e c = True.

    Expressão       Resultado

    a and b         True ou False
    b and b         True ou False
    not c           True ou False
    not b           True ou False
    not a           True ou False
    a and b         True ou False
    b and c         True ou False
    a or c          True ou False
    b or c          True ou False
    c or a          True ou False
    c or b          True ou False
    c or c          True ou False
    b or b          True ou False
"""

# Resolução do exercício:

a = True
b = False
c = True

print(a and a) # True
print(b and b) # False
print(not c) # False
print(not b) # True
print(not a) # False
print(a and b) # False
print(b and c) # False
print(a or c) # True
print(b or c) # True
print(c or a) # True
print(c or b) # True
print(c or c) # True
print(b or b) # False