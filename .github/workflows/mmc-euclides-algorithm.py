# Adapted from: 
# https://www.ime.usp.br/~macmulti/exercicios/inteiros/12Python.html
# https://pt.stackoverflow.com/questions/237169/programa-pra-achar-o-mmc-em-python
# https://pt.wikipedia.org/wiki/Algoritmo_de_Euclides
# https://python.nilo.pro.br/

# Solution 1

# num1 = int(input("Digite um número inteiro:"))
# num2 = int(input("Digite outro número inteiro:"))

# if num1 > num2:
#     maior = num1
# else:
#     maior = num2
# while True:
#     if maior % num1 == 0 and maior % num2 == 0:
#         print(maior)
#         break
#     else:
#         maior += 1

# Solution 2 (Using For loop instead of While)

# num1 = int(input("Digite um número inteiro:"))
# num2 = int(input("Digite outro número inteiro:"))

# if num1 > num2:
#     maior = num1
# else:
#     maior = num2

# for i in range(maior):
#     aux = num1 * i
#     if (aux % num2) == 0:
#         mmc = aux

# print(mmc)


## BEST SOLUTION!!

##############################################################################
# Parte do livro IntroduÃ§Ã£o Ã  ProgramaÃ§Ã£o com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2024
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 08\exercicio-08-08.py
##############################################################################

# def mdc(a, b):
#     if b == 0:
#         return a
#     return mdc(b, a % b)


# def mmc(a, b):
#     return abs(a*b) / mdc(a, b)


# print(f"MMC 10 e 5 -->  {mmc(10, 5)}")
# print(f"MMC 32 e 24 --> {mmc(32, 24)}")
# print(f"MMC 5 e 3 -->   {mmc(5, 3)}")

## BEST SOLUTION ADAPTED TO ENTER ANY NUMBER AS COMMAND LINE ARGUMENTS IN FUNCTION

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    return abs(a*b) / mdc(a, b)


print(f"MMC 32 and 24 --> {mmc(32, 24)}")
print(f"MDC 32 and 24 --> {mdc(32, 24)}")

print()

print(f"MMC 20 and 30 --> {mmc(20, 30)}")
print(f"MDC 20 and 30 --> {mdc(20, 30)}")

print()

a_argument = int(input('Type "a": '))
b_argument = int(input('Type "b": '))

print("MMC a and b --> ", mmc(a_argument, b_argument))
print()
print("MDC a and b --> ", mdc(a_argument, b_argument))
