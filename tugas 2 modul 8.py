#rekursif bilangan pangkat
def pangkat(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat(x,y-1)

x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))
nilai = x**y
print("hasil bilangan pangkat adalah : ", str(nilai))