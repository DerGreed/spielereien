def Addition(*Summanden):
    Summe = 0
    for Summand in Summanden:
        Summe += Summand
    return Summe
#_____________________________________________

def Addition_rekursiv(*Summanden):
    if len(Summanden) > 0:
        return Summanden[0] + Addition_rekursiv(*Summanden[1:])
    else:
        return 0

print(Addition_rekursiv(1, 2, 3, 10))

def Multiplikation(*Faktoren):
    Produkt = 1
    for Faktor in Faktoren:
        Produkt *= Faktor
    return Produkt
#_____________________________________________

def Division(Dividend, *Divisoren):
    Quotient = Dividend
    for Divisor in Divisoren:
        Quotient /= Divisor
    return Quotient
#_____________________________________________

def Subtraktion(Minuend, *Subtrahenden):
    Differenz = Minuend
    for Subtrahend in Subtrahenden:
        Differenz -= Subtrahend
    return Differenz
#_____________________________________________

def Durchschnitt(*Noten):
    return Addition(*Noten) / len(Noten)


note1, note2, note3 = 5, 2, 1

liste = [note1, note2, note3, 1, 1, 1]

print("Noten:", str(liste)[1:-1])
print('Durchschnitt =', Durchschnitt(*liste))


a, b = 12, 5
liste = [180, a, b, 1] 

Funktionen = [Addition, Subtraktion, Multiplikation, Division]
print("Zahlen:", str(liste)[1:-1])
for f in Funktionen:
    print(f.__name__ + ":", f(*liste))

flaeche = lambda a,b,c: (s := (a + b + c) / 2, (s * (s - a) * (s - b) * (s - c)) ** 0.5)[1]
print(flaeche(3, 4, 5))