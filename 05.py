def triangle():
    leng1= float(input("what is the Length of the First side of Triangle?"))
    leng2 = float(input("what is the Length of the Second side of Triangle?"))
    leng3 = float(input("what is the Length of the Third side of Triangle?"))
    perimeter = leng1 + leng2 + leng3
    print (f"Here is the Perimeter of your Triangle:{perimeter}")



if __name__ == '__main__':
    triangle()