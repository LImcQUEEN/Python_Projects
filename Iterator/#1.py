#myTuple = ("apple", "banana", "cherry")
#myIt = iter(myTuple)
#print(next(myIt))
#print(next(myIt))
#print(next(myIt))
myName = "muhammad"
#myIt = iter(myName)
#print(next(myIt))
#for x in myName:
    #print(x)
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = myNumbers()
myIter = iter(myClass)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
