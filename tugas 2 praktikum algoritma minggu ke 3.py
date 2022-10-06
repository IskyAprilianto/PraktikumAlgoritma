#Isky Dwi Aprilianto-064002200006
import math

a= int(input("masukan nilai A : "))
b= int(input("masukan nilai B : "))
c= int(input("masukan nilai C : "))

if (a ==  0):
    print("bukan merupakan persamaan kuadrat, karena nilai A=" + str(a))
else:
    D = pow(b, 2)-(4*a*c)
    if (D > 0):
        x1 = ((-b)+ math.sqrt(D))/(2*a)
        x2 = ((-b)- math.sqrt(D))/(2*a);
        print("persamaan kuadrat = " +str(a) + "x^2 +" + str(b) + "x +" + str (c))
        print("Determinannya = " + str (D))
        print("memiliki Akar Berbeda")
        print("Akar x1 = " + str (x1))
        print("Akar x2 = " + str (x2)) 
    elif(D == 0) :
        x1 = (-b)/(2*a)
        x2 = x1
        print("persamaan kuadrat = " +str(a) + "x^2 +" + str(b) + "x +" + str (c))
        print("Determinannya = " + str (D))
        print("merupakan Akar Berbeda")
        print = ("akar = " + str (x2))
    elif( D < 0 ):
        print("persamaan kuadrat = " +str(a) + "x^2 +" + str(b) + "x +" + str (c))
        print("Determinannya = " + str (D))
        print("merupakan Akar Imaginer")
        print("Akar x1 = -" + str(b) + " + √" + str(D) + "/2*" + str (a))
        print("Akar x2 = -" + str(b) + " + √" + str(D) + "/2*" + str (a))
    else :
        print("error, masukan angka yang valid")