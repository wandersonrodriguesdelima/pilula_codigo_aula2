import statistics as st
lote1 = int(input('Produção lote1:'))
lote2 = int(input('Produção lote2:'))
lote3 = int(input('Produção lote3:'))
media = st.mean((lote1,lote2,lote3))
desvio = st.stdev ((lote1,lote2,lote3))
print(f'Média:{media:.2f} ')
print(f'Desvio padrão {desvio: 2f}')
