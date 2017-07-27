x=map(int,raw_input("enter list of values").split())
print x

def add(x):
    y=0
    for i in x:
        y+=int(i)
    return y
def sub(x):
    if len(x)==2:
        return x[0]-x[1]
    else:
        print "subraction cannot be performed",
    x = map(int, raw_input("enter list of values").split())
    return sub(x)
def mul(x):
    p=1
    for i in x:
        p*=i
    return p
def div(x):
    if len(x)==2:
        try:
            return float(x[0]/x[1])
        except:
            return ZeroDivisionError
    else:
        return "Divison cannot be performed"
def fact(x):
    if len(x)==1:
        a=1
        for i in range(1,int(x[0])+1):
            a*=i
            i=i-1
        return a
    else:
        return "Factorial cannot be performed,enter only one value"
def avg(x):
    return float(add(x)/len(x))
def pow(x):

    if len(x)==2:
        return x[0]**x[1]
    return "please enter valid inputs"




def repeat(x):
    calculation=raw_input('''
    Enter the Arithmatic Calculation you want to perform:
                               + for addition
                               - for subraction
                               * for multiplication
                               / for division
                               @ for factorial
                               $ for average
                               ^ for power
                               ''')
    print x

    if calculation == '+':
        print("sum of all numbers is: ", add(x))

    elif calculation == '-':
        print("subraction of numbers is: ", sub(x))


    elif calculation == '*':
        print("multiplicaiton of numbers is: ", mul(x))


    elif calculation == '/':
        print("Division of numbers is: ", div(x))


    elif calculation == '@':
        print("factorial of numbers is: ", fact(x))


    elif calculation == '$':
        print("average of numbers is: ", avg(x))


    elif calculation == '^':
        print("power of two numbers is: ", pow(x))

    a = raw_input("Do wish to Continue Y or N:")
    if a == "Y":
        print repeat(x)

    elif a == "N":
        print("No more operations to perform")
    else:
        repeat(x)


print repeat(x)





