myDict = {"brand": "ford", "model": "mustang", "year": "2017"}
# dictionary are ordered or unordered depending upon version of python
# changeable and don't allow for duplicates
# print(myDict["brand"])
#   We access items using particular key and key can't be same
# temp = myDict.keys()
# myDict["tyres"] = "white wall"
# print(myDict)
# tempVal = myDict.values()
# print(tempVal)
myDict.update({"year": "2019"})
myDict.pop("brand")
print(myDict)
for x in myDict.keys():
    print(x)
