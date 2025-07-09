import time

import numpy as np
import streamlit as st

st.title("Cache + Smart Progress Bar")


# 1️⃣ Cached heavy computation (no internal spinner)
@st.cache_data(show_spinner=False)
def heavy_computation(n: int):
    time.sleep(2)  # simulate expensive work
    return np.square(np.arange(n))


# 2️⃣ Parameters form
with st.form("params"):
    n = st.number_input("Number of squares to compute", 100, 10_000, 1_000, 100)
    run = st.form_submit_button("Run")

# 3️⃣ Run with adaptive progress bar
if run:
    placeholder = st.empty()  # container for bar/info

    tic = time.perf_counter()
    data = heavy_computation(int(n))
    elapsed = time.perf_counter() - tic

    if elapsed > 0.1:  # cold cache
        bar = placeholder.progress(0, "Computing…")
        for i in range(100):
            time.sleep(elapsed / 100)
            bar.progress(i + 1, "Computing…")
        placeholder.empty()
    else:  # cache hit
        placeholder.info(f"⚡️ Cache returned in {elapsed:.2f} s; progress bar skipped.")

    st.success("Done! First 10 results:")
    st.write(data[:10], "…")
