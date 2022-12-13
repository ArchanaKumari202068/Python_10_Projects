# define the functions needed : add,sub,mul,div
# print options to the users
# ask for values
# call the functions
# while loop to continue the program until the user want to exit


def add(a,b):
    ans = a+b
    print (str(a)+ "+"+str(b)+ " = "+ str(ans))
    # print (ans)
def sub(a,b):
    ans = a-b
    print (str(a)+ "-" + str(b)+ " = "+ str(ans))

def mul(a,b):
    ans = a*b
    print (str(a)+ "*" + str(b)+ " = "+ str(ans))

def div(a,b):
    ans = a/b
    print (str(a)+ "/" + str(b)+ " = "+ str(ans))    

while True :
    print ("A.addition")
    print ("B.subtraction")
    print("C.Multiplication")
    print ("D.Division")
    print ("E.Exit")

    choice = input('Enter Your Choice :')

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number:"))
        b = int (input("input second number: "))
        add(a,b)    
    elif choice == "b" or choice =="B ":
        print("Subtraction")
        a = int(input("input first number:"))
        b = int (input("input second number: "))
        sub(a,b)
    elif choice == "c" or choice =="C":
        print("Multiplication")
        a = int(input("input first number:"))
        b = int (input("input second number: "))
        mul(a,b)

    elif choice == "d" or choice =="D":
        print("Division")
        a = int(input("input first number:"))
        b = int (input("input second number: "))
        div(a,b)
    
    elif choice == "e" or choice =="E":
        print("Program ended")
        quit()