import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("Editable Table + Multiplier")

# 1️⃣ Store initial data in session_state
if "df" not in st.session_state:
    np.random.seed(0)
    st.session_state.df = pd.DataFrame(
        {"A": np.arange(1, 11), "B": np.random.randn(10)}
    )

# 2️⃣ Sidebar multiplier
multiplier = st.sidebar.number_input("Multiplier (1–10)", 1, 10, 2)

# 3️⃣ Add computed column
editable_df = st.session_state.df.copy()
editable_df["B × k"] = editable_df["B"] * multiplier  # recomputed on each run

edited_df = st.data_editor(
    editable_df,
    column_config={
        "B × k": st.column_config.Column("B × k", disabled=True)  # read-only
    },
    num_rows="dynamic",
    key="editable_table",
)

# 4️⃣ Persist edits (columns A & B)
st.session_state.df = edited_df.drop(columns=["B × k"])

# 5️⃣ Metrics & chart
st.sidebar.metric("Rows", len(st.session_state.df))

st.subheader("B × k Line")
st.line_chart(st.session_state.df.set_index("A")["B"] * multiplier)
