from MyEnum import MyEnum

def fibonacci(my_num):
    if my_num == 0:
        return True
    
    prev_fibo_num = 0
    curr_fibo_num = 1
    while curr_fibo_num < my_num:
        new_prev = curr_fibo_num
        curr_fibo_num += prev_fibo_num
        prev_fibo_num = new_prev
    return curr_fibo_num == my_num

def belongs_to_fibonacci():
    my_input = input(f"QUESTÃO 2 - Para sair, digite 0. Para continuar, qualquer outra tecla:  ")
    while True:
        if my_input == MyEnum.SAIR_QUESTAO.value:
            break

        try:
            my_num = int(input("Digite o seu número para verificar se ele pertence" + 
                        " à sequência de Fibonacci:  "))
            answer = ""
            if my_num < 0:
                answer += "Número negativo. Digite apenas números não negativos."
            elif fibonacci(my_num):
                answer += "O número informado pertence à sequência de Fibonacci.\n\n"
            else:
                answer += "O número informado NÃO pertence à sequência de Fibonacci.\n\n"
            print(answer)          
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número inteiro.")
            continue
        
        my_input = input("0 para sair, qualquer tecla para continuar ~~\n") 