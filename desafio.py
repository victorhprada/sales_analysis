import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja1 = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

print(loja1.head())

## Faturamento de cada loja

total_loja = loja1['Preço'].sum()
print(f"Valor total da loja: R$ {total_loja:,.2f}")

total_loja2 = loja2['Preço'].sum()
print(f"Valor total da loja: R$ {total_loja2:,.2f}")

total_loja3 = loja3['Preço'].sum()
print(f"Valor total da loja: R$ {total_loja3:,.2f}")

total_loja4 = loja4['Preço'].sum()
print(f"Valor total da loja: R$ {total_loja4:,.2f}")

## Faturamento de cada produto por loja

print("\nFaturamento por produtos na Loja 1:")
# Calcular o faturamento total e quantidade por categoria de produto
faturamento_por_categoria = loja1.groupby('Categoria do Produto').agg({
    'Preço': 'sum',
    'Produto': 'count'
}).reset_index()
faturamento_por_categoria.columns = ['Categoria do Produto', 'Valor Total', 'Quantidade']
faturamento_por_categoria['Valor Total'] = faturamento_por_categoria['Valor Total'].apply(lambda x: f"R$ {x:,.2f}")
print(faturamento_por_categoria)

print("\nFaturamento por produtos na Loja 2:")
faturamento_por_categoria2 = loja2.groupby('Categoria do Produto').agg({
    'Preço': 'sum',
    'Produto': 'count'
}).reset_index()
faturamento_por_categoria2.columns = ['Categoria do Produto', 'Valor Total', 'Quantidade']
faturamento_por_categoria2['Valor Total'] = faturamento_por_categoria2['Valor Total'].apply(lambda x: f"R$ {x:,.2f}")
print(faturamento_por_categoria2)

print("\nFaturamento por produtos na Loja 3:")
faturamento_por_categoria3 = loja3.groupby('Categoria do Produto').agg({
    'Preço': 'sum',
    'Produto': 'count'
}).reset_index()
faturamento_por_categoria3.columns = ['Categoria do Produto', 'Valor Total', 'Quantidade']
faturamento_por_categoria3['Valor Total'] = faturamento_por_categoria3['Valor Total'].apply(lambda x: f"R$ {x:,.2f}")
print(faturamento_por_categoria3)

print("\nFaturamento por produtos na Loja 4:")
faturamento_por_categoria4 = loja4.groupby('Categoria do Produto').agg({
    'Preço': 'sum',
    'Produto': 'count'
}).reset_index()
faturamento_por_categoria4.columns = ['Categoria do Produto', 'Valor Total', 'Quantidade']
faturamento_por_categoria4['Valor Total'] = faturamento_por_categoria4['Valor Total'].apply(lambda x: f"R$ {x:,.2f}")
print(faturamento_por_categoria4)

## Média de avaliação dos produtos por loja
print("\nSatisfação por produtos nas Lojas")

print("\nSatisfação por produtos na Loja 1:")
satisfacao_por_produto1 = loja1.groupby('Categoria do Produto')['Avaliação da compra'].mean().reset_index()
satisfacao_por_produto1.columns = ['Categoria do Produto', 'Média de Avaliação']
satisfacao_por_produto1['Média de Avaliação'] = satisfacao_por_produto1['Média de Avaliação'].round(2)
print(satisfacao_por_produto1)

print("\nSatisfação por produtos na Loja 2:")
satisfacao_por_produto2 = loja2.groupby('Categoria do Produto')['Avaliação da compra'].mean().reset_index()
satisfacao_por_produto2.columns = ['Categoria do Produto', 'Média de Avaliação']
satisfacao_por_produto2['Média de Avaliação'] = satisfacao_por_produto2['Média de Avaliação'].round(2)
print(satisfacao_por_produto2)

print("\nSatisfação por produtos na Loja 3:")
satisfacao_por_produto3 = loja3.groupby('Categoria do Produto')['Avaliação da compra'].mean().reset_index()
satisfacao_por_produto3.columns = ['Categoria do Produto', 'Média de Avaliação']
satisfacao_por_produto3['Média de Avaliação'] = satisfacao_por_produto3['Média de Avaliação'].round(2)
print(satisfacao_por_produto3)

print("\nSatisfação por produtos na Loja 4:")
satisfacao_por_produto4 = loja4.groupby('Categoria do Produto')['Avaliação da compra'].mean().reset_index()
satisfacao_por_produto4.columns = ['Categoria do Produto', 'Média de Avaliação']
satisfacao_por_produto4['Média de Avaliação'] = satisfacao_por_produto4['Média de Avaliação'].round(2)
print(satisfacao_por_produto4)

## Produtos mais e menos vendidos em cada loja
print("\nProdutos mais e menos vendidos em cada loja:")

# Loja 1
print("\nLoja 1:")
produtos_mais_vendidos1 = loja1['Produto'].value_counts().head(5).reset_index()
produtos_mais_vendidos1.columns = ['Produto', 'Quantidade']
print("Top 5 produtos mais vendidos:")
print(produtos_mais_vendidos1)

produtos_menos_vendidos1 = loja1['Produto'].value_counts().tail(5).reset_index()
produtos_menos_vendidos1.columns = ['Produto', 'Quantidade']
print("\n5 produtos menos vendidos:")
print(produtos_menos_vendidos1)

# Loja 2
print("\nLoja 2:")
produtos_mais_vendidos2 = loja2['Produto'].value_counts().head(5).reset_index()
produtos_mais_vendidos2.columns = ['Produto', 'Quantidade']
print("Top 5 produtos mais vendidos:")
print(produtos_mais_vendidos2)

produtos_menos_vendidos2 = loja2['Produto'].value_counts().tail(5).reset_index()
produtos_menos_vendidos2.columns = ['Produto', 'Quantidade']
print("\n5 produtos menos vendidos:")
print(produtos_menos_vendidos2)

# Loja 3
print("\nLoja 3:")
produtos_mais_vendidos3 = loja3['Produto'].value_counts().head(5).reset_index()
produtos_mais_vendidos3.columns = ['Produto', 'Quantidade']
print("Top 5 produtos mais vendidos:")
print(produtos_mais_vendidos3)

produtos_menos_vendidos3 = loja3['Produto'].value_counts().tail(5).reset_index()
produtos_menos_vendidos3.columns = ['Produto', 'Quantidade']
print("\n5 produtos menos vendidos:")
print(produtos_menos_vendidos3)

# Loja 4
print("\nLoja 4:")
produtos_mais_vendidos4 = loja4['Produto'].value_counts().head(5).reset_index()
produtos_mais_vendidos4.columns = ['Produto', 'Quantidade']
print("Top 5 produtos mais vendidos:")
print(produtos_mais_vendidos4)

produtos_menos_vendidos4 = loja4['Produto'].value_counts().tail(5).reset_index()
produtos_menos_vendidos4.columns = ['Produto', 'Quantidade']
print("\n5 produtos menos vendidos:")
print(produtos_menos_vendidos4)

## Calculando o frete de cada loja

print("\nFrete que cada loja está cobrando:\n")

frete_medio_loja1 = loja1['Frete'].mean()
print(f"Frete médio da Loja 1: R$ {frete_medio_loja1:.2f}")

print("\nLoja 2:")
frete_medio_loja2 = loja2['Frete'].mean()
print(f"Frete médio da Loja 2: R$ {frete_medio_loja2:.2f}")

print("\nLoja 3:")
frete_medio_loja3 = loja3['Frete'].mean()
print(f"Frete médio da Loja 3: R$ {frete_medio_loja3:.2f}")

print("\nLoja 4:")
frete_medio_loja4 = loja4['Frete'].mean()
print(f"Frete médio da Loja 4: R$ {frete_medio_loja4:.2f}")

## Criando gráficos para as lojas

# Criando um gráfico de barras para comparar o faturamento total das lojas
lojas = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']
faturamento_total = [total_loja, total_loja2, total_loja3, total_loja4]

plt.figure(figsize=(10, 6))
plt.bar(lojas, faturamento_total, color=['#3498db', '#2ecc71', '#e74c3c', '#f39c12'])
plt.xlabel('Lojas')
plt.ylabel('Faturamento Total (R$)')
plt.title('Faturamento Total por Loja')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Formatar os valores no eixo y para exibir em milhões de reais
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000000:.1f}M'))

# Adicionar os valores acima das barras
for i, v in enumerate(faturamento_total):
    plt.text(i, v + 50000, f'R$ {v/1000000:.1f}M', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Criando um gráfico de barras para comparar o frete médio das lojas
fretes_medios = [frete_medio_loja1, frete_medio_loja2, frete_medio_loja3, frete_medio_loja4]

plt.figure(figsize=(10, 6))
plt.bar(lojas, fretes_medios, color=['#3498db', '#2ecc71', '#e74c3c', '#f39c12'])
plt.xlabel('Lojas')
plt.ylabel('Frete Médio (R$)')
plt.title('Frete Médio por Loja')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar os valores acima das barras
for i, v in enumerate(fretes_medios):
    plt.text(i, v + 1, f'R$ {v:.2f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Criando um gráfico de barras para comparar as avaliações
lojas = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']

# Calculando a média geral de satisfação para cada loja
avaliacao_media_loja1 = loja1['Avaliação da compra'].mean()
avaliacao_media_loja2 = loja2['Avaliação da compra'].mean()
avaliacao_media_loja3 = loja3['Avaliação da compra'].mean()
avaliacao_media_loja4 = loja4['Avaliação da compra'].mean()

avaliacoes_medias = [avaliacao_media_loja1, avaliacao_media_loja2, avaliacao_media_loja3, avaliacao_media_loja4]

plt.figure(figsize=(10, 6))
plt.bar(lojas, avaliacoes_medias, color=['#3498db', '#2ecc71', '#e74c3c', '#f39c12'])
plt.xlabel('Lojas')
plt.ylabel('Média de avaliações')
plt.title('Avaliações médias por loja')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar os valores acima das barras
for i, v in enumerate(avaliacoes_medias):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Criando um gráfico de barras para comparar as avaliações por categoria
# Vamos usar a Loja 1
categorias = satisfacao_por_produto1['Categoria do Produto'].tolist()
avaliacoes_categoria = satisfacao_por_produto1['Média de Avaliação'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(categorias, avaliacoes_categoria, color='#3498db')
plt.xlabel('Categorias de Produtos')
plt.ylabel('Média de Avaliação')
plt.title('Avaliações médias por categoria de produto (Loja 1)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(avaliacoes_categoria):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Loja 2
categorias2 = satisfacao_por_produto2['Categoria do Produto'].tolist()
avaliacoes_categoria2 = satisfacao_por_produto2['Média de Avaliação'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(categorias2, avaliacoes_categoria2, color='#2ecc71')
plt.xlabel('Categorias de Produtos')
plt.ylabel('Média de Avaliação')
plt.title('Avaliações médias por categoria de produto (Loja 2)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(avaliacoes_categoria2):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Loja 3
categorias3 = satisfacao_por_produto3['Categoria do Produto'].tolist()
avaliacoes_categoria3 = satisfacao_por_produto3['Média de Avaliação'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(categorias3, avaliacoes_categoria3, color='#e74c3c')
plt.xlabel('Categorias de Produtos')
plt.ylabel('Média de Avaliação')
plt.title('Avaliações médias por categoria de produto (Loja 3)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(avaliacoes_categoria3):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Loja 4
categorias4 = satisfacao_por_produto4['Categoria do Produto'].tolist()
avaliacoes_categoria4 = satisfacao_por_produto4['Média de Avaliação'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(categorias4, avaliacoes_categoria4, color='#f39c12')
plt.xlabel('Categorias de Produtos')
plt.ylabel('Média de Avaliação')
plt.title('Avaliações médias por categoria de produto (Loja 4)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(avaliacoes_categoria4):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

## Criando um gráfico para ver os produtos mais vendidos em cada loja
# Loja 1
produtos = produtos_mais_vendidos1['Produto'].tolist()
quantidades = produtos_mais_vendidos1['Quantidade'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(produtos, quantidades, color='#3498db')
plt.xlabel('Produtos')
plt.ylabel('Quantidade Vendida')
plt.title('Top 5 Produtos Mais Vendidos (Loja 1)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(quantidades):
    plt.text(i, v + 0.5, f'{v}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Loja 2
produtos2 = produtos_mais_vendidos2['Produto'].tolist()
quantidades2 = produtos_mais_vendidos2['Quantidade'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(produtos2, quantidades2, color='#2ecc71')
plt.xlabel('Produtos')
plt.ylabel('Quantidade Vendida')
plt.title('Top 5 Produtos Mais Vendidos (Loja 2)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(quantidades2):
    plt.text(i, v + 0.5, f'{v}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Loja 3
produtos3 = produtos_mais_vendidos3['Produto'].tolist()
quantidades3 = produtos_mais_vendidos3['Quantidade'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(produtos3, quantidades3, color='#e74c3c')
plt.xlabel('Produtos')
plt.ylabel('Quantidade Vendida')
plt.title('Top 5 Produtos Mais Vendidos (Loja 3)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(quantidades3):
    plt.text(i, v + 0.5, f'{v}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Loja 4
produtos4 = produtos_mais_vendidos4['Produto'].tolist()
quantidades4 = produtos_mais_vendidos4['Quantidade'].tolist()

plt.figure(figsize=(12, 6))
plt.bar(produtos4, quantidades4, color='#f39c12')
plt.xlabel('Produtos')
plt.ylabel('Quantidade Vendida')
plt.title('Top 5 Produtos Mais Vendidos (Loja 4)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Adicionar os valores acima das barras
for i, v in enumerate(quantidades4):
    plt.text(i, v + 0.5, f'{v}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Criando um gráfico para comparar o faturamento por categoria em todas as lojas
categorias = faturamento_por_categoria['Categoria do Produto'].tolist()
faturamento_loja1 = faturamento_por_categoria['Valor Total'].str.replace('R$ ', '').str.replace(',', '').astype(float).tolist()
faturamento_loja2 = faturamento_por_categoria2['Valor Total'].str.replace('R$ ', '').str.replace(',', '').astype(float).tolist()
faturamento_loja3 = faturamento_por_categoria3['Valor Total'].str.replace('R$ ', '').str.replace(',', '').astype(float).tolist()
faturamento_loja4 = faturamento_por_categoria4['Valor Total'].str.replace('R$ ', '').str.replace(',', '').astype(float).tolist()

# Configurando a largura das barras e posições
largura = 0.2
pos1 = range(len(categorias))
pos2 = [x + largura for x in pos1]
pos3 = [x + largura for x in pos2]
pos4 = [x + largura for x in pos3]

plt.figure(figsize=(14, 8))
plt.bar(pos1, faturamento_loja1, largura, label='Loja 1', color='#3498db')
plt.bar(pos2, faturamento_loja2, largura, label='Loja 2', color='#2ecc71')
plt.bar(pos3, faturamento_loja3, largura, label='Loja 3', color='#e74c3c')
plt.bar(pos4, faturamento_loja4, largura, label='Loja 4', color='#f39c12')

plt.xlabel('Categorias de Produtos')
plt.ylabel('Faturamento (R$)')
plt.title('Comparação de Faturamento por Categoria em Todas as Lojas')
plt.xticks([p + largura * 1.5 for p in pos1], categorias, rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Formatar o eixo y para exibir em milhares de reais
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}K'))

plt.tight_layout()
plt.show()

## Análise geográfica das vendas

# Verificar se as colunas de latitude e longitude existem
print("\nVerificando colunas disponíveis:")
print("Loja 1:", loja1.columns.tolist())
print("Loja 2:", loja2.columns.tolist())
print("Loja 3:", loja3.columns.tolist())
print("Loja 4:", loja4.columns.tolist())

# Função para criar um mapa de calor com os dados de vendas
def criar_mapa_calor(df, titulo, arquivo_saida):
    # Verificar se as colunas de latitude e longitude existem
    if 'lat' in df.columns and 'lon' in df.columns:
        # Criar um mapa centralizado na média das coordenadas
        mapa = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], 
                         zoom_start=10)
        
        # Criar dados para o mapa de calor
        dados_calor = []
        for idx, row in df.iterrows():
            dados_calor.append([row['lat'], row['lon'], row['Preço']])
        
        # Adicionar o mapa de calor
        HeatMap(dados_calor).add_to(mapa)
        
        # Adicionar um título ao mapa
        folium.TileLayer('OpenStreetMap').add_to(mapa)
        folium.LayerControl().add_to(mapa)
        
        # Salvar o mapa
        mapa.save(arquivo_saida)
        print(f"Mapa de calor criado e salvo como {arquivo_saida}")
    else:
        print(f"As colunas 'Lat' e 'Lon' não foram encontradas no DataFrame. Colunas disponíveis: {df.columns.tolist()}")

# Criar mapas de calor para cada loja
criar_mapa_calor(loja1, "Vendas da Loja 1", "mapa_vendas_loja1.html")
criar_mapa_calor(loja2, "Vendas da Loja 2", "mapa_vendas_loja2.html")
criar_mapa_calor(loja3, "Vendas da Loja 3", "mapa_vendas_loja3.html")
criar_mapa_calor(loja4, "Vendas da Loja 4", "mapa_vendas_loja4.html")

# Criar um mapa combinado com todas as lojas
def criar_mapa_combinado():
    # Combinar todos os DataFrames
    todas_lojas = pd.concat([loja1, loja2, loja3, loja4])
    
    # Verificar se as colunas de latitude e longitude existem
    if 'lat' in todas_lojas.columns and 'lon' in todas_lojas.columns:
        # Criar um mapa centralizado na média das coordenadas
        mapa = folium.Map(location=[todas_lojas['lat'].mean(), todas_lojas['lon'].mean()], 
                         zoom_start=10)
        
        # Criar dados para o mapa de calor
        dados_calor = []
        for idx, row in todas_lojas.iterrows():
            dados_calor.append([row['lat'], row['lon'], row['Preço']])
        
        # Adicionar o mapa de calor
        HeatMap(dados_calor).add_to(mapa)
        
        # Adicionar um título ao mapa
        folium.TileLayer('OpenStreetMap').add_to(mapa)
        folium.LayerControl().add_to(mapa)
        
        # Salvar o mapa
        mapa.save("mapa_vendas_todas_lojas.html")
        print("Mapa de calor combinado criado e salvo como mapa_vendas_todas_lojas.html")
    else:
        print(f"As colunas 'Lat' e 'Lon' não foram encontradas no DataFrame combinado. Colunas disponíveis: {todas_lojas.columns.tolist()}")

criar_mapa_combinado()

# Análise de vendas por região (se possível)
def analisar_vendas_por_regiao(df):
    if 'lat' in df.columns and 'lon' in df.columns:
        # Criar uma coluna de região baseada em faixas de latitude/longitude
        # Esta é uma simplificação - em um caso real, você usaria dados geográficos mais precisos
        df['Regiao'] = 'Desconhecida'
        
        # Exemplo de divisão por regiões (ajuste conforme necessário)
        df.loc[df['lat'] > df['lat'].mean(), 'Regiao'] = 'Norte'
        df.loc[df['lat'] <= df['lat'].mean(), 'Regiao'] = 'Sul'
        
        # Calcular faturamento por região
        faturamento_por_regiao = df.groupby('Regiao')['Preço'].sum().reset_index()
        faturamento_por_regiao.columns = ['Região', 'Faturamento Total']
        faturamento_por_regiao['Faturamento Total'] = faturamento_por_regiao['Faturamento Total'].apply(lambda x: f"R$ {x:,.2f}")
        
        return faturamento_por_regiao
    else:
        return "Não foi possível analisar vendas por região: colunas de latitude/longitude não encontradas"

# Analisar vendas por região para cada loja
print("\nAnálise de vendas por região:")
print("\nLoja 1:")
print(analisar_vendas_por_regiao(loja1))

print("\nLoja 2:")
print(analisar_vendas_por_regiao(loja2))

print("\nLoja 3:")
print(analisar_vendas_por_regiao(loja3))

print("\nLoja 4:")
print(analisar_vendas_por_regiao(loja4))

