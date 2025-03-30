password=input("Enter a password")
def ispassword_valid(password):
    SpecialSym = ['$', '@', '#', '%']
    val=True
    if len(password)<6:
        print('Length of password should be atleast 6')
        val=False
    if len(password)>20:
        print('length is blw 8 to 20')
        val=False
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
    if not any(char.islower() for char in password):
        print('Password should have at least lower character ')
        val = False
    if not any(char.isupper() for char in password):
        print('Password should have at least one upper')
        val = False
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#%')
        val = False
    if val:
        return val
ispassword_valid(password)
if (ispassword_valid(password)):
    print('Password is Valid')
else:
    print('Password is Not Valid')



