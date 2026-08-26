import streamlit as st
import json
import os 

# nama file tempat menyimpan data
FILE_DATA = "todo_data.json" 

# fungsi untuk membaca dan menyimpan data
def muat_data():
    """membaca data dari file json jika file ada"""
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            return json.load(file)
    return[]

def simpan_data(data):
    """Meyimpan data ke dalam file JSON"""
    with open(FILE_DATA.json, "w") as file:
        json.dump(data, file, indent=4)

st.set_page_config(page_title="To-Do List App", page_icon="📝")

st.title("📝Aplikasi To-Do List")
st.write("lu pelupa? buat To-Do list lu disini biar keseharian lu mudah")

#1. inisialisasi session_rate agar data tidak hilang saat tombol diklik
if "daftar_tugas" not in st.session_state:
    st.session_state.daftar_tugas = muat_data()

#2. form untuk menambah tugas baru
st.subheader("Tambah Tugas Baru")
with st.form(key="form_tugas", clear_on_submit=True):
    tugas_baru = st.text_input("Tulis tugas yang ingin dikerjakan:")
    tombol_tambah = st.form_submit_button("Tambah Tugas")

if tombol_tambah:
    if tugas_baru.strip() != "":
        st.session_state.daftar_tugas.append(tugas_baru)
        simpan_data(st.session_state.daftar_tugas)
        st.success(f"Berhasil Menambahkan: **{tugas_baru}**")
        st.rerun()
    else:
        st.warning("Tugas tidak boleh kosong")

st.divider() 

#3. menampilkan dan mengelola daftar tugas
st.subheader("Daftar Tugas Anda")

if not st.session_state.daftar_tugas:
    st.info("Belum ada tugas. yahaha nganggur lu yak")
else:
    #menampilkan tugas satu persatu menggunakan checkbox
    for index, tugas in enumerate(st.session_state.daftar_tugas):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"**{index + 1}.** {tugas}")
        with col2:
            #tombol hapus untuk masing-masing tugas
            if st.button("Hapus", key=f"hapus_{index}"):
                st.session_state.daftar_tugas.pop(index)
                simpan_data(st.session_state.daftar_tugas)
                st.rerun()

#4. tombol khusus: hapus semua tugas
if st.session_state.daftar_tugas:
    st.divider()
    if st.button("🗑️ Hapus Semua Tugas"):
        st.session_state.daftar_tugas.clear()
        simpan_data(st.session_state.daftar_tugas)
        st.rerun()