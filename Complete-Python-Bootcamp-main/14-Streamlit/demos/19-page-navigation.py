"""Page-navigation ideas that remain simple in a single teaching file."""  # This explains why the demo imitates pages instead of needing extra files.

import streamlit as st  # Streamlit provides navigation-like controls and URL query parameters.

st.set_page_config(page_title="Navigation Demo", page_icon="🧭")  # This configures the browser tab.
st.title("🧭 Page navigation")  # This displays the lesson title.

page_names = ["Home", "Lessons", "About"]  # This list contains every pretend page name.
requested_page = st.query_params.get("page", "Home")  # Query parameters remember a value in the page's URL.
starting_index = page_names.index(requested_page) if requested_page in page_names else 0  # Unknown URL values safely fall back to Home.
selected_page = st.sidebar.radio("Go to", options=page_names, index=starting_index, help="A sidebar radio makes a small manual navigation menu.")  # This menu chooses one page at a time.
st.query_params["page"] = selected_page  # Writing the choice into the URL makes it bookmarkable.

if selected_page == "Home":  # This branch renders the pretend Home page.
    st.header("Home")  # This heading makes the current page obvious.
    st.write("Welcome! Choose another page from the sidebar.")  # This gives the visitor a next action.
elif selected_page == "Lessons":  # This branch renders the pretend Lessons page.
    st.header("Lessons")  # This heading names the current page.
    first_tab, second_tab = st.tabs(["Widgets", "Charts"])  # Tabs provide smaller navigation inside a page.
    first_tab.write("Widgets collect information from visitors.")  # This text belongs to the Widgets tab.
    second_tab.write("Charts turn rows of numbers into pictures.")  # This text belongs to the Charts tab.
else:  # The only remaining known choice is About.
    st.header("About")  # This heading names the current page.
    st.info("This one-file pattern is for learning; larger apps should use `st.Page` and `st.navigation`.")  # This points learners to Streamlit's scalable navigation tools.

with st.expander("Real multipage pattern"):  # This hides advanced code until the learner wants it.
    st.code("home = st.Page('home.py', title='Home')\nabout = st.Page('about.py', title='About')\nmenu = st.navigation([home, about])\nmenu.run()\nst.page_link('about.py', label='About')", language="python", line_numbers=True)  # This shows Page, navigation, and page-link APIs without executing missing pages.
    st.link_button("Read Streamlit navigation docs", "https://docs.streamlit.io/develop/api-reference/navigation")  # A link button safely navigates to an external learning page.
