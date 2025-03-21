def convertor():
    fahrenheit = float(input("Enter the temperature in Fahrenheit:"))
    ceslius = (fahrenheit - 32) * 5.0/9.0
    print (f"the temperature in celsius is {ceslius}")


if __name__ =='__main__' :
    convertor()