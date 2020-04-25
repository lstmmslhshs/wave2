odd = ["1", "3", "5" ,"7" ] 
even = ["2", "4", "6" ,"8" ] 
l1 = ["a","c","e","g"]
l2 = ["b","d","f","h"]
s = input("please input a position :")
l = s[0]
n = s[1]
if l in l1 :
     if n in odd:
      print("black")
    
     elif n in even :
      print("white")
    
elif l in l2 :
     if n in odd:
      print("white")
    
     elif n in even :
      print("black")
else: 
 print("not valuable")
