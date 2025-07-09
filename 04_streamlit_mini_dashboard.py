import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("Mini Dashboard: Map + Filters")


@st.cache_data
def load_data():
    # Generate reproducible synthetic data roughly within Europe
    np.random.seed(42)
    return pd.DataFrame(
        {
            "city": [f"City {i}" for i in range(200)],
            "lat": np.random.uniform(40, 60, 200),  # latitude 40–60° N
            "lon": np.random.uniform(-5, 15, 200),  # longitude 5° W to 15° E
            "value": np.random.randint(0, 100, 200),  # numeric metric to filter
        }
    )


# Full dataset cached above
df = load_data()

# ---------- Sidebar filters ----------
with st.sidebar:
    st.header("Filters")

    # Range slider keeps only rows whose `value` lies inside the interval
    v_min, v_max = st.slider("Value range", 0, 100, (20, 80))

    # Rows that survive the `value` filter; needed to bound the next widget
    max_rows = df.query("@v_min <= value <= @v_max").shape[0]

    # How many points to plot: limited to the filtered row count
    sample = st.number_input(
        "Sample size",
        min_value=1,
        max_value=max_rows if max_rows > 0 else 1,
        value=min(50, max_rows if max_rows > 0 else 1),
    )

    # Optional toggle for raw-data visibility
    show_table = st.checkbox("Show table", True)

# Apply filters + sampling for display
filtered = df.query("@v_min <= value <= @v_max").sample(sample)

# ---------- Visual output ----------
st.subheader("Distribution Map")
# Streamlit's built-in map accepts a DataFrame with 'lat' and 'lon'
st.map(filtered[["lat", "lon"]])

if show_table:
    st.dataframe(filtered)
