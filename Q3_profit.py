import json

def profit():
    print("QUESTÃO 3\n")

    # Abrir o arquivo fornecido
    with open('dados.json', 'r', encoding='utf-8') as file:
        month_profit = json.load(file)

    min_profit_all = month_profit[0]['valor'] # Sem ignorar dias sem faturamento
    min_profit_all_day = 1

    min_profit = month_profit[0]['valor'] # Ignorando dias sem faturamento
    min_profit_day = 1

    max_profit = month_profit[0]['valor']
    max_profit_day = 1

    sum_profit = 0.0
    profitable_day_amt = 0

    for register in month_profit:
        if register['valor'] < min_profit or min_profit == 0.0: 
            min_profit_all = register['valor']
            min_profit_all_day = register['dia']
            if register['valor'] > 0.0:
                min_profit = register['valor']
                min_profit_day = register['dia']
        elif register['valor'] > max_profit:
            max_profit = register['valor']
            max_profit_day = register['dia']

        # Para cálculo da média
        if register['valor'] > 0.0:
            sum_profit += register['valor']
            profitable_day_amt += 1

    print(f"Menor valor de faturamento, considerando todos os dias: R${round(min_profit_all, 2)}, no dia {min_profit_all_day}\n\n")
    print(f"Menor valor de faturamento ocorrido em um dia do mês (tirando dias sem fat.): R${round(min_profit, 2)}, no dia {min_profit_day}\n\n")
    print(f"Maior valor de faturamento ocorrido em um dia do mês: R${round(max_profit, 2)}, no dia {max_profit_day}\n\n")

    try:
        month_profit_mean = sum_profit / profitable_day_amt
        higher_profit_days_amt = 0
        for register in month_profit:
            if register['valor'] > month_profit_mean:
                higher_profit_days_amt += 1
        print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal (ignorando dias sem faturamento): {higher_profit_days_amt}\n\n")    
    except ZeroDivisionError:
        print("Não há dias com faturamento ou houve algum erro no processamento dos dados (divisão por zero).\n")