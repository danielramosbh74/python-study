# Testes básicos e simples - For e arrays

x = ['123', '456', '789']
valores = []
for val in x:
    valores.append(int(val))
    print(valores)

x = ['123', '456', '789']
valores = []
for val in range(0,len(x)):
    valores.append(int(val))
    print(valores)
    # Não deu certo assim, pois não inseriu os valores de x como números no array valores

# creating an empty list
lst = []

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele) # adding the element
    print(lst)
    print()
print(lst)

""" x = ['123', '456', '789']
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
 """