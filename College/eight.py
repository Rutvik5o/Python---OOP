'''
(9)=> Write a menu driven python program which performm the following:
->find area of circle
->Find area of triangle
->Find area of simple interest
'''

def mainmenu():

    print("1: Find area of circle")
    print("2: Find area of triangle")
    print("3: Find area of simple interest")
    print("4. Quit\n")

    selection = int(input("Enter your choice -> "))

    if selection == 1:

        radius=float(input("Enter radius of circle->"))

        area = 3.14*radius*radius

        print("\nArea of Circle -> %0.2f\n" %area)

        mainmenu()

    elif selection == 2:

        a = float(input("Enter length of first side1->"))

        b = float(input("Enter length of second side2->"))

        c = float(input("Enter length of third side3->"))

        s=(a+b+c)/2

        area = (s*(s-a)*(s-b)*(s-c))**0.5

        print("\nArea of Triangle -> %02.f\n" %area)

        mainmenu()

    elif selection == 3:

        p = float(input("Enter the principle amount->"))

        r = float(input("Enter rate of interest->"))

        t = float(input("Enter the time in year->"))

        si = (p*r*t)/100

        print("\nSimple Interest =>",si)

        mainmenu()

    elif selection == 4:

        exit

    else:

        print("\nInvalid Choice\n")

        mainmenu()


mainmenu()
        










