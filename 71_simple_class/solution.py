class inputOutString:
    def __init__(self):
        self.s = ''
    # method for getting string
    def inputString(self):
        self.s = input()
    #method for printing the string
    def printString(self):
        print(self.s.upper())

obj = inputOutString()
obj.inputString()
obj.printString()
    
        