# -*- Isky DWi Aprilianto -*-

number =int(input("masukan jumlah maksimal :"))
for i in range(number, 0, -1):
    for j in range (i) :
        print(i, end='')
    print('\r')