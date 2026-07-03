import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import Button, Output, VBox, HBox, HTML
from IPython.display import display, FileLink
import copy


DESCRICOES = {
    # Planilha 1: Fenóis
    "Trat_Meses": "Tempo de tratamento/armazenamento da erva-mate",
    "Average_caffeine": "Teor medio de cafeina",
    "Average_theobromine": "Teor medio de teobromina",
    "Average_catechin": "Teor medio de catequina",
    "Average_chlorogenic_acid": "Teor medio de acido clorogenico",
    "Average_caffeic_acid": "Teor medio de acido cafeico",

    # Planilha 2: Analise Sensorial
    "Green_color": "Categoria visual de coloracao esverdeada.",
    "Gold_color": "Categoria visual de coloracao dourada/amarelada.",
    "Fresh_green_odor": "Odor de folha fresca/recem-colhida",
    "Green_aroma": "Aroma vegetal, de folha crua, semelhante ao cheiro de mato",
    "Sweet_aroma": "Nota aromatica adocicada, associada a substancias doces",
    "Bitter_aroma": "Percepcao associada ao amargor",
    "Straw_odor": "Cheiro de palha, aromatico seco e ligeiramente empoeirado",
    "Straw_aroma": "Sabor de palha percebido em boca/retro-olfacao",
    "Astringency": "Sensacao de ressecamento e enrugamento na lingua",

    # Planilha 3: Umidade e Atividade de Agua
    "Moisture_content": "Teor de umidade da erva-mate",
    "Aw": "Atividade de agua, mede a agua disponivel para reacoes quimicas",

    # Planilha 4: Cor
    "L": "Luminosidade (L*), indica a claridade ou escuridao da bebida",
    "a": "Coordenada a*, vermelho vs. verde.",
    "b": "Coordenada b*, amarelo vs. azul.",
    "C": "Chroma (C*), saturacao da cor. Quanto maior, mais viva e intensa a coloracao",
    "D": "De-greening (D*), perda de coloracao verde",
    "YI": "Yellowing Index, indice de amarelamento",
    "DeltaE": "Delta E, diferenca total de cor em relacao a uma referencia"
}



def interpretar_correlacao(r: float) -> str:
    if r == 1:
        return "mesma variavel"

    r_abs = abs(r)
    if r_abs < 0.3:
        forca = "fraca"
    elif r_abs < 0.7:
        forca = "moderada"
    else:
        forca = "forte"

    direcao = "positiva" if r > 0 else "negativa"
    return f"correlacao {forca} e {direcao}"



def plot_correlation_heatmap(df, colunas=None, titulo="Matriz de Correlacao de Pearson",
                               largura=600, altura=600, color_continuous_scale="RdBu_r"):

    if colunas is None:
        colunas = [c for c in df.columns if c in DESCRICOES]

    corr = df[colunas].corr(method="pearson")

    n = len(corr.columns)

    # Monta uma matriz 3D (linha, coluna, [desc_x, desc_y, interpretacao])
    # para usar como customdata no hovertemplate
    customdata = np.empty((n, n, 3), dtype=object)
    for i, y_var in enumerate(corr.index):
        for j, x_var in enumerate(corr.columns):
            r = corr.iloc[i, j]
            customdata[i, j, 0] = DESCRICOES.get(x_var, "Descricao nao encontrada")
            customdata[i, j, 1] = DESCRICOES.get(y_var, "Descricao nao encontrada")
            customdata[i, j, 2] = interpretar_correlacao(r)

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale=color_continuous_scale,
        zmin=-1, zmax=1,
        title=titulo,
    )

    fig.update_traces(
        customdata=customdata,
        hovertemplate=(
            "<b>%{x}</b> × <b>%{y}</b><br>"
            "<span style='font-size:11px'>%{customdata[0]}</span><br>"
            "<span style='font-size:11px'>%{customdata[1]}</span><br><br>"
            "r = %{z:.2f} — %{customdata[2]}"
            "<extra></extra>"
        ),
    )

    fig.update_layout(
        width=largura,
        height=altura,
    )

    return fig


def plot_regressao(df, x, y, titulo=None, cor_pontos="#1f77b4"):
    if titulo is None:
        titulo = f"Regressao Linear: {y} vs. {x}"

    desc_x = DESCRICOES.get(x, "Descricao nao encontrada")
    desc_y = DESCRICOES.get(y, "Descricao nao encontrada")

    fig = px.scatter(
        df, x=x, y=y,
        trendline="ols",
        title=titulo,
        color_discrete_sequence=[cor_pontos],
    )

    # trace 0 = pontos, trace 1 = linha de tendencia
    fig.data[0].update(
        hovertemplate=(
            f"<b>{x}</b>: %{{x}}<br>"
            f"<span style='font-size:11px'>{desc_x}</span><br><br>"
            f"<b>{y}</b>: %{{y}}<br>"
            f"<span style='font-size:11px'>{desc_y}</span>"
            "<extra></extra>"
        )
    )

    if len(fig.data) > 1:
        fig.data[1].update(hovertemplate="Linha de tendencia (OLS)<extra></extra>")

    fig.update_layout(width=650, height=550)

    return fig


def aplicar_estilo_sobrio(fig):
    fig_sobria = copy.deepcopy(fig)

    fig_sobria.update_layout(
        font=dict(family="Times New Roman, Times, serif", size=14, color="black"),
        title_font=dict(family="Times New Roman, Times, serif", size=16, color="black"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        coloraxis_colorbar=dict(
            title_font=dict(family="Times New Roman, Times, serif", size=13),
            tickfont=dict(family="Times New Roman, Times, serif", size=12),
            outlinewidth=1,
            outlinecolor="black",
        ),
        margin=dict(l=80, r=40, t=60, b=80),
    )

    fig_sobria.update_coloraxes(colorscale="RdBu_r")

    fig_sobria.update_xaxes(
        showline=True, linewidth=1, linecolor="black", mirror=True,
        tickfont=dict(family="Times New Roman, Times, serif", size=12),
    )
    fig_sobria.update_yaxes(
        showline=True, linewidth=1, linecolor="black", mirror=True,
        tickfont=dict(family="Times New Roman, Times, serif", size=12),
    )

    return fig_sobria


def exportar_para_artigo(fig, nome_arquivo="heatmap_artigo.png", escala=3):
    pergunta = HTML(
        "<b>Deseja salvar a versao estatica desta figura para o artigo?</b>"
    )
    botao_sim = Button(description="Sim, salvar", button_style="success")
    botao_nao = Button(description="Nao", button_style="danger")
    saida = Output()

    def ao_clicar_sim(b):
        with saida:
            saida.clear_output()
            fig_sobria = aplicar_estilo_sobrio(fig)
            caminho = f"/content/drive/MyDrive/dados-erva-mate/outputs/{nome_arquivo}"
            fig_sobria.write_image(caminho, scale=escala)
            print(f"Figura salva em: {caminho}")

    def ao_clicar_nao(b):
        with saida:
            saida.clear_output()
            print("Exportacao cancelada.")

    botao_sim.on_click(ao_clicar_sim)
    botao_nao.on_click(ao_clicar_nao)

    display(VBox([pergunta, HBox([botao_sim, botao_nao]), saida]))
