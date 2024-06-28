'''
(9)Write a menu driven python program which perform the following:
->Find area of circle
->find area of triangle
->find area of sqaure & rectangle
->find simple interest

Exit.(Hint: use infinite while loop for menu)

'''


choice =0

while(choice!=5):

    print("1.Find area of circle")
    print("2.Find area of triangle")
    print("3.Area of square and rectangle")
    print("4.Find Simple interest")
    print("5.Exit")



    choice = int(input("Enter you choice=>"))

    if choice == 1:

        pi=3.14

        radius = float(input("Please enter the radius of a circle"))

        area = pi * radius * radius

        circumference = 2 * pi * radius

        print("Area of Circle => %.2f " %circumference)


    elif choice == 2:

        a=float(input("Enter first side->"))

        b=float(input("Enter second side->"))

        c=float(input("Enter third side"))


        #calculate the semi-perimeter


        s=(a+b+c)/2


        #calculate the area

        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

        print("The area of the triangle is %0.2f" %area)

    elif choice == 3:

        side= int(input("Enter side length of sqaure-> "))

        area_sqaure = side*side

        print("Area of square => ",area_sqaure)

        width=float(input("Please enter the width of a Rectangle->"))

        height=float(input("Please Enter the Height of a Rectangle->"))

        #calculate the area

        Area = width * height

        #calculate the perimeter

        perimeter = 2*(width+height)

        print("\nArea of Rectangle is : %.2f" %Area)

        print("\nPerimeter is: %.2f" %Area)

    elif choice == 4:

        p= int(input("Enter P->"))

        r=int(input("Enter R->"))

        n=int(input("Enter N->"))

        l=(p*r*n)/100

        print(l)

    elif choice == 5:

        exit()

    else:

        print("GoodBy")



