import streamlit as st

st.write("""
Rino Indra.
# Aplikasi Luas Segitiga
Ini Kali Pertama Saya Membuat Web Aplikasi Menggunakan Streamlit
""")

alas = st.number_input("Masukan Alas", 0)
tinggi = st.number_input("Masukan Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas = int(0.5 * alas * tinggi)
    st.success(f"Luas Segitiganya Adalah {luas}")
    st.balloons()