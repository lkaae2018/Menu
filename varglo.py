import lemmelregning

x = "global"
y= 5

def lk():
    print(y)

def foo():
    global y
    print("x inside :", x)
    print("Y=", y)
    y = y+1


foo()
lk()
lemmelregning.regning()
print("x outside:", x)
print("y=",y)


