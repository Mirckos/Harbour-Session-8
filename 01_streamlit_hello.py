import numpy as np
import streamlit as st

# --------------------------- UI Header ---------------------------
# The main title at the top of the page
st.title("Streamlit Hello Demo")

# ----------------------- User Instructions -----------------------
# Short description explaining what the slider does
st.write(
    "Move the slider — the script re‑runs automatically "
    "and computes the square of the selected number."
)

# -------------------------- Slider -------------------------------
# Slider widget returning an int in the range 0–100
value = st.slider("Number (0–100)", 0, 100, 25)

# ----------------------- Computation -----------------------------
# Display the square of the chosen value
st.write(f"Square: {value**2}")

# -------------------- Demonstrate Rerun --------------------------
# Show a random number on each run to emphasize reruns
st.write(f"Random number for this run: {np.random.randint(0, 1000)}")
