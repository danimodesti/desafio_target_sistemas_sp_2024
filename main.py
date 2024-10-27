from MyEnum import MyEnum

from Q1_sum import sum
from Q2_belongs_to_fibo import belongs_to_fibonacci
from Q3_profit import profit
from Q4_percentage import percentage
from Q5_reverse_str import reverse_str

def main():
    print("Olá, meu nome é Danielle e este é o meu teste técnico para a Target Sistemas SP!\n")

    question = None
    while question != MyEnum.SAIR.value:
        try:
            question = int(input("\n\nEscolha uma das perguntas para ver as respostas, ou 0 para sair:  "))
        except ValueError:
            print("Pergunta inválida. Tente de novo.\n")
            continue

        if question == MyEnum.PERGUNTA_1.value:
            sum()
        elif question == MyEnum.PERGUNTA_2.value:
            belongs_to_fibonacci()
        elif question == MyEnum.PERGUNTA_3.value:
            profit()
        elif question == MyEnum.PERGUNTA_4.value:   
            percentage()
        elif question == MyEnum.PERGUNTA_5.value:
            reverse_str()
        elif question == MyEnum.SAIR.value:
            print("OK, obrigada por executar meu programa :)")
            break
        else:
            print("Pergunta inválida. Tente de novo.\n")

if __name__ == "__main__":
    main()