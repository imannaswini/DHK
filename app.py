import streamlit as st
from core.diffie_hellman import generate_keys

st.title("Diffie-Hellman Key Exchange")

p = st.number_input("Prime Number (p)", value=23)
g = st.number_input("Generator (g)", value=5)

a = st.number_input("Private Key A", value=6)
b = st.number_input("Private Key B", value=15)

if st.button("Generate"):
    A, B, key_A, key_B = generate_keys(p, g, a, b)

    st.write("### Public Keys")
    st.write(f"A sends: {A}")
    st.write(f"B sends: {B}")

    st.write("### Shared Key")
    st.success(f"A's Key: {key_A}")
    st.success(f"B's Key: {key_B}")