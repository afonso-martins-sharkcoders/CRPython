def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


def resto(n1, n2):
    return n1 % n2


def potenciar(n1, n2):
    return n1 % n2


while True:

    print("1 - soma ")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    print("5 - potenciar")
    print("6 - resto")

    option = int(input("Insira a opção desejada: "))

    if option == 1:
        n1 = float(input("número 1: "))
        n2 = float(input("número 2: "))
        print(somar(n1, n2))


    elif option == 2:
        n1 = float(input("número 3: "))
        n2 = float(input("número 4: "))
        print(subtrair(n1, n2))


    elif option == 3:
        n1 = float(input("número 5: "))
        n2 = float(input("número 6: "))
        print(multiplicar(n1, n2))


    elif option == 4:
        n1 = float(input("número 7:"))
        n2 = float(input("número 8:"))
        print(dividir(n1, n2))


    elif option == 5:
        n1 = float(input("número 9:"))
        n2 = float(input("número 10:"))
        print(potenciar(n1, n2))


    elif option == 6:
        n1 = float(input("número 11:"))
        n2 = float(input("número 12:"))
        print(resto(n1, n2))

    elif option == 7:
        numero = int(input("Insira um número inteiro"))

        if numero % 2 == 0:
            print("E o numero par")

        else:
            print("E o numero impar")
