def genre():
 print("Action")
 
def artist():
 print("Batman")

def year():
 print("2000")
 
genre()

artist()

year()

a="Hello, World!"

print(a[1:4])


print(a[:4])

print(a[1:])


c=100
d=400
if (c>d):
 print("C is greater than d")
else:
 print("C is not greater than d")


like = False

count=0

like=True
if(like == True):
 count=count+1
 print(count)
 like = False

Temp=20
Thermo=15
print(Thermo)

if Temp <=15:
 Thermo=Thermo-5
 print(Thermo)
 
if Temp >=20:
 Thermo=Thermo+5
 print(Thermo)


Time="Night"
Sleepy=True
Pajamas="Off"
if Time == "Day" and Sleepy == False:
 Pajamas="On"
elif Time == "Evening" and Sleepy ==True:
 Pajamas="On"
else:
 Pajamas="Off"
 
print(Pajamas)

a=10
b=20
c="30"

def compare(x,y,z):
 if x==10 and y==20 and z=="30":
  print(True)
 
 else:
  print(False)
 
compare(a,b,c)
