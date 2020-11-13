
""" (1) Fahrenheit to Celcius conversion"""
"""Way 1 : Fahrenheit input inside main, parameter needs to be passed"""
def tempconversion(fahren):
    """This function takes fahren as parameter and converts fahrenheit reading to celcius"""
    c=(fahren-32)*(100/180)
    print("The celcius reading is : ",c)

def main():
    f=float(input("Enter Fahrenheit reading: "))
    tempconversion(f)
    """Function is called with argument f"""

if __name__=="__main__":
    main()

print()
"""Way 2 : Fahrenheit input inside function, so parameter not passed"""

##def tempconversion():
##    f=float(input("Enter Fahrenheit reading: "))
##    c=(f-32)*(100/180)
##    print("The celcius reading is : ",c)
##
##def main():
##    tempconversion()
##
##if __name__=="__main__":
##    main()


""" (2) Seconds to Mins/Seconds conversion"""
def timeconversion(x):
    """This function converts user input time in seconds to minutes and seconds"""
    y=x//60
    z=x%60
    print("After calcuation=>")
    print("Mins: ",y)
    print("Secs: ",z)

def main():
    t=int(input("Enter time in seconds : "))
    timeconversion(t)

if __name__=="__main__":
    main()

print()
""" (3) List"""

"""Way 1 : list defined inside the main"""
def listlength(i):
    """This function prints the length of list"""
    print("The length of the list is:",len(i))
def firstelement(i):
    """This function prints the first element of list""" 
    print("The first element of  the list is :",i[0])
def fourthelement(i):
    """This function prints the fourth element of list"""
    print("The fourth element of  the list is :",i[3])

def main():
    intro=["Jon","Doe",44,"Nepal"]
    listlength(intro)
    firstelement(intro)
    fourthelement(intro)

if __name__=="__main__":
    main()

print()
"""Way 2 : list defined globally"""

##intro=["Jon","Doe",44,"Nepal"]
##def listlength():
##    print("The length of the list is:",len(intro))
##def firstelement():
##    print("The first element of  the list is :",intro[0])
##def fourthelement():
##    print("The fourth element of  the list is :",intro[3])
##
##def main():
##    listlength()
##    firstelement()
##    fourthelement()
##
##if __name__=="__main__":
##    main()


""" (4) List with methods"""
position=["ST","LW","CMF","DMF","DF","GK"]
print("The list is:",position)
def popelement():
    print("The popped element is :",position.pop(1))
    """The element at index 1 i.e. "LW" is popped out"""
def insertelement():
    position.insert(1,"RW")
    """The element "RW" is inserted to list at index 1"""
    print("The list after insertion is :",position)
def removeelement():
    position.remove("DMF")
    """The element "DMF" is removed from list"""
    print("The list after removal is :",position)

def main():
    popelement()
    insertelement()
    removeelement()

if __name__=="__main__":
    main()
    
print()













