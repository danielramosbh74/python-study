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

# Esta é uma função matemática com 2 argumentos
somar(){
soma=numero1+numero2
return soma
}

echo "Este script simples somará 2 números"
read "Digite o primeiro número: " int1
read "Digite o segundo número: " int2
somar (int1, int2)
echo "A soma é: " somar

# Para executar este script digite em um terminal Linux digite na pasta onde o arquivo foi salvo:
# sudo ./soma_de_2_numeros_digitados.sh
