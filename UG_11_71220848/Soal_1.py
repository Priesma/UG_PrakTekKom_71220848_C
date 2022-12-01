def penjumlahan(satu,dua):
    hasil = satu + dua
    return hasil

def pengurangan(satu,dua):
    hasil = satu - dua
    return hasil

def perkalian(satu,dua):
    hasil = satu * dua
    return hasil

def pembagian(satu,dua):
    hasil = satu / dua
    return hasil

print("=========================")
print(' 1. Jumlah   [+] ')
print(' 2. Kurang   [-] ')
print(' 3. Kali     [*] ')
print(' 4. Bagi     [/] ')
print("=========================")
operasi = input("Pilih operasi (1/2/3/4): ")
print("=========================")
satu = eval(input('Masukkan bilangan pertama: '))
dua = eval(input('Masukkan bilangan kedua: '))
if operasi == '1':
  print(f"Hasil operasi dari ",satu,"+",dua,"=",penjumlahan(satu,dua))

elif operasi == '2':
  print(f"Hasil operasi dari ",satu,"-",dua,"=",pengurangan(satu,dua))

elif operasi == '3':
  print(f"Hasil operasi dari ",satu,"*",dua,"=",perkalian(satu,dua))

elif operasi == '4':
  print(f"Hasil operasi dari ",satu,"/",dua,"=",pembagian(satu,dua))