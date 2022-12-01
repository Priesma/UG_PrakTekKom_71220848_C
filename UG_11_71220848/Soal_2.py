print("priksa kelipatan 9")
masuk = int(input("Masukan Angka : "))
def kelipatan_sembilan():
    jawaban = (masuk%9)
    return jawaban

if kelipatan_sembilan()==0:
    print("BENAR")

else:
    print("SALAH")