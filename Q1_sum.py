def sum():
    print("QUESTÃO 1\n")

    indice = 13
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    print(soma) # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 = 91
    print("\nPodemos executar o código e perceber que o valor da" + 
          f" variável soma, ao final, será de {soma}.")