"""
x = int(input("masukan nilai x = "))
if x%2 == 0:
    print(x, "adalah bilangan genap")
else:
    print(x, "adalah bilangan ganjil")


usia = int(input("Masukan usia anda : "))
if usia >= 17:
    print("Wajib Punya KTP")
else:
    print("Belum bisa mendapatkan KTP")
"""

n = float(input("Masukan nilai rata-rata : "))
m = input("punya prestasi akademik?")

if n>=95 and m=="ya":
    print("dapat beasiswa 100%")
elif n>=90 and n<95 and m=="ya":
    print("dapat beasiswa 75%")
elif n>=90 and n<95 and m=="tidak":
    print("dapat beasiswa 50%")
else:
    print("tidak layak beasiswa")