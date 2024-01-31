while True:

    idade = int(input("Insira a sua idade "))

    if idade >= 18:
        print("Pode votar")

    elif idade < 18 and idade >= 0:
        print("Não pode votar")

    elif idade < 0:
        print("Não pode ter uma idade negativa")

    else:
        print("Opção invalida")
