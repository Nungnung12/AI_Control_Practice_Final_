# var = 50


# if(var > 75):
#     print("Var 는 75 초과입니다.")    
# elif (var <= 75 and var >25):
#     print("Var 는 25 초과 75 이하입니다.")
# elif (var <= 25):
#     print("Var 25 이하입니다.")

#!/usr/bin/python3


def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return


printme("This is first call to the user defined function!")
printme("Again second call to the same function")

def changem(mylist):
    print("Values inside the function before change: ", mylist)
    mylist[2] = 50
    print("Values inside the function after change: ", mylist)
    return

mylist = [10,20,30]
changem(mylist)
print("Values outside the function: ", mylist)

def changeme(mylist):
    mylist = [1,2,3,4]
    print("Values inside the function: ", mylist)
    return

mylist = [10,20,30]
changeme(mylist)
print("Values outside the function: ", mylist)

def printme(str):
    print(str)
    return

printme()

def printme(str):
    print(str)
    return

printme( str = "My String")

def printinfo(name,age):
    print("Name: ",name)
    print("Age ",age)
    return

printinfo(age=50, name="miki")

def printinfo(name, age = 25):
    print("Name: ", name)
    print("Age ", age)
    return

printinfo(age = 50, name = "IDW")
printinfo( name = "IDWoo")

def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(70, 60, 50)