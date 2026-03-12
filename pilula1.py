import math
#entrada 
assinantes = int(input('assinantes atuais: '))
mensalidades = float(input('valor da mensalidade'))
taxa = float(input('Taxa de ccrescimento mensal(%): '))/100
meses = int(input('meses de projeção: '))
#processamento
assinantes_finais = assinantes * math.pow ((1+taxa), meses)
receita_final = assinantes_finais * mensalidades
#saida
print(f'asisnantes estimados;{assinantes_finais:.0f}')
print(f'Receitas mensal estimados;{receita_final:.2f}')