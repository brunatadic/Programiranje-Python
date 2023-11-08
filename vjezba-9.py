import random
x = random.randint(1, 10)
y = int(input("pogodi broj x"))
if x == y:
    print("bravo, pogodio si traženi broj")
else: 
    print("netočno, traženi broj je bio {0}".format(x))
