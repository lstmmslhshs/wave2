import random
n = random.randint(0,37)
red = [1,2,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green = [0,37] 
if n in red: 
     if n <19 and n>0:
         if n % 2 == 0 :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay red")
           print("Pay even")
           print("Pay 1 to 18")
         else :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay red")
           print("Pay odd")
           print("Pay 1 to 18")
     elif n <= 36 and n > 18:
         if n % 2 == 0 :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay red")
           print("Pay even")
           print("Pay 19 to 36")
         else :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay red")
           print("Pay odd")
           print("Pay 19 to 36")
elif n in black:
     if n <19 and n>0:
         if n % 2 == 0 :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay black")
           print("Pay even")
           print("Pay 1 to 18")
         else :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay black")
           print("Pay odd")
           print("Pay 1 to 18")
     elif n <= 36 and n > 18:
         if n % 2 == 0 :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay black")
           print("Pay even")
           print("Pay 19 to 36")
         else :
           print("The spin resulted in ",n,"...",sep='')
           print("Pay",n)
           print("Pay black")
           print("Pay odd")
           print("Pay 19 to 36")
elif n in green:
     if n == 0:
         print ("the spin result in 0...")
         print ("Pay 0")
     elif n == 37:
         print ("the spin result in 00...")
         print ("Pay 00")