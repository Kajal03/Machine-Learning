import sys

def printData():
    print(sys.argv)

def printSum():
    print("Printing sum : ",end=" ")
    print(int(sys.argv[1]) + int(sys.argv[2]))
    
printData()
printSum()
print("Printing sys version : {}".format(sys.version))

#interpreter will search for packages in these paths
print("Printing sys path : {} ".format(sys.path))

#print("Printing maxint : {}".format(sys.maxint))

print("Printing maxsize : {}".format(sys.maxsize))

print("Printing stdin : {}".format(sys.stdin))
print("Printing stdout : {}".format(sys.stdout))
