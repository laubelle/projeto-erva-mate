# Dicionário de Dados

Este documento reúne a definição de todas as variáveis utilizadas nas planilhas de dados desta pesquisa, organizadas por tema/planilha de origem. Cada tabela inclui a referência bibliográfica que fundamenta a definição e/ou o método de obtenção da variável.

obs: Verificar presença dos termos exatos nos artigos.

---

## 1. Planilha de Compostos Bioativos

| Variável | Descrição | Ref. |
|---|---|---|
| `Trat_Meses` | Tempo de tratamento/armazenamento da erva-mate | — |
| `Average_caffeine` | Teor médio de cafeína, principal metilxantina estimulante da erva-mate | [1,2] |
| `Average_theobromine` | Teor médio de teobromina, metilxantina que contribui para o amargor | [1] |
| `Average_catechin` | Teor médio de catequina, flavonoide com atividade antioxidante | [3] |
| `Average_chlorogenic_acid` | Teor médio de ácido clorogênico, principal ácido fenólico da erva-mate | [4] |
| `Average_caffeic_acid` | Teor médio de ácido cafeico, derivado da degradação do ácido clorogênico | [5] |

---

## 2. Planilha de Análise Sensorial

| Variável | Descrição | Ref. |
|---|---|---|
| `Trat_Meses` | Tempo de tratamento/armazenamento da erva-mate | — |
| `Green_color` | Intensidade da cor verde, associada à clorofila presente | [6] |
| `Fresh_green_odor` | Odor de folha fresca/recém-colhida | [6] |
| `Sweet_aroma` | Nota aromática adocicada, típica de erva mais envelhecida | [6] |
| `Green_aroma` | Aroma vegetal, de folha crua | [6] |
| `Bitter_aroma` | Percepção aromática associada ao amargor | [6] |
| `Gold_color` | Tonalidade amarelo-dourada, ligada à degradação da clorofila | [6] |
| `Straw_odor` | Cheiro de palha/feno seco, característico de erva envelhecida | [6] |
| `Straw_aroma` | Aroma de palha percebido em boca/retro-olfação | [6] |
| `Astringency` | Sensação de boca seca/travo, ligada a taninos e compostos fenólicos | [6,9] |

> Os termos específicos acima (exceto `Astringency`, confirmado no Documento [9]) são atribuídos ao léxico sensorial geral de Godoy et al. (2020), que descreve cor, aroma e sabor do chá-mate com 39 atributos. 
---

## 3. Planilha Físico-Química (Umidade e Atividade de Água)

| Variável | Descrição | Ref. |
|---|---|---|
| `Trat_Meses` | Tempo de tratamento/armazenamento da erva-mate | — |
| `Moisture_content` | Teor de umidade da erva-mate | [7] |
| `Aw` | Atividade de água; mede a água disponível para reações químicas e crescimento microbiano | [8] |

---

## 4. Planilha de Cor (Colorimetria)

| Variável | Descrição | Ref. |
|---|---|---|
| `Trat_Meses` | Tempo de armazenamento, eixo temporal da análise | — |
| `L` | Luminosidade (L*): claridade da bebida | [8] |
| `a` | Coordenada a*: vermelho vs. verde. Positivo = mais vermelho; negativo = mais verde | [8] |
| `b` | Coordenada b*: amarelo vs. azul. Positivo = mais amarelo; negativo = mais azul | [8] |
| `C` | Chroma (C*): saturação/intensidade da cor. Quanto maior, mais viva a coloração | [8] |
| `D` | De-greening (D*): perda de coloração verde, associada à degradação da clorofila | [8] |
| `YI` | Yellowing Index: índice de amarelamento, tende a aumentar com o envelhecimento | [8] |
| `DeltaE` | ΔE: diferença total de cor em relação a uma referência. Quanto maior, mais a cor se afastou do estado original | [8] |

> A fórmula de ΔE aparece no artigo [8], mas não é reportada nos resultados/tabelas. Analisar melhor.

---

## Referências

[1] Bojić M, Simon Haas V, Šarić D, Maleš Ž. Determination of Flavonoids, Phenolic Acids, and Xanthines in Mate Tea. *J Anal Methods Chem*. 2013.

[2] Heck CI, De Mejia EG. Yerba Mate Tea (Ilex paraguariensis): A Comprehensive Review on Chemistry, Health Implications, and Technological Considerations. *J Food Sci*. 2007;72(9).

[3] Bravo L, Goya L, Lecumberri E. LC/MS characterization of phenolic constituents of mate (Ilex paraguariensis, St. Hil.) and its antioxidant activity compared to commonly consumed beverages. *Food Research International*. 2007;40(3):393–405.

[4] Rząsa-Duran E, Kryczyk-Poprawa A, Drabicki D, Podkowa A, Sułkowska-Ziaja K, Szewczyk A, et al. Yerba Mate as a Source of Elements and Bioactive Compounds with Antioxidant Activity. *Antioxidants*. 2022;11(2):371.

[5] de Vasconcellos AC, Frazzon J, Zapata Noreña CP. Phenolic Compounds Present in Yerba Mate Potentially Increase Human Health: A Critical Review. *Plant Foods for Human Nutrition*. 2022;77(4):495–503.

[6] Godoy RCB, Chambers E, Yang G. Development of a preliminary sensory lexicon for mate tea. *J Sens Stud*. 2020;35(3):e12570.

[7] Frizon CNT, Nisgoski S. Color parameters to predict moisture and tannin content in yerba mate process. *Floresta e Ambiente*. 2020;27(2):e20180098.

[8] Câmara OP, Costa E, Prado NV do, Lucchetta L, Moresco KS, Burgardt VCF, Machado-Lunkes A. NIX quality control colorimeter can evaluate color of yerba mate. *Food Science and Technology*, Campinas. 2025;45:e00460.

[9] Lucchetta L, Martins R, Oliveira NM de, Gobbi BGV, Câmara OP, Coelho SR, Prado NV do, Wagner Junior A. Beverage of mate tea (Ilex paraguariensis) with pitanga (Eugenia uniflora) for enhanced sensory and nutritional benefits. *Rev Ceres*, Viçosa. 2025;72:e72036.
