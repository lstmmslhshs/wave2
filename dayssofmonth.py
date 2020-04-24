thirtyone = ["Jan", "Mar", "May" ,"Jul" ,"Aug", "Oct","Dec"] 
thirty  = ["Apr","Jun","Sep","Nov"]

if str(input())in thirtyone :
    print("31 days")
    
elif str(input()) in thirty :
    print("30 days")
    
else : 
    print("28 or 29 days")