import streamlit as st

# Judul aplikasi
st.title("Aplikasi Multi Fungsi Sederhana")

# Menu di sidebar
menu = st.sidebar.radio("Pilih Menu:", ["Kalkulator", "Konversi Suhu", "Fibonacci"])

# ==========================
# KALKULATOR
# ==========================
if menu == "Kalkulator":
    st.header("Kalkulator Sederhana")

    # input angka
    angka1 = st.number_input("Masukkan Angka Pertama", value=0.0)
    angka2 = st.number_input("Masukkan Angka Kedua", value=0.0)

    # pilih operator
    operasi = st.selectbox("Pilih Operasi", ["+", "-", "*", "/"])

    # tombol hitung
    if st.button("Hitung"):
        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/":
            if angka2 == 0:
                hasil = "Error! Pembagian dengan 0"
            else:
                hasil = angka1 / angka2
        st.write("Hasil =", hasil)

# ==========================
# KONVERSI SUHU
# ==========================
elif menu == "Konversi Suhu":
    st.header("Konversi Suhu")

    # input nilai suhu
    satuan = st.selectbox("Pilih Satuan Asal", ["Celcius", "Reamur", "Fahrenheit"])
    nilai = st.number_input("Masukkan Nilai Suhu", value=0.0)

    # konversi berdasarkan satuan
    if satuan == "Celcius":
        st.write("Reamur =", (4/5) * nilai)
        st.write("Fahrenheit =", (9/5) * nilai + 32)
    elif satuan == "Reamur":
        st.write("Celcius =", (5/4) * nilai)
        st.write("Fahrenheit =", (9/4) * nilai + 32)
    elif satuan == "Fahrenheit":
        st.write("Celcius =", (5/9) * (nilai - 32))
        st.write("Reamur =", (4/9) * (nilai - 32))

# ==========================
# FIBONACCI
# ==========================
elif menu == "Fibonacci":
    st.header("Deret Fibonacci")

    n = st.number_input("Masukkan jumlah bilangan", min_value=1, step=1, value=5)

    if st.button("Tampilkan"):
        # logika fibonacci dasar
        fib = []
        a, b = 0, 1
        for i in range(n):
            fib.append(a)
            temp = a + b
            a = b
            b = temp
        st.write("Deret Fibonacci:", fib)
