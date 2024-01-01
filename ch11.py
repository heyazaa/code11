import mysql.connector
import matplotlib.pyplot as plt

def connectionDataBase():
    connector = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "uty"
    )

    if connector.is_connected:
        print("Database terkoneksi")
        return connector
    else :
        print("Database gagal terkoneksi")
        return False

def tampilkanNim(inputUser):
    try:
        conn = connectionDataBase()
        cursor = conn.cursor()
        sql = "SELECT agama, mtk, ipa FROM nilai WHERE nim = %s"
        search = (inputUser,)
        cursor.execute(sql, search)
        result = cursor.fetchall()
        if result:
            for i in result:
                matkul = ("agama", "mtk", "ipa")
                hasil = i
                plt.bar(matkul, hasil)
                plt.show()       
        else :
            print("Data tidak ditemukan")
    except mysql.connector.Error as error:
        print("Terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()

def inputData(nim, nama, agama, mtk, ipa):
    try:
        conn = connectionDataBase()
        cursor = conn.cursor()
        sql = "INSERT INTO nilai (nim, nama, agama, mtk, ipa) VALUES (%s, %s, %s, %s, %s)"
        data = (nim, nama, agama, mtk, ipa)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil ditambahkan")
    except mysql.connector.Error as error:
        print("Terjadi kesalahan saat input")
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()

def editData(nim, nama, agama, mtk, ipa):
    try:
        conn = connectionDataBase()
        cursor = conn.cursor()
        sql = "UPDATE nilai SET nama = %s WHERE nim = %s"
        data = ("Fenti", "52391")
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil diperbaharui")
    except mysql.connector.Error as error:
        print("Terjadi kesalahan")
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()

def hapusData(nim):
    try:
        conn = connectionDataBase()
        cursor = conn.cursor()
        sql = "DELETE FROM nilai WHERE nim = %s"
        data = (nim,)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil dihapus")
    except mysql.connector.Error as error:
        print("Terjadi kesalahan")
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()

def menu():
    print("Program Menampilkan Data")
    print("1. Tampilkan visualisasi berdasarkan nim")
    print("2. Input data")
    print("3. Edit data")
    print("4. Hapus data")

while True:
    menu()
    inputmenu = int(input("Masukkan Menu [1-4] : "))
    if inputmenu == 1:
        inputNim = input("Masukkan nim : ")
        tampilkanNim(inputNim)
    elif inputmenu == 2:
        inputNim = input("Masukkan nim : ")
        inputNama = input("Masukkan nama : ")
        inputAgama = input("Masukkan nilai agama : ")
        inputMtk = input("Masukkan nilai mtk : ")
        inputIpa = input("Masukkan nilai ipa : ")
        inputData(inputNim, inputNama, inputAgama, inputMtk, inputIpa)
    elif inputmenu == 3:
        inputNim = input("Masukkan nim : ")
        inputNama = input("Masukkan nama : ")
        inputAgama = input("Masukkan nilai agama : ")
        inputMtk = input("Masukkan nilai mtk : ")
        inputIpa = input("Masukkan nilai ipa : ")
        editData(inputNim, inputNama, inputAgama, inputMtk, inputIpa)
    elif inputmenu == 4:
        inputNim = input("Masukkan nim : ")
        hapusData(inputNim)

