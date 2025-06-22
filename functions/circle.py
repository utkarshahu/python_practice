import math

def circle(radius):
    area = math.pi*(radius**2)
    circumference = (2*math.pi)*radius  
    return (area,circumference)

Area,Circumference = circle(12)
print(f"Area {Area:.2f} , Circumference {Circumference:.2f}")
