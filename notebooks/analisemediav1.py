import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

# ==============================
# 📂 CARREGAMENTO DOS DADOS
# ==============================

AnaliseSensorialM = pd.read_csv(
    r"C:\Users\Alexi\Downloads\faculdade\IC-ENG ALIMENTOS\Dados\CSV data\Análise sensorial.csv",
    sep=',',
    decimal='.',
    encoding='utf-8'
)

CorM = pd.read_csv(
    r"C:\Users\Alexi\Downloads\faculdade\IC-ENG ALIMENTOS\Dados\CSV data\Cor.csv",
    sep=',',
    decimal='.',
    encoding='utf-8'
)

EstatUmidM = pd.read_csv(
    r"C:\Users\Alexi\Downloads\faculdade\IC-ENG ALIMENTOS\Dados\CSV data\Estat. Umid e AW.csv",
    sep=',',
    decimal='.',
    encoding='utf-8'
)

FenoisIndividuaisM = pd.read_csv(
    r"C:\Users\Alexi\Downloads\faculdade\IC-ENG ALIMENTOS\Dados\CSV data\Fenóis individuais.csv",
    sep=';',
    decimal='.',
    encoding='utf-8'
)

# ==============================
# ⚙ CONFIGURAÇÃO
# ==============================

pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.5f}'.format

# ==============================
# 📊 FUNÇÃO DE PREDIÇÃO (CORRIGIDA)
# ==============================

def criar_predicao(df, coluna_y):
    modelo = LinearRegression()

    x = df[['Trat_Meses']]
    y = df[coluna_y]

    modelo.fit(x, y)

    # 🔥 intervalo real
    meses_min = df['Trat_Meses'].min()
    meses_max = df['Trat_Meses'].max()

    # 🔵 linha do modelo (mesmo intervalo do histórico)
    meses_linha = pd.DataFrame({
        "Trat_Meses": np.linspace(meses_min, meses_max, 50)
    })

    linha_modelo = modelo.predict(meses_linha)

    df_linha_hist = pd.DataFrame({
        "Trat_Meses": meses_linha["Trat_Meses"],
        coluna_y: linha_modelo,
        "Tipo": "Histórico"
    })

    # 🔴 previsão futura (APÓS o último ponto)
    meses_futuro = pd.DataFrame({
        "Trat_Meses": np.linspace(meses_max, meses_max + 10, 50)
    })

    previsoes = modelo.predict(meses_futuro)

    df_previsao = pd.DataFrame({
        "Trat_Meses": meses_futuro["Trat_Meses"],
        coluna_y: previsoes,
        "Tipo": "Previsão"
    })

    # 🔵 dados reais
    df_real = df.copy()
    df_real["Tipo"] = "Dados Reais"

    return df_real, df_linha_hist, df_previsao

# ==============================
# 📈 FUNÇÃO DE GRÁFICO (CORRIGIDA)
# ==============================

def gerar_grafico(df_real, df_linha_hist, df_previsao, coluna_y, titulo):

    fig = go.Figure()

    # 🔵 pontos reais
    fig.add_trace(go.Scatter(
        x=df_real["Trat_Meses"],
        y=df_real[coluna_y],
        mode='markers',
        name='Dados Reais'
    ))

    # 🔵 linha do histórico (modelo ajustado)
    fig.add_trace(go.Scatter(
        x=df_linha_hist["Trat_Meses"],
        y=df_linha_hist[coluna_y],
        mode='lines',
        name='Histórico'
    ))

    # 🔴 linha de previsão
    fig.add_trace(go.Scatter(
        x=df_previsao["Trat_Meses"],
        y=df_previsao[coluna_y],
        mode='lines',
        name='Previsão'
    ))

    # 🔥 layout
    fig.update_layout(
        title=titulo,
        xaxis=dict(
            title="Meses",
            tickmode='linear',
            dtick=1
        ),
        yaxis=dict(
            title=coluna_y
        )
    )

    fig.write_html("grafico.html", auto_open=True)

# ==============================
# 🎯 MENU PRINCIPAL
# ==============================

print("Escolha o tipo de análise:")
print("1 - Análise Sensorial")
print("2 - Cor")
print("3 - Fenóis")
print("4 - Estatística de Umidade")

opcao = input("Digite o número: ")

if opcao == "1":
    df = AnaliseSensorialM
    titulo = "Análise Sensorial"

elif opcao == "2":
    df = CorM
    titulo = "Cor"

elif opcao == "3":
    df = FenoisIndividuaisM
    titulo = "Fenóis"

elif opcao == "4":
    df = EstatUmidM
    titulo = "Umidade"

else:
    print("Opção inválida!")
    exit()

# ==============================
# 🔢 ESCOLHA DA COLUNA
# ==============================

colunas_validas = [col for col in df.columns if col != "Trat_Meses"]

print("\nEscolha o atributo para análise:")

for i, col in enumerate(colunas_validas):
    print(f"{i} - {col}")

indice = int(input("Digite o número da coluna: "))

if indice < 0 or indice >= len(colunas_validas):
    print("Índice inválido!")
    exit()

coluna_escolhida = colunas_validas[indice]

# ==============================
# 🚀 EXECUÇÃO
# ==============================

df_real, df_linha_hist, df_previsao = criar_predicao(df, coluna_escolhida)

print("\n📊 DADOS REAIS:")
print(df_real)

print("\n📊 PREVISÃO:")
print(df_previsao)

gerar_grafico(
    df_real,
    df_linha_hist,
    df_previsao,
    coluna_escolhida,
    f"{coluna_escolhida} ao longo dos meses"
)