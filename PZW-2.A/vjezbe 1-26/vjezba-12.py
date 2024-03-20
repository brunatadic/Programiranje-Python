#python igra - pogodi broj
import random

tajnibroj = random.randint(1,20)
while True:
    pogodi = int(input("Pogodi broj između 1 i 20"))

    if pogodi == tajnibroj:
        print("Bravo pogodio si traženi broj")
        break
    else:
        print("Pogriješio si, probaj onovno..")