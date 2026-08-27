from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
GRAPH_FILE = APP_DIR / "grafo_ferramentas_ia.html"

st.set_page_config(
    page_title="Grafo de ferramentas de IA",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if not GRAPH_FILE.is_file():
    st.error("O arquivo grafo_ferramentas_ia.html não foi encontrado.")
    st.stop()

# O arquivo é local e controlado pelo projeto. O JavaScript é necessário para
# pesquisa, filtros, zoom, arraste e exportação em PNG/SVG.
st.html(
    GRAPH_FILE,
    width="stretch",
    unsafe_allow_javascript=True,
)
