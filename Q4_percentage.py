def percentage():
    print("QUESTÃO 4\n")
    profit_participation = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total_profit = 0.00
    for state in profit_participation:
        total_profit += profit_participation[state]

    print(f"O faturamento total foi de {round(total_profit, 2)}.")
    for state in profit_participation:
        representation_percentage = profit_participation[state] * 100 / total_profit
        print(f"O percentual de representação de {state}, de faturamento R${profit_participation[state]}, foi de {round(representation_percentage, 2)}%.\n\n")