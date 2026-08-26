import streamlit as st
import json
import os

FILE_DATA = "todo_data.json"

def muat_data():
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, "r") as file:
                return json.load(file)
        except:
            return []
    return []

def simpan_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)

st.set_page_config(page_title="To-Do List App", page_icon="📝")

st.title("📝 Aplikasi To-Do List")
st.write("Kelola daftar tugas harian Anda.")

if "daftar_tugas" not in st.session_state:
    st.session_state.daftar_tugas = muat_data()

st.subheader("Tambah Tugas Baru")
with st.form(key="form_tugas", clear_on_submit=True):
    tugas_baru = st.text_input("Tulis tugas yang ingin dikerjakan:")
    tombol_tambah = st.form_submit_button("Tambah Tugas")

if tombol_tambah:
    if tugas_baru.strip() != "":
        st.session_state.daftar_tugas.append(tugas_baru)
        simpan_data(st.session_state.daftar_tugas)
        st.success(f"Berhasil menambahkan: **{tugas_baru}**")
        st.rerun()
    else:
        st.warning("Tugas tidak boleh kosong!")

st.divider()

st.subheader("Daftar Tugas Anda")

if not st.session_state.daftar_tugas:
    st.info("Belum ada tugas. Nikmati waktu luangmu! 🎉")
else:
    for index, tugas in enumerate(st.session_state.daftar_tugas):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.write(f"**{index + 1}.** {tugas}")
            
        with col2:
            if st.button("Hapus", key=f"hapus_{index}"):
                st.session_state.daftar_tugas.pop(index)
                simpan_data(st.session_state.daftar_tugas)
                st.rerun()

if st.session_state.daftar_tugas:
    st.divider()
    if st.button("🗑️ Hapus Semua Tugas"):
        st.session_state.daftar_tugas.clear()
        simpan_data(st.session_state.daftar_tugas)
        st.rerun()