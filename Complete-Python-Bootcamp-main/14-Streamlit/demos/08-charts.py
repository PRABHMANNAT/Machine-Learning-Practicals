"""Beginner demo of three built-in Streamlit chart components."""  # This tells learners the topic before the app starts.

import pandas as pd  # Pandas stores the numbers used by every chart.
import streamlit as st  # Streamlit draws the controls and charts.

st.set_page_config(page_title="Charts Demo", page_icon="📊")  # This sets the browser tab's label and icon.
st.title("📊 Charts: line, bar, and area")  # This displays the page heading.

days = st.slider("How many days?", min_value=3, max_value=10, value=7, help="This parameter controls how many rows the charts receive.")  # This widget chooses the number of visible days.
chart_data = pd.DataFrame(  # This begins a small table with predictable values.
    {  # This dictionary maps column names to their values.
        "day": list(range(1, days + 1)),  # Range creates day numbers from one through the chosen amount.
        "apples": [2 + number * 2 for number in range(days)],  # This list comprehension makes apples rise steadily.
        "oranges": [3 + number for number in range(days)],  # This makes oranges rise more slowly.
    }  # This closes the dictionary.
).set_index("day")  # The day column becomes the horizontal chart axis.

line_tab, bar_tab, area_tab = st.tabs(["Line", "Bar", "Area"])  # Tabs let three examples share one tidy page.
with line_tab:  # Everything indented here appears inside the Line tab.
    st.line_chart(chart_data, height=300, width="stretch")  # A line chart is useful for change over time, and stretch fills the tab.
with bar_tab:  # Everything indented here appears inside the Bar tab.
    st.bar_chart(chart_data, height=300, width="stretch")  # A bar chart makes separate amounts easy to compare.
with area_tab:  # Everything indented here appears inside the Area tab.
    st.area_chart(chart_data, height=300, width="stretch")  # An area chart fills the space under each line.

st.dataframe(chart_data, width="stretch")  # Showing the source table helps learners connect numbers to shapes.
st.caption("Useful parameters: `height` sets pixels and `width='stretch'` fills the available space.")  # This explains the repeated chart arguments.
