s=input("enter a string")
def Valid_email(s):
    if s[-10:] == "@gmail.com":
        return "its a valid email"
    elif s[-12:] == "@Outlook.com":
        return "its a valid email"
    elif s[-10:] == "@yahoo.com":
        return "its a valid email"
    else:
        return "It not valid Email"
print(Valid_email(s))