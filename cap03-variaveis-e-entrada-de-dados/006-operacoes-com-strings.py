"""
CAPÍTULO 3

Operações com strings

Testando os comandos que o autor pediu entre as páginas 102 e 108:
"""

### Concatenação

s = "ABC"

print(s + "C") # ABCC
print(s + "D" * 4) # ABCDDDD
print("X" + "-" * 10 + "X") # X----------X
print(s + "x4 = " + s * 4) # ABCx4 = ABCABCABCABC

# Esta forma de concatenação só pode ser usada com strings o exemplo abaixo daria erro:

"""
nome = "tião"
idade = 10

print(nome + idade) = TypeError:can only concatenate str (not "int") to str
"""

### Composição

# Marcadores

"""
    Marcador        Tipo

    %d          Números inteiros
    %s          Strings
    %f          Números decimais
"""

# Exemplos marcador %d

idade = 22

print("[%d]" % idade) # [22]
print("[%03d]" % idade) # [022]
print("[%3d]" % idade) # [ 22]
print("[%-3d]" % idade) # [22 ]

# Exemplos marcador %f

print("%5f" % 7) # [7.000000]
print("%5.2f" % 7) # [ 7.00]
print("%10.5f" % 7) # [   7.00000]

# Exemplos com todos os marcadores; %s, %d e %f

nome = "João"
idade = 22
grana = 51.34

print("%s tem %d anos e R$ %f no bolso." % (nome, idade, grana))
# [João tem 22 anos e R$ 51.340000 no bolso.]
print("%12s tem %3d anos e R$ %5.2f no bolso." % (nome, idade, grana))
# [        João tem  22 anos e R$ 51.34 no bolso.]
print("%12s tem %03d anos e R$ %5.2f no bolso." % (nome, idade, grana))
# [        João tem 022 anos e R$ 51.34 no bolso.]
print("%-12s tem %-3d anos e R$ %-5.2f no bolso." % (nome, idade, grana))
# [João         tem 22  anos e R$ 51.34 no bolso.]

### .format

nome = "João"
idade = 22
grana = 51.34

print("{} tem {} anos e R$ {} no bolso.".format(nome, idade, grana))
# [João tem 22 anos e R$ 51.34 no bolso.]
print("{:12} tem {:3} anos e R$ {:5.2f} no bolso.".format(nome, idade, grana))
# [João         tem  22 anos e R$ 51.34 no bolso.]
print("{:12} tem {:03} anos e R$ {:5.2f} no bolso.".format(nome, idade, grana))
# [João         tem 022 anos e R$ 51.34 no bolso.]
print("{:<12s} tem {:<3} anos e R$ {:5.2f} no bolso.".format(nome, idade, grana))
# [João         tem 22  anos e R$ 51.34 no bolso.]

# .format também suporta o uso da posição dor parâmetros dentro de colchetes

print("{1} {0} {2}".format("a", "b", "c")) # b a c, a ordem é definida pela ordem dos índices dadas aos parâmetros

# Podemos repetir um parâmetro dentro da máscara

print("{2} {2} {0} {1}".format("a", "b", "c")) # c c a b

### f-string

nome = "João"
idade = 22
grana = 51.34

print(f"{nome} tem {idade} anos e R$ {grana} no bolso.")
# [João tem 22 anos e R$ 51.34 no bolso.]
print(f"{nome:12} tem {idade:3} anos e R$ {grana:5.2f} no bolso.")
# [João         tem  22 anos e R$ 51.34 no bolso.]
print(f"{nome:12} tem {idade:03} anos e R$ {grana:5.2f} no bolso.")
# [João         tem 022 anos e R$ 51.34 no bolso.]
print(f"{nome:<12s} tem {idade:<3} anos e R$ {grana:5.2f} no bolso.")
# [João         tem 22  anos e R$ 51.34 no bolso.]

### Fatiamento de strings

# O número a esquerda dos dois pontos indica o início, o da direita indica o final
# O conteúdo exibido será sempre o número da esquerda até o número da direita -1

# Exemplos

s = "ABCDEFGHI"

print(s[0:2]) # AB
print(s[1:2]) # B
print(s[2:4]) # CD
print(s[0:5]) # ABCDE
print(s[1:8]) # BCDEFGH

# Também podemos omitir um dos dois números, aplicando apenas para um dos lados

print(s[:2]) # AB
print(s[1:]) # BCDEFGHI
print(s[:]) # ABCDEFGHI

# Também podemos utilizar valores negativos, dessa forma -1 é o último caractere, -2 o penúltimo, etc

print(s[0:-2]) # ABCDEFG
print(s[-1:]) # I
print(s[-5:7]) # EFG
print(s[-2:-1]) # H

# Inversão utilizando um terceiro parâmetro, com número negativo

print(s[::-1]) # IHGFEDCBA

# Utilizando o terceiro parâmetro com um número positivo, determina o intervalo entre os elementos

print(s[::2]) # ACEGI