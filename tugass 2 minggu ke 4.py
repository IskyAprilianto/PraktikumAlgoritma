ulang = "y"
while ulang == "y":
    bulan = int(input("masukan bulan (1-12) : "))
    tahun = int(input("masukan tahun : "))
    if (bulan == 1):
     hari = 31
    elif(bulan == 2):
     if((tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0):
        hari = 29
     else:
         hari = 28
    elif(bulan == 3):
         hari = 31
    elif(bulan == 4): 
         hari = 30
    elif(bulan == 5):
         hari = 31
    elif(bulan == 6):
         hari = 30
    elif(bulan == 7):
         hari = 31
    elif(bulan == 8):
         hari = 31
    elif(bulan == 9):
         hari = 30
    elif(bulan == 10):
         hari = 31
    elif(bulan == 11):
         hari = 30
    elif(bulan == 12):
         hari = 31
    else:
         hari = -1
    print("ada", hari, "hari di bulan ke", bulan)
    ulang = input("ketik y untuk ulang, ketik n untuk berhenti:")
    if ulang == "n":
        print("terimakasih telah menggunakan program ini.")
        break