#fungsi rekursif
jumlah = int(input("masukan jumlah : "))
def penjumlahan (angka = 0, jml = 0, i = 1):
    if (jml <= 0):
        return 0
    else :
        angka = int(input("masukan bilangan ke-"  +str(i)+ ":"))
        if (jml ==1):
            return (angka)
        else :
            i+=1
            return angka + penjumlahan(angka, jml-1, i)
nilai = penjumlahan(jml=jumlah)
print("hasil dari penjumlahan adalah:" + str(nilai))