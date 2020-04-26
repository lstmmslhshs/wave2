import math

a = float(input("input a: "))
b = float(input("input b: "))
c = float(input("input c: "))
z = b ** 2 - 4*a*c
if a == 0:
    print("not valuable")
else:
    if z > 0:
        print("there are two possible answers")
        an = (-b + math.sqrt(z))/2*a 
        aw = (-b - math.sqrt(z))/2*a 
        print(an)
        print(aw)
    elif z == 0:
        print("there is one possible answer")
        an = (-b)/2*a 
    elif z<0:
        print("there is no possible answer")