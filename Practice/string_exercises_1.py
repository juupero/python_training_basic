# 1. from ’bark’ create: ’b’ , ’a’ , ’r’ , ’k’ from ’park’ create: ’p’ , ’a’ , ’r’ , ’k’
str1 = "bark"
print(str1[0], str1[1], str1[2], str1[3])
str1 = "park"
print(str1[0], str1[1], str1[2], str1[3])

# 2. from ’pin’ create: ’pi’,’in’
s2 = "pin"
print(s2[:2])
print(s2[1:])

# 3. from ’abracadabra’ create:’abra’,’cadabra’
s3 = "abracadabra"
print(s3[:s3.index("c")], s3[s3.index("c"):])

# 4. from ’four’ create: 4
s4 = "four"
print(len(s4))

# 5. from ’viisi’ create: 5
s5 = "viisi"
print(len(s5))

# 6. from ’breathe’ create: ’breath’
s6 = "breathe"
print(s6.rstrip("e"))

# 7. from ’weight’ create: ’weigh’
s7 = "weight"
print(s7[0:s7.index("t")])


# 8. from ’weight’ create: ’eight’
print(s7.lstrip("w"))
print(s7[1:])


# 9. from ’hearth’ create: ’earth’
s9 = "hearth"
print(s9[1:])

# 10. from ’intermediate’ create: ’media’
s10 = "intermediate"
print(s10.lstrip("inter").rstrip("te"))

# 11. from ’premediates’ create: ’media’
s11 = "premediates"
print(s11[s11.find("media"):s11.index("t")])


# 12. from ’grand’ and ’ma’ create: ’grandma’
s12 =  "grand"
s12a = "ma"
print(s12+s12a)

# 13. from ’grand’ and ’dad’ create: ’grandad’
s13 = "dad"
print(s12+s13)

# 14. from ’grand’ and ’ma’ create: ’grandgrandgrandma’
print(s12*3+s12a)

# 15. from ’grand’ and ’dad’ create: ’grandgrandgrandgrandad’
print(s12*4+s13)

# 16. from 3 create: ’3’
num = 3
print("'%d'" % num)

# 17. from 4 create: ’444’
num1 = "4"*3
print("'%s'" % num1)

# 18. from ’Another bad example, what a good day’ create: ’Another good example, what a bad day'
str18 = "Another bad example, what a good day"
print(str18.replace('good', 'bad').replace('bad','good',1))
