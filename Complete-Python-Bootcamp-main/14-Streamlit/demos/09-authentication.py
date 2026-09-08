"""Safe authentication lesson with a local pretend login and OIDC guidance."""  # This announces that the login is educational, not production security.

import streamlit as st  # Streamlit gives us forms, passwords, state, and messages.

st.set_page_config(page_title="Authentication Demo", page_icon="🔐")  # This configures the browser-tab title and icon.
st.title("🔐 Authentication")  # This is the main page heading.
st.warning("Learning demo only: this pretend login must not protect real data.")  # This prevents learners from mistaking the example for secure authentication.

if "demo_user" not in st.session_state:  # Session state is a small memory box that survives Streamlit reruns.
    st.session_state.demo_user = ""  # An empty name means nobody is pretending to be logged in yet.

if not st.session_state.demo_user:  # This branch shows the login form when no name is stored.
    with st.form("login_form"):  # A form waits and sends all its widget values together.
        username = st.text_input("Username", placeholder="little-coder", help="A real app gets identity from a trusted provider.")  # This collects a demonstration username.
        password = st.text_input("Password", type="password", help="type='password' hides the characters on screen.")  # This masks, but does not securely verify, the sample password.
        submitted = st.form_submit_button("Pretend to log in", type="primary")  # This button submits the whole form at once.
    if submitted and username.strip() and password:  # This accepts any non-empty values because it is only a UI lesson.
        st.session_state.demo_user = username.strip()  # The cleaned name is saved in the session memory box.
        st.rerun()  # Rerun redraws the page so the logged-in branch appears immediately.
    elif submitted:  # This branch runs when the button was pressed with missing information.
        st.error("Please fill in both boxes.")  # An error box clearly explains what must be fixed.
else:  # This branch appears after the pretend login stores a name.
    st.success(f"Hello, {st.session_state.demo_user}!")  # This personalized message proves that session state remembered the name.
    st.metric("Demo status", "Signed in")  # A metric card displays the current pretend state.
    if st.button("Log out"):  # This button lets the visitor remove the pretend identity.
        st.session_state.demo_user = ""  # Clearing the name returns the demo to logged-out state.
        st.rerun()  # Rerunning shows the login form again.

with st.expander("How real Streamlit login works"):  # This disclosure keeps advanced OIDC information optional.
    st.write("Real apps use `st.login()`, `st.user`, and `st.logout()` with an OpenID Connect provider.")  # This names Streamlit's production authentication tools.
    st.code("if not st.user.is_logged_in:\n    st.button('Log in', on_click=st.login)\n    st.stop()", language="python")  # This displays a short real-login pattern without executing unconfigured login.
    st.info("Client secrets belong in `.streamlit/secrets.toml`; never commit that real file.")  # This teaches the most important secret-handling rule.
