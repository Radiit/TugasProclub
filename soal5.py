a = int(input())

for i in range(a):
  for j in range(i):
    print("", end=" ")
  for m in range(a):
    print("*", end=" ")
  a = a-1
  print(" ")