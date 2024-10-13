import math
def cal(r):
    area=math.pi*r**2
    circum=2*math.pi*r
    return area,circum
    #function of
r=5
c=cal(r)
a,b=cal(r)
print("area of circle:",c[0])
print("area of Circumference:",round(c[1],3))