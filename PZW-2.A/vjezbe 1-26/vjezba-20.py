#napiši program koji unosi bodove pet najboljih natjecanja
# u trčanju na 100m te ispisuje koliko je
#bodova imao drugi najbolji natjecatelj

lista = []

for i in range(5):
    a = int(input("upiši broj:"))
    lista.append(a)

lista.sort()
print(lista)
print(lista[-2])