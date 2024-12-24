import streamlit as st

# Slide bar directory
dashboard = st.Page("./fitur/dashboard.py", title = "Dashboard")
nabung = st.Page("./fitur/nabung.py", title = "Nabung")
penarikan = st.Page("./fitur/penarikan.py", title = "Penarikan")

pg = st.navigation(
    {
       "Dashboard": [dashboard],
       "Transaksi": [nabung, penarikan],
    }
)

if "Jumlah" not in st.session_state:
    st.session_state["Jumlah"] = []
# menjalankan nvigasi
pg.run()



