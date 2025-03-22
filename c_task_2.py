tem_val=float(input('enetr a Temperature value'))
unit=input("enter a unit")
def tem_conv(tem_val,unit):
    if unit.lower()=="celsius" or ""C:
        converted_value = round((tem_val * 9 / 5) + 32,2)
        conv_unit="Farenheit"
    elif unit.lower=="Farenheit" or "F":
        converted_value=(tem_val-32)*5/9
        conv_unit="celsius"
    else:
        print("Enter a valid Unit blw Celsius or Farenheit")
    return f'{tem_val},{unit} is equal to {converted_value},{conv_unit}'
print(tem_conv(tem_val,unit))