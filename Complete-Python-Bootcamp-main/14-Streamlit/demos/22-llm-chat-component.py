"""LLM-shaped chat lesson using the optional st-chat-message component."""  # This honestly describes the example as a safe local simulation.

import streamlit as st  # Streamlit supplies state, inputs, controls, and a native fallback chat UI.

try:  # Optional imports need a friendly fallback when a learner has not installed the package yet.
    from st_chat_message import message as component_message  # The package import name uses underscores even though pip uses hyphens.
except ImportError:  # This branch runs only when `pip install st-chat-message` has not been run.
    component_message = None  # None is an easy flag meaning the optional component is unavailable.

st.set_page_config(page_title="LLM Chat Demo", page_icon="🤖")  # This sets the browser-tab details.
st.title("🤖 LLM chat-shaped demo")  # This creates the main page heading.
st.warning("This beginner demo uses local rules, not a real LLM or paid API.")  # This keeps the simulation transparent.
st.code("python -m pip install st-chat-message", language="bash")  # This displays the exact installation command the learner requested.


def make_reply(prompt, temperature, max_words):  # These parameters imitate common LLM controls in a predictable local function.
    cleaned_prompt = prompt.strip()  # Strip removes accidental spaces from both ends.
    if "dinosaur" in cleaned_prompt.lower():  # This tiny rule recognizes one teaching topic.
        answer = "Dinosaurs were a diverse group of reptiles. Try the dinosaur classifier project next!"  # This is the dinosaur-specific local response.
    elif "streamlit" in cleaned_prompt.lower():  # This tiny rule recognizes another teaching topic.
        answer = "Streamlit reruns your Python script when a widget changes, then redraws the page."  # This is the Streamlit-specific local response.
    else:  # This fallback handles every other prompt.
        answer = f"You said: {cleaned_prompt}. A real LLM would generate a learned response here."  # Echoing proves the prompt travelled through the app.
    playful_ending = " 🌈" if temperature > 0.7 else ""  # Higher pretend temperature adds a playful decoration.
    return " ".join(answer.split()[:max_words]) + playful_ending  # Slicing limits the output to the chosen pretend maximum words.


if "chat_history" not in st.session_state:  # Session state keeps prior messages between reruns.
    st.session_state.chat_history = [{"role": "assistant", "text": "Hello! Ask me about Streamlit or dinosaurs."}]  # This starter message makes the empty chat welcoming.

temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.3, step=0.1, help="Real LLMs often use temperature to control randomness; this demo only changes an emoji.")  # This demonstrates a common generation parameter.
max_words = st.slider("Maximum words", min_value=5, max_value=30, value=18, help="This teaching version limits words instead of tokens.")  # This demonstrates output-length control.
use_component = st.checkbox("Render with st-chat-message", value=False, disabled=component_message is None)  # This opt-in safely demonstrates the third-party component when installed.

for index, chat_item in enumerate(st.session_state.chat_history):  # This loop redraws every remembered message after each rerun.
    if use_component and component_message is not None:  # This branch uses the requested package only when available and selected.
        component_message(chat_item["text"], is_user=chat_item["role"] == "user", key=f"component_{index}")  # `is_user` controls side and styling; unique keys separate messages.
    else:  # This branch uses Streamlit's built-in chat component as the dependable default.
        with st.chat_message(chat_item["role"]):  # The role parameter chooses assistant or user styling.
            st.markdown(chat_item["text"])  # Markdown prints the message text inside its chat bubble.

prompt = st.chat_input("Ask a small question")  # Chat input waits at the bottom and returns text after submission.
if prompt:  # This branch runs only after the visitor sends a non-empty prompt.
    st.session_state.chat_history.append({"role": "user", "text": prompt})  # This saves the visitor's message first.
    reply = make_reply(prompt, temperature, max_words)  # This sends the prompt and control parameters to our local response function.
    st.session_state.chat_history.append({"role": "assistant", "text": reply})  # This saves the generated local response.
    st.rerun()  # Rerun redraws the full history including both new messages.

if st.button("Clear chat"):  # This button offers a fresh conversation.
    st.session_state.chat_history = []  # Replacing the list removes all remembered messages.
    st.rerun()  # Rerun immediately redraws the now-empty chat.

if component_message is None:  # This branch helps learners who have not installed the optional dependency.
    st.info("Install `st-chat-message`, restart Streamlit, and this page will enable the component checkbox.")  # This gives a concrete recovery instruction.
