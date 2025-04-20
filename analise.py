# Challenge Alura Store

import pandas as pd
import matplotlib.pyplot as plt

loja_1 = pd.read_csv('./data/loja_1.csv')
loja_2 = pd.read_csv('./data/loja_2.csv')
loja_3 = pd.read_csv('./data/loja_3.csv')
loja_4 = pd.read_csv('./data/loja_4.csv')

lojas = {'Loja 1' : loja_1, 'Loja 2' : loja_2, 'Loja 3' : loja_3, 'Loja 4' : loja_4}
# Faturamento total de cada loja
faturamento_total = {}
def faturamento_por_loja(loja):
    return loja['Preço'].sum()

for loja, i in lojas.items():
    resultado = faturamento_por_loja(i)
    faturamento_total[loja] = resultado

print(faturamento_total)

# Quantidade vendida por categoria em cada loja
qtde_total_produtos_vendidos = {}

def qtde_produtos_por_loja(loja):
   return loja.groupby(['Categoria do Produto']).size()

for loja, i in lojas.items():
    resultado = qtde_produtos_por_loja(i)
    qtde_total_produtos_vendidos[loja] = resultado

print(qtde_total_produtos_vendidos)

# Média de Avaliação por Loja
media_avaliacao = {}

def media_avaliacao_por_loja(loja):
    return loja['Avaliação da compra'].mean().round(3)

for loja, i in lojas.items():
    resultado = media_avaliacao_por_loja(i)
    media_avaliacao[loja] = resultado

print(media_avaliacao)

# Produtos Mais Vendidos por loja
produtos_mais_vendidos = {}

def produtos_mais_vendidos_por_loja(loja):
    nome_produto = loja.idxmax()
    maior_qtde_vendida = loja.max()
    return f'{nome_produto} --> {maior_qtde_vendida}'

for loja, i in qtde_total_produtos_vendidos.items():
    resultado = produtos_mais_vendidos_por_loja(i)
    produtos_mais_vendidos[loja] = resultado

print(produtos_mais_vendidos)

#  Produtos Menos Vendidos por loja

produtos_menos_vendidos = {}

def produtos_menos_vendidos_por_loja(loja):
    nome_produto = loja.idxmin()
    menor_qtde_vendida = loja.min()
    return f'{nome_produto} --> {menor_qtde_vendida}'

for loja, i in qtde_total_produtos_vendidos.items():
    resultado = produtos_menos_vendidos_por_loja(i)
    produtos_menos_vendidos[loja] = resultado

print(produtos_menos_vendidos)

# Frete Médio por Loja

frete_medio = {}

def frete_medio_por_loja(loja):
    return loja['Frete'].mean().round(2)

for loja, i in lojas.items():
    resultado = frete_medio_por_loja(i)
    frete_medio[loja] = resultado

print(frete_medio)

# Gerando gráficos de barra faturamento total das lojas

def grafico_bar(loja,i):
    grafico_barra = plt.bar(loja, i)
    plt.bar_label(grafico_barra, fmt= '%.2f')
    plt.title('Faturamento total por loja')
    plt.ylabel('Faturamento (R$)')
    plt.tight_layout()
    plt.show()
    
grafico_bar(faturamento_total.keys(), faturamento_total.values())


# Gerando gráficos de pizza da quantidade de produtos vendidos por loja

def grafico_piz(loja, i):
    grafico_pizza = plt.pie(i, labels=i.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Participação de Vendas por Categoria - {loja}')
    plt.tight_layout()
    plt.show()

for loja, i in qtde_total_produtos_vendidos.items():
    grafico_piz(loja, i)

# Gráfico de disperção sobre a relação entre Avaliação da Compra e Frete

def grafico_scat(loja, i):
    plt.scatter(i['Avaliação da compra'], i['Frete'])
    plt.title(f'Comparação entre Avaliação da Compra e Frete - {loja}')
    plt.xlabel('Avaliação da compra')
    plt.ylabel('Frete (R$)')
    plt.tight_layout()
    plt.show()

for loja, i in lojas.items():
    grafico_scat(loja, i)
