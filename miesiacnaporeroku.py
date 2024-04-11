print("Podaj aktualny miesiac w liczbe")
x = int(input())
if x in range(3,4):
    print("Wiosna")
elif x in range(5,9):
    print("Lato")
elif x in range(10,11):
    print("Jesien")
elif x in range(12):
    print("Zima")
elif x in range(1):
    print("Zima")
elif x in range(2):
    print("Zima")
else:
    print("Podaj prawdziwy miesiac")

