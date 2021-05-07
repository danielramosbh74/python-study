# Original em Linux Shell Bash
#!/bin/bash
#
# Esta é uma função matemática com 2 argumentos
# somar(){
# soma=$(($1+$2))
# return $soma
# }
#
# echo "Este script simples somará 2 números"
# read -p "Digite o primeiro número: " int1
# read -p "Digite o segundo número: " int2
# somar $int1 $int2
# echo "A soma é: " $?
#
# Para executar este script digite em um terminal Linux digite na pasta onde o arquivo foi salvo:
# sudo ./soma_de_2_numeros_digitados.sh






# Convertido manualmente para Python3

# Não precisamos criar uma função com 2 argumentos neste caso, 
# pois somar é uma operação aritmética básica, então conseguimos fazer isso
# apenas somando as 2 variáveis que entramos pelo teclado e atribuindo o resultado
# a uma outra variável

print ("Este script simples somará 2 números")
string1 = input ("Digite o primeiro número: ")
string2 = input ("Digite o segundo número: ")
soma = int(string1) + int(string2)
# O comando input insere os dados como strings, 
# então precisamos convertê-los em números inteiros se quisermos fazer cálculos com eles
print ("A soma é: ", soma) 

# Para executar este script digite em um terminal Linux digite na pasta onde o arquivo foi salvo:
# sudo ./soma_de_2_numeros_digitados.sh

# Podemos fazer isso de outra forma, entrando com uma "lista de 2 números"
# e usando a função pré-definida sum



x = ['123', '456', '789']
valores = []
for val in x:
    valores.append(int(val))




print()
print('------')
print()

print ("Outro script simples que somará 2 números")
# creating an empty list
lst = []
  
# number of elemetns as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)

print ("A soma é dos elementos da lista é: ", sum(lst))
media = sum(lst) / len(lst)
print("Média: ", media)

mediana = sum(lst) / 2
print("Mediana: ", mediana)


# Para executar este script digite em um terminal Linux digite na pasta onde o arquivo foi salvo:
# sudo ./soma_de_2_numeros_digitados.sh
