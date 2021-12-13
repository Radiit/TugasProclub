def oke(angka):
  lisa = []
  for i in angka:
    jumlah = angka.count(i)
    if jumlah == 1:
      lisa.append(i)
  return lisa

a = input()
panggil_fungsi = oke(a)
lis1= list(map(int,panggil_fungsi)) 

print(lis1)