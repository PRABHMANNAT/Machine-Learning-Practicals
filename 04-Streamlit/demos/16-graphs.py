"""Network and flow graphs using Graphviz text."""  # This states that the lesson is about relationships, not numeric charts.

import streamlit as st  # Streamlit renders Graphviz, code, controls, and explanations.

st.set_page_config(page_title="Graphs Demo", page_icon="🕸️")  # This configures the browser tab.
st.title("🕸️ Graphs and relationships")  # This shows the page heading.

direction = st.radio("Graph direction", options=["LR", "TB"], horizontal=True, format_func=lambda value: "Left to right" if value == "LR" else "Top to bottom")  # Graphviz reads LR or TB to arrange nodes.
show_cache = st.checkbox("Include the cache step", value=True)  # This widget decides whether one optional node is included.

dot_lines = [  # This list stores Graphviz's small DOT language one line at a time.
    "digraph learning_app {",  # `digraph` starts a graph whose arrows have direction.
    f"rankdir={direction};",  # `rankdir` receives the radio button's direction parameter.
    'User [shape=oval, color="#ff4b4b"];',  # This creates an oval user node with a red outline.
    'Widget [shape=box, color="#4b8bff"];',  # This creates a blue rectangular widget node.
    'Model [shape=box, color="#22a06b"];',  # This creates a green rectangular model node.
    "User -> Widget;",  # This arrow means the user changes the widget.
]  # This closes the starting list.
if show_cache:  # This branch adds a cache node only when the checkbox is ticked.
    dot_lines.extend(['Cache [shape=cylinder];', "Widget -> Cache;", "Cache -> Model;"])  # Extend appends three strings to the existing list.
else:  # This branch is used when the optional cache step is hidden.
    dot_lines.append("Widget -> Model;")  # Append adds the direct widget-to-model arrow.
dot_lines.extend(["Model -> Result;", "}"])  # These lines add the final result arrow and close the graph.
dot_source = "\n".join(dot_lines)  # Joining with newline characters makes valid Graphviz source text.

st.graphviz_chart(dot_source, width="stretch")  # This component turns DOT text into a full-width diagram.
st.code(dot_source, language="dot", line_numbers=True)  # This component lets learners inspect the source that created the picture.
st.info("Nodes are things; arrows are relationships or movement between things.")  # This explains graphs in child-friendly language.
