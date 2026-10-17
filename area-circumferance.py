import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
areainteger=int(area)
print(f"Circumference of the circle: {circumference:.2f}")
print(f"Area of the circle: {area:.2f}")
print(f"Integer part of the area: {areainteger}")
