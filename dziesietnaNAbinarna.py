a = int(input())
r = ""
while a:
    r=r+str(a%2)
    a = int(a/2)
print(r[::-1])