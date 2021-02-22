myUniqueList =[]
myLeftovers =[]


def list(x):
 if x in myUniqueList:
  print(False)
  myLeftovers.append(x)
 
 else:
  print(True)
  myUniqueList.append(x)
 
 
list(10)
list(20)
list(30)
list(40)
list(50)
list(10)
list(20)
list("List Example")
list(2.0)
list(20)
print(myUniqueList)
print(myLeftovers)