# Mesclando informações de algumas fontes para obter um resultado melhor


# Fonte 1: https://www.horadecodar.com.br/2020/08/12/como-converter-string-para-int-em-python/

numeroEmString = input ("Digite um número ")

print(type(numeroEmString))

numero = int(numeroEmString)

print(type(numero))

print('O dobro do número digitado e já convertido de string para inteiro é: ', numero * 2)


# Fonte 2: https://pt.stackoverflow.com/questions/301022/converter-uma-lista-de-string-em-uma-lista-de-n%C3%BAmeros-inteiros


x = ['123', '456', '789']
valores = []
for val in x:
    valores.append(int(val))

media = sum(valores) / len(valores)
print(media)

mediana = sum(valores) / 2
print(mediana)

valores.sort()
min = valores[0] # Primeiro valor da lista
print(min)

max = valores[-1] # Ultimo valor da lista
print(max)

# Fonte 3: https://pt.stackoverflow.com/questions/364387/problema-com-entrada-de-mais-de-um-n%C3%BAmero-inteiro-com-input

"""Perceba que você deve fazer uma checagem antes para garantir que é um numero que esta vindo pela entrada, isto é feito pela função isdigit().

Veja abaixo o exemplo:
"""

numeros = [int(v) for v in input('Valores: ').split() if v.isdigit()]
print(numeros)

"""
Entrada:

1 32 3 55

Saída:

[1, 32, 3, 55]

A saída é uma lista de números inteiros que foram retornados separadamente por int(v) através da list comprehension, seguindo da condição especificada isdigit(s) que simplesmente verifica se o valor é um digito.

"""


# Mesclagem e minha edição para obter um resultado final melhor, entrando com os dados da lista pelo teclado
# Depois pretendo transformar este mesmo exemplo em um Teste Unitário


valores = [int(v) for v in input('Valores: ').split() if v.isdigit()]
print(valores)

media = sum(valores) / len(valores)
print(media)

mediana = sum(valores) / 2
print(mediana)

valores.sort()
min = valores[0] # Primeiro valor da lista
print(min)

max = valores[-1] # Ultimo valor da lista
print(max)

"""
SAÍDA:
Digite um número 5
<class 'str'>
<class 'int'>
456.0
684.0
123
789
Valores: 123 456 789
[123, 456, 789]
Valores: 000 111 222
[0, 111, 222]
111.0
166.5
0
222
"""

