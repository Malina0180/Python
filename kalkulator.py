import math
a = int(input("Podaj liczbe a -"))
b = int(input("Podaj liczbe b -"))

suma = a+b
roznica = a-b
iloczyn = a*b
iloraz = a/b
pierwiastekSumy = math.sqrt(a+b) 
potega1 = a^b
potega2 = b^a

print("Dodawanie",suma,",odejmowanie",roznica,",mnożenie",iloczyn,",dzielenie",iloraz,",pierwiastkowanie",pierwiastekSumy,",Potęga a^b",potega1,",Potęga b^a",potega2)