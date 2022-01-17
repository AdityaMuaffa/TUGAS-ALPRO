tahun = 2021

#siswa 1
nim1 = input ("Nim         :")
nim1 = int(nim1)
nama1 = input ("Nama        :")
tahun_lahir1 = input ("Tahun lahir :")
tahun_lahir1 = int(tahun_lahir1)
print("\n")
umur1 = tahun - tahun_lahir1

#siswa 2
nim2 = input ("Nim         :")
nim2 = int(nim2)
nama2 = input ("Nama        :")
tahun_lahir2 = input ("Tahun lahir :")
tahun_lahir2 = int(tahun_lahir2)
print("\n")
umur2 = tahun - tahun_lahir2

#siswa 3
nim3 = input ("Nim         :")
nim3 = int(nim3)
nama3 = input ("Nama        :")
tahun_lahir3 = input ("Tahun lahir :")
tahun_lahir3 = int(tahun_lahir3)
print("\n")
umur3 = tahun - tahun_lahir3

#siswa 4
nim4 = input ("Nim         :")
nim4 = int(nim4)
nama4 = input ("Nama        :")
tahun_lahir4 = input ("Tahun lahir :")
tahun_lahir4 = int(tahun_lahir4)
print("\n")
umur4 = tahun - tahun_lahir4

#siswa 5
nim5 = input ("Nim         :")
nim5 = int(nim5)
nama5 = input ("Nama        :")
tahun_lahir5 = input ("Tahun lahir :")
tahun_lahir5 = int(tahun_lahir5)
print("\n")
umur5 = tahun - tahun_lahir5

#output siswa 1
def siswa1():
    print("Nim         :",nim1)
    print("Nama        : "+nama1)
    print("Tahun lahir :",tahun_lahir1)
    print("Umur        :",umur1)
    print("\n")

#output siswa 2
def siswa2():
    print("Nim         :",nim2)
    print("Nama        : "+nama2)
    print("Tahun lahir :",tahun_lahir2)
    print("Umur        :",umur2)
    print("\n")

#output siswa 3
def siswa3():
    print("Nim         :",nim3)
    print("Nama        : "+nama3)
    print("Tahun lahir :",tahun_lahir3)
    print("Umur        :",umur3)
    print("\n")

#output siswa 4
def siswa4():
    print("Nim         :",nim4)
    print("Nama        : "+nama4)
    print("Tahun lahir :",tahun_lahir4)
    print("Umur        :",umur4)
    print("\n")

#output siswa 5
def siswa5():
    print("Nim         :",nim5)
    print("Nama        : "+nama5)
    print("Tahun lahir :",tahun_lahir5)
    print("Umur        :",umur5)
    print("\n")


#program output
if tahun_lahir1 < tahun_lahir2:
    if tahun_lahir2 < tahun_lahir3:
        if tahun_lahir3 < tahun_lahir4:
            if tahun_lahir4 < tahun_lahir5:
                pertama = siswa1()
                kedua = siswa2()
                ketiga = siswa3()
                keempat = siswa4()
                kelima = siswa5()

if tahun_lahir2 < tahun_lahir1:
    if tahun_lahir1 < tahun_lahir3:
        if tahun_lahir3 < tahun_lahir4:
            if tahun_lahir4 < tahun_lahir5:
                pertama = siswa2()
                kedua = siswa1()
                ketiga = siswa3()
                keempat = siswa4()
                kelima = siswa5()

if tahun_lahir2 < tahun_lahir1:
    if tahun_lahir1 < tahun_lahir3:
        if tahun_lahir4 < tahun_lahir3:
            if tahun_lahir3 < tahun_lahir5:
                pertama = siswa2()
                kedua = siswa1()
                ketiga = siswa4()
                keempat = siswa3()
                kelima = siswa5()

if tahun_lahir2 < tahun_lahir1:
    if tahun_lahir1 < tahun_lahir3:
        if tahun_lahir3 < tahun_lahir4:
            if tahun_lahir5 < tahun_lahir4:
                pertama = siswa2()
                kedua = siswa1()
                ketiga = siswa3()
                keempat = siswa5()
                kelima = siswa4()

if tahun_lahir1 < tahun_lahir2:
    if tahun_lahir3 < tahun_lahir2:
        if tahun_lahir2 < tahun_lahir4:
            if tahun_lahir4 < tahun_lahir5:
                pertama = siswa1()
                kedua = siswa3()
                ketiga = siswa2()
                keempat = siswa4()
                kelima = siswa5()

if tahun_lahir1 < tahun_lahir2:
    if tahun_lahir2 < tahun_lahir3:
        if tahun_lahir4 < tahun_lahir3:
            if tahun_lahir3 < tahun_lahir5:
                pertama = siswa1()
                kedua = siswa2()
                ketiga = siswa4()
                keempat = siswa3()
                kelima = siswa5()

if tahun_lahir1 < tahun_lahir2:
    if tahun_lahir2 < tahun_lahir3:
        if tahun_lahir3 < tahun_lahir4:
            if tahun_lahir5 < tahun_lahir4:
                pertama = siswa1()
                kedua = siswa2()
                ketiga = siswa3()
                keempat = siswa5()
                kelima = siswa4()


if tahun_lahir5 < tahun_lahir4:
    if tahun_lahir4 < tahun_lahir3:
        if tahun_lahir3 < tahun_lahir2:
            if tahun_lahir2 < tahun_lahir1:
                pertama = siswa5()
                kedua = siswa4()
                ketiga = siswa3()
                keempat = siswa2()
                kelima = siswa1()

if tahun_lahir1 < tahun_lahir3:
    if tahun_lahir3 < tahun_lahir2:
        if tahun_lahir2 < tahun_lahir5:
            if tahun_lahir5 < tahun_lahir4:
                pertama = siswa1()
                kedua = siswa3()
                ketiga = siswa2()
                keempat = siswa5()
                kelima = siswa4()

if tahun_lahir3 < tahun_lahir1:
    if tahun_lahir1 < tahun_lahir2:
        if tahun_lahir2 < tahun_lahir5:
            if tahun_lahir5 < tahun_lahir4:
                pertama = siswa3()
                kedua = siswa1()
                ketiga = siswa2()
                keempat = siswa5()
                kelima = siswa4()

if tahun_lahir3 < tahun_lahir4:
    if tahun_lahir4 < tahun_lahir5:
        if tahun_lahir5 < tahun_lahir1:
            if tahun_lahir1 < tahun_lahir2:
                pertama = siswa3()
                kedua = siswa4()
                ketiga = siswa5()
                keempat = siswa1()
                kelima = siswa2()

if tahun_lahir2 < tahun_lahir4:
    if tahun_lahir4 < tahun_lahir5:
        if tahun_lahir5 < tahun_lahir3:
            if tahun_lahir3 < tahun_lahir1:
                pertama = siswa2()
                kedua = siswa4()
                ketiga = siswa5()
                keempat = siswa3()
                kelima = siswa1()

if tahun_lahir1 < tahun_lahir3:
    if tahun_lahir3 < tahun_lahir5:
        if tahun_lahir5 < tahun_lahir4:
            if tahun_lahir4 < tahun_lahir2:
                pertama = siswa1()
                kedua = siswa3()
                ketiga = siswa5()
                keempat = siswa4()
                kelima = siswa2()

if tahun_lahir2 < tahun_lahir3:
    if tahun_lahir3 < tahun_lahir5:
        if tahun_lahir5 < tahun_lahir4:
            if tahun_lahir4 < tahun_lahir1:
                pertama = siswa2()
                kedua = siswa3()
                ketiga = siswa5()
                keempat = siswa4()
                kelima = siswa1()

if tahun_lahir1 < tahun_lahir3:
    if tahun_lahir3 < tahun_lahir4:
        if tahun_lahir4 < tahun_lahir5:
            if tahun_lahir5 < tahun_lahir2:
                pertama = siswa1()
                kedua = siswa3()
                ketiga = siswa4()
                keempat = siswa5()
                kelima = siswa2()

if tahun_lahir1 < tahun_lahir4:
    if tahun_lahir4 < tahun_lahir3:
        if tahun_lahir3 < tahun_lahir5:
            if tahun_lahir5 < tahun_lahir2:
                pertama = siswa1()
                kedua = siswa4()
                ketiga = siswa3()
                keempat = siswa5()
                kelima = siswa2()

if tahun_lahir3 < tahun_lahir5:
    if tahun_lahir5 < tahun_lahir1:
        if tahun_lahir1 < tahun_lahir4:
            if tahun_lahir4 < tahun_lahir2:
                pertama = siswa3()
                kedua = siswa5()
                ketiga = siswa1()
                keempat = siswa4()
                kelima = siswa2()

if tahun_lahir1 < tahun_lahir4:
    if tahun_lahir4 < tahun_lahir5:
        if tahun_lahir5 < tahun_lahir3:
            if tahun_lahir3 < tahun_lahir2:
                pertama = siswa1()
                kedua = siswa4()
                ketiga = siswa5()
                keempat = siswa3()
                kelima = siswa2()

if tahun_lahir3 < tahun_lahir1:
    if tahun_lahir1 < tahun_lahir4:
        if tahun_lahir4 < tahun_lahir2:
            if tahun_lahir2 < tahun_lahir5:
                pertama = siswa3()
                kedua = siswa1()
                ketiga = siswa4()
                keempat = siswa2()
                kelima = siswa5()

if tahun_lahir2 < tahun_lahir3:
    if tahun_lahir3 < tahun_lahir5:
        if tahun_lahir5 < tahun_lahir1:
            if tahun_lahir1 < tahun_lahir4:
                pertama = siswa2()
                kedua = siswa3()
                ketiga = siswa5()
                keempat = siswa1()
                kelima = siswa4()

if tahun_lahir2 < tahun_lahir3:
    if tahun_lahir3 < tahun_lahir1:
        if tahun_lahir1 < tahun_lahir5:
            if tahun_lahir5 < tahun_lahir4:
                pertama = siswa2()
                kedua = siswa3()
                ketiga = siswa1()
                keempat = siswa5()
                kelima = siswa4()

if tahun_lahir4 < tahun_lahir1:
    if tahun_lahir1 < tahun_lahir5:
        if tahun_lahir5 < tahun_lahir2:
            if tahun_lahir2 < tahun_lahir3:
                pertama = siswa4()
                kedua = siswa1()
                ketiga = siswa5()
                keempat = siswa2()
                kelima = siswa3()

if tahun_lahir4 < tahun_lahir5:
    if tahun_lahir5 < tahun_lahir1:
        if tahun_lahir1 < tahun_lahir3:
            if tahun_lahir3 < tahun_lahir2:
                pertama = siswa4()
                kedua = siswa5()
                ketiga = siswa1()
                keempat = siswa3()
                kelima = siswa2()

if tahun_lahir2 < tahun_lahir5:
    if tahun_lahir5 < tahun_lahir1:
        if tahun_lahir1 < tahun_lahir4:
            if tahun_lahir4 < tahun_lahir3:
                pertama = siswa2()
                kedua = siswa5()
                ketiga = siswa1()
                keempat = siswa4()
                kelima = siswa3()

if tahun_lahir3 < tahun_lahir4:
    if tahun_lahir4 < tahun_lahir2:
        if tahun_lahir2 < tahun_lahir5:
            if tahun_lahir5 < tahun_lahir1:
                pertama = siswa3()
                kedua = siswa4()
                ketiga = siswa2()
                keempat = siswa5()
                kelima = siswa1()


