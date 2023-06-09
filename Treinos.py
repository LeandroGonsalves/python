# Exercicios extraidos do endereço wiki.python.org.br")

print(" 1 - Estrutura sequencial\n")

# Faça um programa que mostre a mensagem "Alô mundo" na tela.

print("EXERCICIO 1")
print("Hello world \n")

# Faça um programa em que o usuário precise digitar um numero
# Se não for numero, dê o alerta e peça para ele digitar somente numero

print("EXERCICIO 2")
while not (n := input('Digite um numero: ')).isdigit():
    print('Valor inválido!')

print("Ok, isso é um numero")

print("EXERCICIO 3")
def adicao(x, y):
    return (x + y)

num1 = (int(input("Digite o primeiro numero\n")))
num2 = (int(input("Digite o segundo numero\n")))

print(num1, "+", num2, "=", adicao(num1, num2))

# faça um Programa que peça as 4 notas bimentrais e mostre a média

print("\n EXERCICIO 4 \n")
nota1 = (int(input("Digite a primeira nota: \n ")))
nota2 = (int(input("Digite a segunda nota: \n ")))
nota3 = (int(input("Digite a terceira nota: \n ")))
nota4 = (int(input("Digite a quarta nota: \n")))

media = (nota1 + nota2 + nota3 + nota4)
md = (media/4)
print("A media é", md)

# Faça um programa que converta metros em centimetros
print("\n EXERCICIO 5 \n")

metros = (float(input("Escreva o numero em metros: \n")))
centimetros = (metros * 100)
print("Este numero tem: ", centimetros, "centimetros")

# Faça um programa que peça o raio de um circulo, calculo e mostre sua área
print("\n EXERCICIO 6 \n")
# area =  pi . raio² //sendo π  aproximadamente  3,14.

pi = 3.14
raio = float(input("Informe o raio do circulo: \n"))
area = (pi * (raio*raio))

print("A área do circulo é", area)

# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
print("\n EXERCICIO 7 \n")

comprimento = float(input("Informe o comprimento em centimetros: \n"))
largura = float(input("Informe a largura em centimetros: \n"))
area = (comprimento * largura)
print("A area tem ", area, "metros")
areaDobro = (area * 2)
print("O dobro da area é", areaDobro)

#  Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhadas no mês
# Calcule e mostre o total do seu salario no referido mês
print("\n EXERCICIO 8 \n")

salarioHora = float(input("Informe seu salario por hora: \n"))
horasTrabalhadas = float(input("Informe as horas trabalhadas no mês: \n"))
total_a_receber = (salarioHora * horasTrabalhadas)
print("Você deverá receber", total_a_receber)

# Faça um Programa que peça a temperatura em Fareinheint, transforme em clesius e imprima o resultado
# Formula C = 5/9 x (F-32)
print("\n EXERCICIO 9 \n")

tempFarh = float(input("Informe a temperatura em Fareinheit: \n"))
celsius = ((5/9)) * (tempFarh - 32)
print("A temperaura em Celsius é: ", celsius)

# Faça um Programa que peça a temperatura em Celsius, transforme em Fareinheint e imprima o resultado
# Formula F = (° C × 9/5) + 32.
print("\n")
print("\n EXERCICIO 10 \n")
tempCelsius = float(input("Informe a temperatura em Celsius: \n"))
farenheit = ((tempCelsius * (9/5)) + 32)
print("A temperaura em Farenheit é: ", farenheit)

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
print("\n EXERCICIO 11 \n")
print("\n")
numInt1 = int(input("Informe o primeiro numero inteiro: \n"))
numInt2 = int(input("Informe o segundo numero inteiro: \n"))
numReal = float(input("Informe o numero real:"))
print("Resposta A")
respA = ((numInt1 * 2) + (numInt2 / 2))
print(respA)
print("\n Resposta B \n")
respB = ((numInt1 * 3) + numReal)
print(respB)
print("\n Resposta C \n")
respC = (numReal ** 3)
print(respC)

# Tendo como dados de entrada a altura de uma pessoa
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58
print("\n EXERCICIO 12 \n")
altura = float(input("Informe sua altura: \n"))
pesoIdeal = ((72.7 * altura) - 58)
print("Seu peso ideal é", pesoIdeal)

# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
print("\n EXERCICIO 13 \n")
altura = float(input("Informe sua altura: \n"))
sexo = input("informe seu sexo: ")
if sexo == "Homem":
    pesoIdeal = ((72.7 * altura) - 58)
    print("Seu peso ideal é", pesoIdeal)
elif sexo == "Mulher":
    pesoIdeal = ((62.1 * altura) - 44.7)
    print("Seu peso ideal é", pesoIdeal)
else:
    print("Informação não encontrada")

print(pesoIdeal)

# Toda vez que um pescador traz um peso de peixes maior que o estabelecido pelo regulamento de pesca (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# Faça um programa que leia a variável pesoPeixe e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa.
# Imprima os dados do programa com as mensagens adequadas
print("\n EXERCICIO 14 \n")

pesoPeixe = float(input("Informe o peso dos peixes pescados: "))
multa = 4
excesso = (pesoPeixe - 50)

if pesoPeixe > 50:
    pagar = (excesso * multa)
    print("O pescador deverá pagar", pagar, "reais de multa")
else:
    print("Não houve excesso de peso")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
print("\n EXERCICIO 15 \n")

salHora = float(input("Informe seu salario por hora: \n"))
hTrab = float(input("Informe as horas trabalhadas no mês: \n"))

salarioBruto = (salHora * hTrab)
print("Seu salário bruto é de: ", salarioBruto, "reais")

print("Descontos:")

impostoDeRenda = (salarioBruto * 0.11)
print(impostoDeRenda, "reais do seu salário vai para o imposto de renda")
sindicato = (salarioBruto * 0.08)
print(sindicato, "reais do seu salário vai para o sindicato")
inss = (salarioBruto * 0.05)
print(inss, "reais do seu salário vai para o inss")

print("Seu salario liquido é de: ", (salarioBruto - impostoDeRenda - sindicato - inss))

# Faça um programa que deverá pedir o tamanho em metros quadrados da área a ser pintada
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total
print("\n EXERCICIO 16 \n")

import math as mt

mq=int(input('tamanho em metros quadrados da area a ser pintada '))

l1 = float(mq/3)

if l1<=18:

 print('1 lata de tinta e o preço é de 80 reais')

else:

 x= mt.ceil(l1/18) # arredonda essa divisão p/cima

 vlatas = x*80

 print('ira precisar de {} latas e o valor é de R$ {} reais'.format(x,vlatas))

