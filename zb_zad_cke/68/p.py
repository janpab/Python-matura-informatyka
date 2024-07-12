def is_anagram(a,b):
    if len(a) == len(b):
        a = sorted(a)
        b = sorted(b)
        if a == b:
            return True
    else:
        return False

def zadanie1():
    dane = []
    licznik = 0
    with open("C:/Users/Jan/Desktop/KOREPETYCJE/KOREPETYCJE/68/dane_napisy.txt") as f:
        dane = f.readlines()
    for i in range(1000):
        para = dane[i].strip()
        para = para.split()
        p1 = para[0]
        p2 = para[1]
        if p1 == p2:
            licznik +=1
    print(licznik)

def zadanie2():
    dane = []
    licznik = 0
    with open("C:/Users/Jan/Desktop/KOREPETYCJE/KOREPETYCJE/68/dane_napisy.txt") as f:
        dane = f.readlines()
    for i in range(1000):
        para = dane[i].strip()
        para = para.split()
        p1 = para[0]
        p2 = para[1]
        if is_anagram(p1,p2):
            licznik+=1
    print(licznik)

def zadanie3():
    dane = []
    licznik = 0
    licznik2 = 0
    najwieksza = -9999999
    with open("C:/Users/Jan/Desktop/KOREPETYCJE/KOREPETYCJE/68/dane_napisy.txt") as f: 
        dane = f.readlines()
    for i in range(1000):
        para = dane[i].strip()
        para = para.split()
        p1 = sorted(para[0])
        p2 = sorted(para[1])
        p1s = ""
        p2s = ""
        for z in range(len(p1)):p1s += p1[z]
        for x in range(len(p2)):p2s += p2[x]
        for j in range(1000):
            para_t = dane[j].strip()
            para_t = para_t.split()
            p1_t = sorted(para_t[0])
            p2_t = sorted(para_t[1])
            p1s_t = ""
            p2s_t = ""
            for a in range(len(p1_t)):p1s_t += p1_t[a]
            for b in range(len(p2_t)):p2s_t += p2_t[b]
            if p1s == p1s_t:
                licznik+=1
            if p1s == p2s_t:
                licznik+=1
        for k in range(1000):
            para_t = dane[k].strip()
            para_t = para_t.split()
            p1_t = sorted(para_t[0])
            p2_t = sorted(para_t[1])
            p1s_t = ""
            p2s_t = ""
            for c in range(len(p1_t)):p1s_t += p1_t[c]
            for d in range(len(p2_t)):p2s_t += p2_t[d]
            if p2s == p1s_t:
                licznik2+=1
            if p2s == p2s_t:
                licznik2+=1
        licznik-=1
        licznik2-=1
        if licznik>najwieksza:
            print("p1s: ",p1s,licznik,najwieksza)
            najwieksza=licznik
            licznik=0
        if licznik2>najwieksza:
            print("p2s: ",p2s,licznik,najwieksza)
            najwieksza=licznik2
            licznik2=0
    print(najwieksza)



        
zadanie1()
zadanie2()
zadanie3()