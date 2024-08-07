"""overriding Example"""
class person:

    def move(self):
        print("person is moving")
class kid(person):
    def __init__(self):
        print("inherited")
    def move(self,kid):
        print("the kid is moving")
kid1 = kid()
kid1.move()

"""overloading Example"""
class sum1:
    def addnumbers(a = None, b = None, c = None):
        if a!=None and b!= None and c!= None:
            sum = a+b+c
            print(f"the sum  of three numbers is {sum}")
        elif a!=None and b!= None:
            sum = a+b
            print(f"the sum of the two numbers is {sum}")
sum1.addnumbers(4,5,7)