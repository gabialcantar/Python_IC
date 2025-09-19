print('Seja bem-vindo ao programa de consumo eficiente')

# Primeiro: perguntar o tempo gasto na viagem (em horas)
tempo = float(input('Qual foi o tempo gasto na viagem (em horas)? '))

print('O seu tempo gasto foi:', tempo, 'hora(s)')

# Agora: perguntar a velocidade média (em km/h)
velocidade = float(input('Qual foi a sua velocidade média (em km/h)? '))

print('A sua velocidade média foi de:', velocidade, 'km/h')

# Calcular a distância
distancia = tempo * velocidade
print('A distância percorrida foi:', distancia, 'km')

# Calcular litros gastos
litros = distancia / 12
print('A quantidade de litros utilizada foi:', litros, 'litros')

# Resumo final
print(f'\nResumo da viagem:')
print(f'⏱️ Tempo: {tempo} h')
print(f'🚗 Velocidade média: {velocidade} km/h')
print(f'📏 Distância: {distancia} km')
print(f'⛽ Combustível gasto: {litros:.2f} litros')
