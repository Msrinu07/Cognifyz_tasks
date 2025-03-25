a=input("Enter a string")
def Check_palindrome(a):
    if a[::]==a[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
print(Check_palindrome(a))