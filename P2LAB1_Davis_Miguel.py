# Miguel Davis
# 10/13/2024
# P2LAB1
# Circle Calculator

import math

rad = float(input("What is the radius of the circle? "))
diameter = 2 * rad
circumference = 2 * math.pi * rad
area = math.pi * rad ** 2

print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")

