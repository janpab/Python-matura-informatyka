def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    p = 0
    w = 1
    for i in range(n-1):
        p_old = p
        p=w
        w = p_old  +w
    return w
def from_dec_to_bin(num):

    wynik = ""
    while num != 0:
        wynik = str(num%2)+wynik
        num = num//2
    return wynik
def is_prime(number):
    if number<=1:
        return False

    if number ==2:
        return True
    
    if number % 2 ==0:
        return False
    
    for i in range(3, (number//2)+1):
        if number % i == 0:
            return False
    return True
def zadanie1():
    print(fib(10))
    print(fib(20))
    print(fib(30))
    print(fib(40))
def zadanie2():
    for i in range(1,41):
        if is_prime(fib(i)):
            print(i,".",fib(i))
def zadanie3():
    ostatni = from_dec_to_bin(fib(40))
    for i in range(1,41):
        liczba_bin = from_dec_to_bin(fib(i))
        if len(liczba_bin)< len(ostatni):
            brak_bity=len(ostatni)-len(liczba_bin)
            for k in range(brak_bity):
                liczba_bin = "0"+liczba_bin
        print(liczba_bin)
def zadanie4():
    ostatni = from_dec_to_bin(fib(40))
    for i in range(1,40):
        liczba_bin = from_dec_to_bin(fib(i))
        licznik = 0
        for i in range(len(liczba_bin)):
            if liczba_bin[i] == "1":
                licznik +=1
        if licznik == 6:
            print(liczba_bin)
print("Zadanie 1 ")
zadanie1()
print("Zadanie 2 ")
zadanie2()
print("Zadanie 3 ")
zadanie3()
print("Zadanie 4 ")
zadanie4()