import tkinter as tk
import sqlite3
from tkinter import messagebox

def simpan_data_ke_sqlite(Nama_Siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas):

# Membuka atau membuat database SQLite
    conn = sqlite3.connect("DBTugas8.db")
    cursor = conn.cursor()

# Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS Nilai_Siswa
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Nama_Siswa TEXT,
                    Biologi INTEGER,
                    Fisika INTEGER, 
                    Inggris INTEGER,
                    Prediksi_Fakultas TEXT)''')

# Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO Nilai_Siswa (Nama_Siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas) VALUES (?, ?, ?, ?, ?)",
                    (Nama_Siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas))

# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

top = tk.Tk()
top.title("Kelas B") #Untuk memberi nama judul
top.geometry("500x500") 
top.resizable(False, False)

def Prediksi_Fakultas(Biologi, Fisika, Inggris):
    if Fisika < Biologi > Inggris:
        return "Kedokteran"
    elif Biologi < Fisika > Inggris:
        return "Teknik"
    elif Biologi < Inggris > Fisika:
        return "Bahasa"
    else :
        return "Prodi Lainnya"


#Menampilkan fungsi
def show():
    namasiswa = str(NS1.get())
    nilai1 = B1.get()
    nilai2 = F1.get()
    nilai3 = I1.get()

    if not nilai1 or not nilai2 or not nilai3:
        messagebox.showwarning("Peringatan", "Harap isi semua nilai dan nama mahasiswa.")
        return

    try:
        nilai1 = int(nilai1)
        nilai2 = int(nilai2)
        nilai3 = int(nilai3)

    except ValueError:
        # Jika gagal, tampilkan pesan peringatan
        messagebox.showwarning("Peringatan", "Harap isi semua nilai dengan angka.")
        return
    
    if not namasiswa.isalpha():
        messagebox.showwarning("Peringatan", "Harap isi nama dengan huruf.")
        return

    hasilMhs = f"Nama Mahasiswa: {namasiswa}"
    hasil1 = f"Nilai Biologi: {nilai1}"
    hasil2 = f"Nilai Fisika: {nilai2}"
    hasil3 = f"Nilai Bahasa: {nilai3}"

    prediksi = Prediksi_Fakultas(int(nilai1), int(nilai2), int(nilai3))

    hasilPrediksi = f"Hasil Prediksi: {prediksi}"

    label_hasilMhs.config(text=hasilMhs)
    label_hasil1.config(text=hasil1)
    label_hasil2.config(text=hasil2)
    label_hasil3.config(text=hasil3)
    label_hasilprediksi.config(text=hasilPrediksi)

    frame_hasil.pack()
    simpan_data_ke_sqlite(namasiswa, int(nilai1), int(nilai2), int(nilai3), prediksi)
    messagebox.showinfo("Info","Data Tersimpan")

# Label Judul
label_judul = tk.Label(top, text="Prediksi Prodi Pilihan", font=("Times",14,"bold"), fg='Black')
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(top, labelanchor="n",pady=10, padx=10)
frame_input.pack()


# Label Nama Mahasiswa
NS = tk.Label(frame_input, text="Masukkan Nama : ", bg="#E6E6FA", font=("Times",10,"bold"))
NS.grid(row=0, column=0, pady=10, sticky="e")
NS1 = tk.Entry(frame_input, bd=2, relief="ridge")
NS1.grid(row=0,column=1)

# Label Nilai Biologi
B = tk.Label(frame_input, text="Nilai Biologi : ", bg="#E6E6FA",font=("Times",10,"bold"))
B.grid(row=1, column=0, pady=10, sticky="e")
B1 = tk.Entry(frame_input, bd=2, relief="ridge")
B1.grid(row=1,column=1)

# Label Nilai Fisika
F = tk.Label(frame_input, text="Nilai Fisika : ", bg="#E6E6FA",font=("Times",10,"bold"))
F.grid(row=2, column=0, pady=10, sticky="e")
F1 = tk.Entry(frame_input, bd=2, relief="ridge")
F1.grid(row=2,column=1)

# Label Nilai Inggris
I = tk.Label(frame_input, text="Nilai Inggris : ", bg="#E6E6FA",font=("Times",10,"bold"))
I.grid(row=3, column=0, pady=10, sticky="e")
I1 = tk.Entry(frame_input, bd=2, relief="ridge")
I1.grid(row=3,column=1)

# Tombol Hasil
btn_hasil = tk.Button(top, text="Submit", command=show, font=("Times", 10 , "bold"), bd=3 )
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(top,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

frame_input.configure(bg="#E6E6FA")  # Warna lavender

# Label Hasil
label_hasilMhs = tk.Label(frame_hasil, text="", bg="#E6E6FA", font=("Times",10,"bold"))
label_hasilMhs.pack(anchor="w", padx=10, pady=5)

label_hasil1 =  tk.Label(frame_hasil,text="",bg="#E6E6FA", font=("Times",10,"bold"))
label_hasil1.pack(anchor="w", padx=36, pady=5)

label_hasil2 =  tk.Label(frame_hasil,text="",bg="#E6E6FA", font=("Times",10,"bold"))
label_hasil2.pack(anchor="w", padx=39, pady=5)

label_hasil3 =  tk.Label(frame_hasil,text="",bg="#E6E6FA", font=("Times",10,"bold"))
label_hasil3.pack(anchor="w", padx=36, pady=5)

label_hasilprediksi = tk.Label(frame_hasil, text="",bg="#E6E6FA", font=("Times",10,"bold"))
label_hasilprediksi.pack(anchor="w", padx=25, pady=5)

frame_hasil.configure(bg="#E6E6FA")   # Warna lavender

top.mainloop()