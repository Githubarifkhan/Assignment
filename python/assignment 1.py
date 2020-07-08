num1 =float(input("enter the fist element:"))
num2 =float(input("enter the second element:"))

print("which mathematical operator do you want to enter:")
ch=input("these operator i want to allow +,-,/,*:")


result =0
if ch=='+':
    result =num1+num2

elif ch=='-':
    result =num1-num2

elif ch=='*':
    result =num1*num2

elif ch=='/':
    result =num1/num2

elif ch=='%':
    result =num1%num2

else:
    print("enter number is not possible:")

print(num1,num2,ch,":",result)
