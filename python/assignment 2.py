# Armstrng strong number

# 1 5 3 =1*1*1 +5*5*5 + 3*3*3 =153

num=int(input("Enter the number:"))
sum =0

temp = num
while temp > 0:
        digit =temp %10
        
        sum += digit **3

        temp //=10

if num == sum:
    print(num,"Ihis is armstrong number:")

else:
    print(num,"This is not armstrong number:")
