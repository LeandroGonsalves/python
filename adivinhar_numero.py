x = int(input("Entre com um numero inteiro entre 0 e 1024 -- \n"))
a = 0
b = 1024
test = True
if x == 0:
    print("Seu numero é 0, obrigado por jogar.")
    test = False
else:
    if x == 1024:
        print("Seu numero é 1024, obrigado por jogar.")
        test = False

    while test == True:
        m = int((a+b) / 2)
        if m == x:
            print("Seu numero é ", m, ", obrigado por jogar.")
            break
        else:
            if m < x:
                a = m
            else:
                b = m