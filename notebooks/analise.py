import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np 


# arquivos que vamos usar
AnaliseSensorialM = pd.read_csv(r"C:\Users\Alexi\Downloads\faculdade\IC-ENG ALIMENTOS\Dados\CSV data\Análise sensorial.csv", sep=',', decimal='.', encoding='utf-8')
x=AnaliseSensorialM[['Trat_Meses']]
y=AnaliseSensorialM[['Green_color']]

modelo=LinearRegression()
modelo.fit(x,y)
meses_predicao = pd.DataFrame({"Trat_Meses": [14, 16, 18, 20, 22, 24]})
previsoes=modelo.predict(meses_predicao)

previsoes = modelo.predict(meses_predicao).ravel()

tabela_historico = pd.DataFrame({ "Trat_Meses": AnaliseSensorialM["Trat_Meses"], "Green_color": AnaliseSensorialM["Green_color"]})

tabela_predicao = pd.DataFrame({"Trat_Meses": meses_predicao["Trat_Meses"], "Green_color": previsoes
})

tabela_historico["tipo"] = "Histórico"
tabela_predicao["tipo"] = "Predição"

tabela_completa = pd.concat([tabela_historico, tabela_predicao])

grafico = px.scatter(
    tabela_completa,
    x="Trat_Meses",
    y="Green_color",
    color="tipo",
    title="Análise Sensorial - Green Color"
)

grafico.update_traces(mode='markers+lines') 

print("\n📊 DADOS REAIS:")
print(tabela_historico)

print("\n📊 PREVISÃO:")
print(tabela_predicao)

grafico.show()