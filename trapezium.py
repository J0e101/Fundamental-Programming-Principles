# A program to return the area of a trapezium
#A=(0.5h (a + b))
print("TRAPEZIUM")
height = float(input("Enter height of figure in meters: "))
a = float(input("Enter side a of figure in meters: "))
b = float(input("Enter side b of figure in meters:"))

Area = 0.5 * height * (a + b)

print("Area of the trapezium is", Area, "meters")