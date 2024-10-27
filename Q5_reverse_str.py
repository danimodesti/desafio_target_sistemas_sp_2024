from MyEnum import MyEnum

def reversing(str):
    new_s = ""

    for c in str:
        new_s = c + new_s
    return new_s

def reverse_str():
    my_input = input(f"QUESTÃO 5 - Para sair, digite 0. Para continuar, qualquer outra tecla:  ")
    while True:
        if my_input == MyEnum.SAIR_QUESTAO.value:
            break

        my_str = input("Digite sua string para reverter:  ")

        reversed_str = reversing(my_str)

        print(f"String reversa: {reversed_str}\n")

        my_input = input("0 para sair, qualquer tecla para continuar ~~\n") 