"""Focused demo: text elements, code, equations, and a local image."""

from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
st.set_page_config(page_title="Text and media", page_icon="📝")
st.title("Text and Media")
st.header("A clear section")
st.subheader("A smaller section")
st.write("`st.write` understands text, numbers, dictionaries, tables, and more.")
st.markdown("**Markdown** adds structure such as *emphasis* and lists.")
st.caption("Captions are useful for units, sources, and caveats.")
st.code("total = sum([1, 2, 3])", language="python")
st.latex(r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i")
st.image(str(ROOT / "assets" / "streamlit_learning.svg"), caption="A local SVG asset")
st.info("Avoid rendering untrusted raw HTML. Normal Streamlit text is safer.")

