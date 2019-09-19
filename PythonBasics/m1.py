
if __name__ == '__main__' :
    #what to do when this module is run directly
    print("M1 module is {}".format(__name__))

else:
    #what do to when this module is imported
    print("I am in M1 else block")