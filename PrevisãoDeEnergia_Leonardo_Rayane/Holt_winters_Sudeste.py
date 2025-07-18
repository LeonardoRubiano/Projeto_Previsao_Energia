import pandas as pd
import matplotlib.pyplot as plt

def holt_winters_multiplicativo(series, L, alpha, beta, gamma, h):
    """
    Implementação do método Holt-Winters Multiplicativo do zero.

    :param series: lista de valores da série temporal
    :param L: comprimento do período sazonal (ex: 12 para dados mensais)
    :param alpha: parâmetro de suavização para o nível (0 < alpha < 1)
    :param beta: parâmetro de suavização para a tendência (0 < beta < 1)
    :param gamma: parâmetro de suavização para a sazonalidade (0 < gamma < 1)
    :param h: número de passos à frente para prever
    :return: lista com os h valores previstos
    """
    # 1. Verificação inicial
    if len(series) < L:
        raise ValueError("A série temporal precisa ter pelo menos um ciclo sazonal completo (L).")

    # 2. Inicialização
    nivel_anterior = sum(series[0:L]) / L
    tendencia_anterior = (sum(series[L:2*L]) - sum(series[0:L])) / L**2 if len(series) >= 2*L else (series[L-1] - series[0]) / (L-1)
    
    fatores_sazonais = []
    # Divide cada valor do primeiro ciclo pela média do ciclo para obter os fatores
    for i in range(L):
        fatores_sazonais.append(series[i] / nivel_anterior)
    
    # Lista para armazenar os valores ajustados (para referência)
    ajustados = [] 
    
    # 3. Loop iterativo para calcular nível, tendência e sazonalidade
    for t in range(L, len(series)):
        valor_atual = series[t]
        
        # Último fator sazonal correspondente (do ciclo anterior)
        fator_sazonal_anterior = fatores_sazonais[t-L]

        # Cálculo do Nível
        nivel_atual = alpha * (valor_atual / fator_sazonal_anterior) + (1 - alpha) * (nivel_anterior + tendencia_anterior)
        
        # Cálculo da Tendência
        tendencia_atual = beta * (nivel_atual - nivel_anterior) + (1 - beta) * tendencia_anterior
        
        # Cálculo da Sazonalidade
        fator_sazonal_atual = gamma * (valor_atual / nivel_atual) + (1 - gamma) * fator_sazonal_anterior
        
        # Adiciona o novo fator sazonal à lista
        fatores_sazonais.append(fator_sazonal_atual)
        
        # Atualiza as variáveis para a próxima iteração
        nivel_anterior = nivel_atual
        tendencia_anterior = tendencia_atual
        
        # Adiciona o valor ajustado (previsão de 1 passo)
        ajustados.append((nivel_anterior + tendencia_anterior) * fator_sazonal_anterior)

    # 4. Previsão para h passos à frente
    previsao = []
    for i in range(h):
        # O índice do fator sazonal é pego do último ciclo completo conhecido
        indice_sazonal = len(series) - L + i
        
        valor_previsto = (nivel_anterior + (i + 1) * tendencia_anterior) * fatores_sazonais[indice_sazonal]
        previsao.append(valor_previsto)
        
    return previsao, ajustados


# --- SCRIPT PRINCIPAL ---



dados_consumo_sudeste = [
    # 2021
    6604401, 6235408, 6357289, 6390169, 5526107, 5549613, 5404190, 5472932, 5975072, 5758807, 5674137, 6024669,
    # 2022
    5992623, 6037501, 6641314, 6255459, 5701319, 5493254, 5538689, 5545784, 5694638, 5755198, 5951934, 6316138, 
    # 2023
    5855814, 6333221, 6529244, 6888977, 5936009, 5838541, 5751791, 5929765, 6212348, 6607791, 6880970, 7080334
]

# Parâmetros definidos pelo usuário
ALPHA = 0.3
BETA = 0.1
GAMMA = 0.2
L = 12 # Ciclo sazonal de 12 meses
H = 12 # Prever os próximos 12 meses (2024)

# Chamar a função para obter a previsão 
previsao_2024_sudeste, _ = holt_winters_multiplicativo(dados_consumo_sudeste, L, ALPHA, BETA, GAMMA, H)


# Exibir os resultados 

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

#Norte 
print("Resultados para região Sudeste")
for i in range(len(previsao_2024_sudeste)):
    print(f"{meses[i]} de 2024: {previsao_2024_sudeste[i]:.1f}")


# --- Visualização ---

# Criar a série histórica 
indice_historico = pd.date_range(start='2021-01-01', periods=len(dados_consumo_sudeste), freq='MS')
serie_historica = pd.Series(dados_consumo_sudeste, index=indice_historico)


# 1. Pegar o último ponto da série histórica para ser o ponto de conexão
ponto_de_conexao_indice = serie_historica.index[-1]
ponto_de_conexao_valor = serie_historica.iloc[-1]
ponto_de_conexao = pd.Series([ponto_de_conexao_valor], index=[ponto_de_conexao_indice])

# 2. Criar a série de previsão 
indice_previsao = pd.date_range(start='2024-01-01', periods=H, freq='MS')
serie_previsao = pd.Series(previsao_2024_sudeste, index=indice_previsao)

# 3. Concatenar o ponto de conexão com a série de previsão
serie_previsao_continua = pd.concat([ponto_de_conexao, serie_previsao])

# Plotar os resultados
plt.figure(figsize=(14, 7))
plt.plot(serie_historica, label='Dados Históricos (2021-2023)', color='orange')

# Plotar a nova série de previsão contínua
plt.plot(serie_previsao_continua, label='Previsão Holt-Winters (2024)', linestyle='--', color='red')

plt.title('Previsão de Consumo de Energia com Holt-Winters (Sudeste)')
plt.xlabel('Ano')
plt.ylabel('Consumo (MWh/mês)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
