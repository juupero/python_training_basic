# 1. There are 5280 feet in a mile. Write a Python statement that calculates andprints the number of feet in 23 miles.
mile = 5280
feet_in_23 = mile * 23
print(feet_in_23)

# 2. Write a Python statement that calculates and prints the number of sec-onds in 10 hours, 35 minutes and 20 seconds.
sec = 1
min = 60*sec
hour = 60*min
print("number of seconds:" + str(10*hour+35*min+20))

# 3. The perimeter of a rectangle is 2w+ 2h, wherewandhare the lengths of its sides. Write a Python statement that calculates and prints the length in centimeters of the perimeter of a rectangle with sides of length 10 and 15centimeters.
w = 15
l = 10
result = str(2*w + 2*l)
print("Permiter of the rectanble is " + result)

# 4. The area of a rectangle is wh, wherewandhare the lengths of its sides.Note that the multiplication operation is not shown explicitly in this formula.This is standard practice in mathematics, but not in programming. Write aPython statement that calculates and prints the area in square centimeters ofa rectangle with sides of length 10 and 25 centimeters.
w = 10
h = 25
Area = str(w*h)
print("Area of the rectangle is " + Area)

# 5. The circumference of a circle is 2πr where r is the radius of the circle.Write a Python statement that calculates and prints the circumference in cen-timeters of a circle whose radius is 8 centimeters. Assume that the constant π= 3.14.
pi = 3.14
r = 8
circumference = 2*pi*r
print("Circumference of the circle is " + format(circumference))

# 6. The area of a circle is πr2 where r is the radius of the circle. Write aPython statement that calculates and prints the area in square centimeters ofa circle whose radius is 8 centimeters. Assume that the constant π= 3.14.
area_of_circle = pi*r**2
print("Area of the circle is {}" .format(area_of_circle))

# 7. Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest for y years isp(1 + 0.01ry).  Write a Pythonstatement that calculates and prints the value of 1000 dollars compounded at 7 percent interest for 10 years.
rate = 7
years = 10
p = 1000
interest = p*(1 + 0.01*rate*years)
print("Interest is %.2f" % interest)

# 8. Write a single Python statement that combines the three strings ”Myname is”, ”John” and ”Smith” (plus a couple of other small strings) into onelarger string ”My name is John Smith.” and prints the result.
a= "My"
b = "name is"
c = "John"
d = "Smith"
print("Complete String is '{0} {1} {2} {3}'" .format(a, b, c, d))


# 9. Write a Python expression that combines the string ”John Smith is 40years old.” from the string ”John Smith” and the number 40 and then prints the result (Hint: Use the function str to convert the number into a string.)
print("Another complete string is '{0} {1} " .format(c, d) + "is " + str(40) + " years old.'")

# 10. The distance between two points (x0,y0) and (x1,y1) is √((x0−x1)2 + (y0−y1)2) Write a Python statement that calculates and prints the distance between thepoints (2,2) and (5,6).1
x0 = 2
x1 = 1
y0 = 5
y1 = 6
distance = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
print("Distance between two points is %.2f" % distance)
