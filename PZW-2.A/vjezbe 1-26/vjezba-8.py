#if naredba
x=267

if x > 100:
    print("x je veći od 100")



a = 99

if a == 99:
    print("a je zaista 99!")

    a = 99

if a != 99:
    print("a je zaista 99!")
    a = 99 #tu se ništa ne mjenja u kodu jer je laž

a = 100
if a != 99:
    print("a nije 99!")


#if else naredba

b = 100

if b >= 99:
    print("b je veće ili jednako 100!")
else:
    print("b je manje od 100!")



#if elif naredba

c = 100

if c > 100:
    print("c je veće od 100")
elif c == 100:
    print("c je jednako 100")
else:
    print("c je manje od 100")

