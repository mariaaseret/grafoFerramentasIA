from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


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

# O grafo depende de JavaScript para desenhar o SVG e controlar pesquisa,
# filtros, zoom, arraste e exportação. O iframe executa o documento completo
# sem que o Streamlit remova ou reorganize seus scripts.
graph_html = GRAPH_FILE.read_text(encoding="utf-8")
components.html(
    graph_html,
    height=1450,
    scrolling=True,
)
