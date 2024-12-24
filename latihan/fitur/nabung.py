import streamlit as st

st.title("Halaman Menabung")

# halaman nabung
with st.form("Menabung"):
    nama = st.text_input("Masukan Nama")
    jumlah = st.number_input("Masukan Jumlah (Rp.)", min_value=0)

    submit = st.form_submit_button(label="Menabung")

    if submit:
        st.session_state["Jumlah"].append({
            "Tipe": "Nabung",
            "Nama": nama,
            "Jumlah": jumlah
            })
        st.success("Berhasil Menabung")
    else:
        st.error("Gagal Menabung")