"""Small integration patterns: links, embedded HTML, and copyable payloads."""  # This defines integration as connecting the app to another tool or page.

import json  # JSON is a common text format shared between different systems.

import streamlit as st  # Streamlit supplies link and display components.

st.set_page_config(page_title="Integrations Demo", page_icon="🧩")  # This sets the browser-tab details.
st.title("🧩 Integrations")  # This creates the page heading.
st.write("An integration lets this app exchange information or experiences with another tool.")  # This defines the topic in simple language.

service = st.selectbox("Choose a documentation service", options=["Streamlit", "Python", "Pandas"])  # This collects which external site the learner wants.
service_urls = {"Streamlit": "https://docs.streamlit.io", "Python": "https://docs.python.org/3/", "Pandas": "https://pandas.pydata.org/docs/"}  # This dictionary safely maps known labels to known links.
st.link_button(f"Open {service} documentation", service_urls[service], type="primary")  # A link button opens the selected external website.

st.html("<div style='padding:12px;border:2px solid #ff4b4b;border-radius:8px'><strong>Embedded HTML card</strong><p>This tiny card came from HTML.</p></div>")  # HTML renders a styled local card and ignores JavaScript for safety.

payload = {"event": "lesson_completed", "topic": service.lower()}  # A payload is a packet another service could receive.
payload_text = json.dumps(payload, indent=2)  # Dumps turns the Python dictionary into portable JSON text.
st.code(payload_text, language="json")  # This code block makes the outgoing data easy to inspect.
st.download_button("Download example payload", data=payload_text, file_name="integration_payload.json", mime="application/json")  # Download simulates handing the payload to another system.
st.info("Real integrations often need API keys. Keep keys in Streamlit secrets, never directly in Python files.")  # This teaches the key security rule.
