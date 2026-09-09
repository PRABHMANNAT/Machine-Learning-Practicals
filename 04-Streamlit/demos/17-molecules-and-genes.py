"""No-special-package introduction to molecules and gene sequences."""  # This announces a lightweight scientific-data lesson.

from collections import Counter  # Counter quickly counts each DNA letter.

import pandas as pd  # Pandas puts DNA counts into a table.
import streamlit as st  # Streamlit displays molecule graphs, inputs, metrics, and tables.

st.set_page_config(page_title="Molecules and Genes", page_icon="🧬")  # This selects the browser-tab details.
st.title("🧬 Molecules & genes")  # This shows the main lesson heading.

molecule_tab, gene_tab = st.tabs(["Water molecule", "DNA letters"])  # Two tabs separate chemistry from genetics.
with molecule_tab:  # This block draws a simple water molecule.
    st.graphviz_chart('graph water { O [color="red", style="filled"]; H1 [label="H"]; H2 [label="H"]; O -- H1; O -- H2; }', width="stretch")  # An undirected graph shows one oxygen bonded to two hydrogens.
    st.markdown("Water is **H₂O**: two hydrogen atoms joined to one oxygen atom.")  # Markdown makes the formula and explanation readable.
    st.metric("Atoms in one water molecule", 3)  # This card counts two hydrogen atoms plus one oxygen atom.
with gene_tab:  # This block explores a short DNA-like sequence.
    sequence = st.text_input("DNA sequence", value="ACGTACGGA", max_chars=40, help="Use only A, C, G, and T for this beginner demo.").upper()  # Uppercase makes lowercase input easy to validate and count.
    invalid_letters = sorted(set(sequence) - set("ACGT"))  # Set subtraction finds letters that do not belong to our allowed alphabet.
    if invalid_letters:  # This branch runs when unexpected letters were typed.
        st.error(f"Please remove: {', '.join(invalid_letters)}")  # This tells the learner exactly which letters are invalid.
    else:  # This branch runs when every letter is valid.
        counts = Counter(sequence)  # Counter returns how many A, C, G, and T letters exist.
        count_table = pd.DataFrame({"base": list("ACGT"), "count": [counts[base] for base in "ACGT"]}).set_index("base")  # This builds one chart-ready row per DNA base.
        st.bar_chart(count_table)  # The bars make letter frequencies easy to compare.
        st.dataframe(count_table, width="stretch")  # The table shows the exact values behind the bars.
        st.metric("Sequence length", len(sequence))  # Length counts how many DNA letters were entered.

st.caption("Real bioinformatics needs specialist libraries and careful scientific data; this page only teaches UI patterns.")  # This sets the correct scientific expectation.
