# -*- Isky Dwi Aprilainto -*-

def bulan():
    print("Porgram Untuk Menentukan Hari dan Bulan")

    while True:
        print("Tekan 0 untuk menghentikan program")
        x = int(input('Sekarang bulan ke berapa(1-12)?  '))
        if(x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12):
            print('  Jumlah harinya adalah 31\n')
        elif(x == 2):
            print('  Jumlah harinya adalah 28\n')
        elif x == 0 :
            print("Terimakasih sudah menggunakan program ini.\n")
            break
        else:
            print('  Jumlah harinya adalah 30\n')
            
B = bulan()
print(B)
