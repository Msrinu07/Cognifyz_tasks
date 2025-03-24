a=int(input("Enter a number"))
b=int(input("Enter a number"))
operators=['+','-','*','/','%']
op=input("enter a operation you want")
#for x in operators:
def cal_operators(a,b,op):
    if op=='+':
        result=a+b
        return result
    elif op=='-':
        result=a-b
        return result
    elif op=='*':
        result=a*b
        return result
    elif op=='%':
        result=a%b
        return result
    elif op=='/':
        if b!=0:
            result=a/b
            return result
        else:
            return "Zero Division error"
    else:
        return "Please Enter a Valid operator in ['+','-','*','/','%']"

print(cal_operators(a,b,op))