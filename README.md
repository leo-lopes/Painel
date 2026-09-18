# Painel Interativo η × λ — Simulações de Matéria Ativa

Painel visual que organiza simulações de um modelo de matéria ativa em rede bidimensional numa grade de dois parâmetros. Cada célula mostra um frame representativo da simulação e leva ao vídeo completo da dinâmica.

O objetivo é permitir a leitura visual do espaço de parâmetros: percorrendo a grade na horizontal ou na vertical, dá para ver onde o comportamento coletivo do sistema muda de regime.

> **A preencher:** descreva em uma linha o que cada parâmetro representa no seu modelo — por exemplo, η como intensidade de ruído e λ como força de acoplamento entre partículas. É a informação que falta para alguém de fora entender a grade.

---

## Como ler o painel

| Eixo | Parâmetro | Valores |
|---|---|---|
| Colunas | λ | 0.50, 1.00, 2.00, 5.00 |
| Linhas | η | 0.52, 0.50, 0.40, 0.30, 0.20, 0.10 |

As linhas estão em ordem decrescente de η, de modo que o topo da grade concentra os valores mais altos. A linha η = 0.52 aparece separada de η = 0.50 por ser um ponto de interesse específico próximo à transição.

Clicar em qualquer frame abre o vídeo correspondente no YouTube.

---

## Grade de simulações

| η \ λ | 0.50 | 1.00 | 2.00 | 5.00 |
|---|---|---|---|---|
| **0.52** | [vídeo](https://youtu.be/dQFMFvrg5d0) | [vídeo](https://youtu.be/vOq9_djKiXw) | [vídeo](https://youtu.be/gdi4KxzrFeE) | [vídeo](https://youtu.be/as0LwzBHwyg) |
| **0.50** | [vídeo](https://youtu.be/u_axhnLcGAY) | [vídeo](https://youtu.be/iTcEWhDBy_Y) | [vídeo](https://youtu.be/8EIztlXSEUM) | [vídeo](https://youtu.be/XmzrQvEPlwQ) |
| **0.40** | [vídeo](https://youtu.be/1vD99k046-M) | [vídeo](https://youtu.be/FSnIO3cOoyA) | [vídeo](https://youtu.be/GdWauwtRM7g) | [vídeo](https://youtu.be/UTvzkY4Hiew) |
| **0.30** | [vídeo](https://youtu.be/PQsuwmdQ--A) | [vídeo](https://youtu.be/hSLFSRUlHFw) | [vídeo](https://youtu.be/isfI_HhJ8bM) | [vídeo](https://youtu.be/6Ty7HbsI07A) |
| **0.20** | [vídeo](https://youtu.be/Lvt9Csuu8yE) | [vídeo](https://youtu.be/1jjtRTUTu6U) | [vídeo](https://youtu.be/eAkX7CvFA_4) | [vídeo](https://youtu.be/pECOwlCqyNY) |
| **0.10** | [vídeo](https://youtu.be/IdaV5c3qvfg) | [vídeo](https://youtu.be/5o8qzUB385c) | [vídeo](https://youtu.be/DhA9_h4SmtU) | [vídeo](https://youtu.be/wEC0ftgW47U) |

24 simulações no total.

---

## Estrutura do repositório

```
.
├── index.html          # painel — abrir no navegador
├── frames/             # frame representativo de cada simulação
│   ├── frame_ETA_0.52_LAMBDA_0.5.png
│   ├── frame_ETA_0.52_LAMBDA_1.0.png
│   └── ...
└── README.md
```

O nome de cada frame segue o padrão `frame_ETA_<η>_LAMBDA_<λ>.png`, o que permite localizar qualquer simulação da grade diretamente pelo arquivo.

---

## Como usar

Clone o repositório e abra `index.html` no navegador. Não há dependências nem build — é HTML e CSS puros, e os vídeos são servidos pelo YouTube.

```bash
git clone <url-do-repositorio>
cd <pasta>
open index.html        # macOS
xdg-open index.html    # Linux
```

---

## Como o painel foi gerado

> **A preencher:** se a grade foi montada por script (o que o padrão de nomes sugere), vale incluir aqui o comando que regenera o `index.html` a partir da pasta `frames/` e da lista de links. Quem chega ao repositório costuma querer saber se a grade é escrita à mão ou automatizada — e automatizada pesa mais.

```bash
# exemplo
python gerar_painel.py --frames frames/ --links links.csv --out index.html
```

---

## Contexto

Este painel faz parte da pesquisa em sistemas complexos desenvolvida no doutorado em física computacional na UFMG, sobre modelos de matéria ativa em rede bidimensional.

Projeto relacionado: **[Active Ants](https://activeants.streamlit.app)** — aplicação de ponta a ponta com pipeline de dados em nuvem (ETL → PostgreSQL na AWS RDS → dashboard em Streamlit) e modelos de machine learning treinados sobre os dados de simulação.

---

**Leonardo Lopes** · [GitHub](https://github.com/leonardoslopes) · [LinkedIn](https://linkedin.com/in/leo-slopes)
