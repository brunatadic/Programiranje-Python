def izracunajKorake(put, korak):
    return int(put / korak)

put= float(input("unesi duljinu puta (u metrima): "))
korak= float(input("unesi duljinu koraka(u metrima): "))

print(izracunajKorake(put, korak))