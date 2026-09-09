"""Mini-project 1: filterable sales KPI dashboard with synthetic data."""

from datetime import date, timedelta

import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")


@st.cache_data
def make_sales(seed=42):
    """Create deterministic lesson data; replace with a real source later."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(date.today() - timedelta(days=89), periods=90)
    return pd.DataFrame(
        {
            "date": np.repeat(dates, 3),
            "region": np.tile(["North", "South", "West"], len(dates)),
            "revenue": rng.integers(500, 2500, len(dates) * 3),
            "orders": rng.integers(5, 35, len(dates) * 3),
        }
    )


sales = make_sales()
st.title("Sales Dashboard")
with st.sidebar:
    st.header("Filters")
    regions = st.multiselect("Regions", sorted(sales.region.unique()), default=sorted(sales.region.unique()))
    date_range = st.date_input("Date range", value=(sales.date.min().date(), sales.date.max().date()))

if not regions or len(date_range) != 2:
    st.warning("Choose at least one region and a complete date range.")
    st.stop()

start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
filtered = sales[sales.region.isin(regions) & sales.date.between(start, end)]
if filtered.empty:
    st.warning("No rows match those filters.")
    st.stop()

revenue = int(filtered.revenue.sum())
orders = int(filtered.orders.sum())
average_order = revenue / orders if orders else 0
one, two, three = st.columns(3)
one.metric("Revenue", f"${revenue:,}")
two.metric("Orders", f"{orders:,}")
three.metric("Revenue per order", f"${average_order:,.2f}")

daily = filtered.groupby("date", as_index=False)[["revenue", "orders"]].sum()
st.line_chart(daily, x="date", y="revenue")
by_region = filtered.groupby("region", as_index=False).revenue.sum()
st.bar_chart(by_region, x="region", y="revenue")
st.dataframe(filtered.tail(200), width="stretch", hide_index=True)
