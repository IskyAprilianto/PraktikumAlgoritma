#Isky Dwi Aprilianto
#program bilangan prima

num = int(input("Masukan bilangan : "))
def bil_prima(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return f"{num} bukan bilangan prima karena habis dibagi oleh {i}"
            else : 
                return f"{num} adalah bilangan prima"
                
# bila bilangan kurang atau sama dengan satu
    else:
        print(num, "bukan bilangan prima")
    
x = bil_prima(num)
print(x)