def angka_sama(angka): 
    lisa = []
    for i in angka:   
        jumlah = angka.count(i)
        if jumlah == 1:
            lisa.append(i)   
    return lisa
            
a = input()
b = angka_sama(a)
lisi = list(map(int,b))

print(lisi)
