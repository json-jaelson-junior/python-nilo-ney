"""
CAPÍTULO 3

Variáveis numéricas e representação de valores numéricos

Testando os comandos que o autor pediu nas páginas 90, 91 e 93:
"""

### Variáveis numéricas

# Separando milhas e ponto flutuante

print(1_000) # mil
print(1_000_000) # um milhão
print(1_0_0) # cem, é válido, mas pouco utilizado
print(1_980.10) # 1980.1, _ pode ser combinado com ponto
print(1980.1) # 1980.1

"""
### EXERCÍCIO

Exercício 3.1 - Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado:

    Número          Tipo numérico

    5               Inteiro - Ponto flutuante
    5.0             Inteiro - Ponto flutuante
    4.3             Inteiro - Ponto flutuante
    -2              Inteiro - Ponto flutuante
    100             Inteiro - Ponto flutuante
    1.33            Inteiro - Ponto flutuante
"""

# Resolução do exercício:

print("números inteiros = 5, -2, 100")
print("ponto flutuante = 5.0, 4.3, 1.333")

### Representação de valores numéricos

a = 0b11 # Base 2 - binário
b = 0x11 # Base 16 - hexadecimal
c = 0o11 # Base 9 - octal

print(a, b, c) # 3, 17, 9