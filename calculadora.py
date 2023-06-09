import math
print("********** Calculadora **********\n")

contador = 0
decida = int(input("Digite 0 para usar a calculadora ou 1 para ver uma tabuada: \n"))

if decida > 0:
    numero = int(input("Digite o numero da tabuada: "))
    while contador <= 10:
      resultado = int((numero * contador))
      print(numero, "X", contador, " =", resultado)
      contador = int(contador + 1)

else:
    print("Selecione a opção desejada \n")
    print('1 - soma')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')
    print('5 - potência')
    print('6 - raiz quadrada')

    def adicao(x, y):
        return x + y

    def subtracao(x, y):
        return x - y

    def multiplicacao(x, y):
        return x * y

    def divisao(x, y):
        return x / y

    def potencia(x, y):
        return x ** y

    def raizQuadrada(x):
        return x

    escolha = input("\nDigite sua opção: 1 / 2 / 3 / 4 / 5 / 6: \n")

    if escolha == '6':
        raiz = int(input("Digite o numero: "))
        print(raiz, "=", math.sqrt(raiz))

    elif escolha == '5':
        base = int(input("Digite a base: \n"))
        expoente = int(input("Digite o expoente"))
        print(base, "^", expoente, "=", potencia(base, expoente))

    else:
        num1 = int(input('Digite o primeiro numero da operação\n'))
        num2 = int(input('\nDigite o segundo numero da operação\n'))

        if escolha == '1':
            print(num1, "+", num2, "=", adicao(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))

        else:
            print("opção inválida")