tahun = int(input())
if tahun % 400 == 0:
    print("Kabisat")
if tahun % 400 != 0 and tahun % 100 == 0 :
    print("Bukan Kabisat")
if tahun % 400 != 0 and tahun % 100 != 0 and tahun % 4 ==0 :
    print("Kabisat")
else:
    print("Bukan Kabisat")