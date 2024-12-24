import streamlit as st

st.title("Halaman Dashboard")

# Fungsi untuk menghitung dan menyimpan total tabungan
def total():
    total_nabung = sum(t["Jumlah"] for t in st.session_state["Jumlah"] if t["Tipe"] == "Menabung")
    
    return f"Total tabungan kamu: {total_nabung}"

st.write(total())
