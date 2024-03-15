n = int(input("Podaj wartość liczby naturalnej n -"))
a = n/2
b = int(n/2)

if a!=b:
    s = b+1
j = 1
  
for i in range (1,n+1):
    print('*'*j)
    if s >i:
        j=j+1
    else:
        j=j-1
    
