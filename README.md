# Grafo de ferramentas de IA no Streamlit

Este pacote contém a versão ajustada do grafo e uma aplicação Streamlit pronta
para execução. Mantenha os arquivos `streamlit_app.py` e
`grafo_ferramentas_ia.html` na mesma pasta.

## Executar no computador

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

No macOS ou Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Publicar no Streamlit Community Cloud

1. Coloque toda esta pasta em um repositório do GitHub.
2. Acesse `share.streamlit.io` e escolha **Create app**.
3. Selecione o repositório e informe `streamlit_app.py` como arquivo principal.
4. Clique em **Deploy**.

O `requirements.txt` fixa uma versão do Streamlit compatível com execução de
JavaScript por `st.html`. Os botões internos do grafo continuam exportando PNG
e SVG.
