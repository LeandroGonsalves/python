from random import choice

with open('word.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

print("\n>>>>>>>>>>BEM-VINDO(A) AO JOGO DA FORCA!<<<<<<<<<<\n")
print("Sua vida corre perigo e você será desafiado(a)!\n")
print("Para escapar, basta adivinhar a palavra secreta\n")

palavra = choice(lista_de_palavras).upper()

forca = '''
------
     |
     |
     |
     |
     -
'''

vazio = '''
'''

cabeca = '''
------
 o   |
     |
     |
     |
     -
'''

tronco = '''
------
 o   |
 |   |
     |
     |
     -
'''

pernadireita = '''
------
 o   |
 |   |
/    |
     |
     -
'''

pernaesquerda = '''
------
 o   |
 |   |
/ \\  |
     |
     -
'''
bracodireito = '''
------
 o   |
/|   |
/ \\ |
     |
     -
'''

bracoesquerdo = '''
------
 o   |
/|\\ |
/ \\ |
     |
     -
'''

chancesdoboneco = [forca, cabeca, tronco, pernadireita, pernaesquerda, bracodireito, bracoesquerdo]
acertos = 0
erros = 0
letrasAcertadas = ' '
letrasErradas = ' '

while acertos != len(palavra) and erros != 6:
    mensagem = ''
    for letra in palavra:
        if letra in letrasAcertadas:
            mensagem += f'{letra }'
        else:
            mensagem += '_ '
    print(chancesdoboneco[erros])
    print(mensagem)

    letra = input("\nDigite uma letra: ").upper()

    if letra in letrasAcertadas + letrasErradas:
        print("\n>>>Você já tentou essa letra<<<\n")
        continue

    if letra in palavra:
        print("\n***Letra certa***\n")
        letrasAcertadas += letra
        acertos += palavra.count(letra)

    else:
        print("\nVish! Letra errada\n")
        letrasErradas += letra
        erros += 1
        print("\n>>>Se deu mal HAHAHA!<<<\n")


print("\nA palavra é: ", palavra)