#  wap to Recursion factorial

def recur_fact(n):
 if n==1:
     return n
 else:
     return n*recur_fact(n-1)


num=float(input("Enter the number:"))
if num < 0 :
        print("Recur_fact does not consist")
elif num == 0:
          print("the fact of zero is 1")

else:
    print(recur_fact(num))
          
"The factorial of",num,"is",
