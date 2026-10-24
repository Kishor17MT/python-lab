num1=float(input("enter first number:"))
num2=float(input("enter second number;"))
print("addition=",num1+num2)
print("multipliaction=",num1*num2)
if num2!=0:
    print("division=",num1/num2)
    print("floordivision=",num1//num2)
    print("modulus=",num1%num2)
else:
    print("division,floor division and modulus are undefined for zero divisor")
print("exponentiation=",num1**num2)