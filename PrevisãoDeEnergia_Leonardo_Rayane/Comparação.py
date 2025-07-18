import matplotlib.pyplot as plt

#Listas com os dados reais

NorteR= [1122689, 1087908, 1084094, 1117881, 1136247, 1117165, 1143776, 1200943, 1274834, 1320869, 1258922, 1222897]
NordesteR= [3168933, 3098896, 3082552, 3153214, 3106169, 2997394, 2757151, 2839556, 2954096, 2966217, 3170640, 3244577]
SudesteR= [7069136, 6886915, 7260103, 6721233, 6872360, 6358441, 6056893, 6140575, 6386658, 6932033, 6532052, 6859871]
SulR= [2703760, 2770449, 2750929, 2572691, 2330962, 2264676, 2239193, 2334292, 2215836, 2278504, 2387957, 2432536]
Centro_OesteR= [1381913, 1353531, 1422776, 1382255, 1396686, 1232245, 1194277, 1229234, 1377488, 1581633, 1443059, 1470025]


#Listas com os dados previstos

Norte = [1069388.3, 1031545.9, 1075318.2, 1131808.8, 1144029.0, 1204200.7, 1180011.1, 1269998.2, 1361242.5, 1367395.9, 1349540.0, 1337454.9]
Nordeste =  [3083885.1, 2967321.9, 3113896.8, 3129456.3, 2979999.3, 2935837.5, 2863863.2, 2884281.0, 3108189.6, 3150614.7, 3212035.2, 3356302.6]
Sudeste = [7420691.5, 7327921.2, 7616157.5, 7688974.7, 6727686.6, 6737067.5, 6653632.6, 6791339.2, 7367159.7, 7321142.5, 7345522.7, 7772643.2]
Sul = [2623238.7, 2539907.6, 2589700.2, 2441885.5, 2195666.6, 2222666.7, 2317078.9, 2335851.4, 2230822.8, 2290128.2, 2359093.9, 2563802.4]
Centro_Oeste = [1441386.1, 1381128.2, 1465712.7, 1524695.5, 1400404.8, 1443036.4, 1338900.3, 1384140.9, 1668205.9, 1736662.8, 1639614.6, 1720732.0]


#Função que calcula o erro relativo
def erro_relativo(valor_medido,valor_real):
    erro_absoluto = abs(valor_medido - valor_real)
    erro_relativo = erro_absoluto/abs(valor_real)

    return erro_relativo



#Função que cria uma lista com os erros de cada região
def lista_de_erros(Lista_medida, Lista_real):
    lista_de_erros = []
    for i in range(len(Lista_medida)):
        erro_relativo_i = erro_relativo(Lista_medida[i], Lista_real[i])
        lista_de_erros.append(erro_relativo_i)
    
    return lista_de_erros

#Criando as listas com os erros de cada região
erro_Norte= lista_de_erros(Norte, NorteR)
erro_Nordeste= lista_de_erros(Nordeste, NordesteR)
erro_Sudeste= lista_de_erros(Sudeste, SudesteR)
erro_Sul= lista_de_erros(Sul, SulR)
erro_Centro_Oeste= lista_de_erros(Centro_Oeste, Centro_OesteR)

#Mostrando os resultados
print("Erros relativos na Região Norte: " + str(erro_Norte))
print("\nErros relativos na Região Nordeste: " + str(erro_Nordeste))
print("\nErros relativos na Região Sudeste: " + str(erro_Sudeste))
print("\nErros relativos na Região Sul: " + str(erro_Sul))
print("\nErros relativos na Região Centro-Oeste: " + str(erro_Centro_Oeste))


#---- Gráfico ----
# Cria os índices para o eixo X (assumindo que são períodos de tempo sequenciais)
indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Cria a figura e os eixos para o gráfico
plt.figure(figsize=(12, 7))

# Plota os dados da lista NorteR (Reais)
plt.plot(indices, NorteR, marker='o', linestyle='-', color='blue', label='Norte - Reais (NorteR)')

# Plota os dados da lista Norte (Previstos)
plt.plot(indices, Norte, marker='x', linestyle='--', color='red', label='Norte - Previstos')

# Adiciona título e rótulos aos eixos
plt.title('Comparativo: Valores Reais vs. Previstos - Região Norte')
plt.xlabel('Período')
plt.ylabel('Valores')

# Adiciona uma grade para melhor visualização
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adiciona a legenda para identificar as linhas
plt.legend()

# Formata os rótulos do eixo Y para melhorar a legibilidade
plt.gca().get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, p: format(int(x), ','))
)
plt.xticks(indices) # Garante que todos os períodos sejam mostrados no eixo X

# Exibe o gráfico
plt.tight_layout()
plt.show()


    
    