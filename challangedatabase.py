import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "5230411119"
)

def guru():
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM guru")
    result = mycursor.fetchall()
    print(result)

def siswa():
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM siswa")
    result = mycursor.fetchall()
    print(result)

def menu():
    print("======DATA SEKOLAH======")
    print("1.DATA GURU")
    print("2.DATA SISWA")
    print("3.EXIT")

while True:
    menu()
    inputmenu = int(input("MASUKAN MENU (1-2) : "))
    if inputmenu == 1:
        guru()
    elif inputmenu == 2:
        siswa()
    elif inputmenu == 3:
        break
    else:
        print("input eror")
        continue


