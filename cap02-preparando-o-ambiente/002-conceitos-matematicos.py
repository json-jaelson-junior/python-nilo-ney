"""
### CAPÍTULO 2 ###

Revisão de conceitos matemáticos

Testando os comandos que o autor pediu entre as páginas 77 e 87:
"""

### Propriedades da divisão

# Exemplo de divisão inteira e resto

print(101 // 4) # 25
print( 101 / 4) # 25.25
print( 101 % 4) # 1

# Sinais iguais e diferentes

print(-5 / -2) # 2.5
print(5 / 2) # 2.5
print(5 / -2) # -2.5
print(-5 / 2) # -2.5

# Erro ao dividir por zero

print("10 / 0 = ZeroDivisionError: division by zero")

# Divisões com números reais podem não ter o resultado esperado

print(2 / 5) # 0.4
print(0.6 / 5) # 0.12
print(5 / 0.6) # 8.333333333333334
print(10 / 0.1) # 100.0

# Resto da divisão é 0, indica que o dividendo é divisível pelo divisor.

print(10 % 3) # 1, não é divisível pelo divisor
print(9 % 3 ) # 0, é divisível pelo divisor

### Propriedades da multiplicação

# Multiplicação sinais diferentes

print(5 * -1) # -5
print(-1 * 5) # -5
print(-5 * -1) # 5
print(-3.4 * 1) # 3.4

# A ordem de fatores não altera o produto

print(6 * 2) # 12
print(2 * 6) # 12
print(-4 * 3) # -12
print(3 * -4) # -12
print(10.4 * 8) # -83.2
print(8 * 10.4) # -83.2

# Se o número de fatores negativos é par, o produto é positivo, se ímpar, é negativo

print(1 * -1 * -1) # 1
print(-1 * -1 * -1) # -1
print(3 * -2 * 9) # -54
print(-3 * -2 * 9) # 54
print(-3 * -2 * -9) # -54

### Propriedades de resto

# Cálculo de limites, como por exemplo de 0 a 3, pode ser gerada pelo resdo do número com 4

print(0 % 4) # 0 - Quando o resto é 0, o primeiro número é múltiplo do segundo número
print(1 % 4) # 1
print(2 % 4) # 2
print(3 % 4) # 3
print(4 % 4) # 0
print(5 % 4) # 1
print(6 % 4) # 2
print(7 % 4) # 3
print(8 % 4) # 0

# O módulo (resto) com números reais e negativos também pode ser calculado

print(0.5 % 9) # 0.5
print(11.5 % 9) # 2.5
print(-10 % 9) # 8
print(10 % 9) # 1
print(-5 % 9) # 4

# Quando usamos o módulo com números negativos, o resultado da divisão é arredondado para o próximo valor inteiro

print(-10 % 9) # 8 ou - 10 % 9 = -10 - (9 * -2) = - 10 + 18 = 8

# Média aritmética

print((2 + 4 + 5) / 3) # 3.6666666666666665 - Devemos usar parênteses ou o resultado sairá incorreto
print(2 + 4 + 5 / 3) # 7.666666666666667

# Média ponderada

print(2 * 7 + 9) / 3 # 7.666666666666667
print(6 * 20 + 8 * 30 + 7 * 50) / 100 # 7.1
print(0.2 * 6 + 8 * 0.3 + 7 * 0.5) # 7.1

"""
### EXERCÍCIO ###

Exercício 2.7 - Usando as propriedades da divisão e da multiplicação, tente entender como estes resultados são iguais:

0.2 * 6 + 8 * 0.3 + 7 * 0.5 = (20 * 6 + 8 * 30 + 7 * 50) / 100
"""

# Resolução do exercício:

print("0.2, 0.3 e 0.5 são a mesma coisa de 20, 30 e 50 / 100, por isso, a divisão já foi feita, gerando o mesmo resultado.")