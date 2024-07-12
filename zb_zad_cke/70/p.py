def luk_1(x):
    x4 = x*x*x*x
    x2 = x*x
    wynik = (x4/500)-(x2/200)-(3/250)
    return wynik
def luk_2(x):
    x3=x*x*x
    wynik = (-x3/30)+(x/20)+(1/6)
    return wynik

print(luk_2(2))
print(luk_1(2))




def zad1():
    dc = 19+(16/125)
    ab = 32+(2/3)
    da = 2
    cb = da 
    print(luk_1(dc))
    print(luk_2(ab))
zad1()