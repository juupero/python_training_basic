# 1. Find index of the first ’o’ in ’Anomalocaris’
str1 = "Anomalocaris"
print(str1.find('o'))

# 2. Find index of the first ’r’ in ’Anomalocaris’.
print(str1.index('r'))

# 3. Find index of the last ’on’ in ’Waging on the purple drone’
s3 = "Waging on the purple drone"
print(s3.rfind('on'))

# 4. Find index of the last ’z’ in ’Superficial’
s4 = "Superficial"
print(s4.index('z'))

# 5. Find index of first ’a’ in the second half of the sentence ’There truly is a dazzling bright world out there, waiting for us to explore.’
s5 = "There truly is a dazzling bright world out there, waiting for us to explore."
print(s5[len(s5)//2:].index('a'))

# 6. Find index of the last ’a’ in the first half of the sentence ’There truly is a dazzling bright world out there, waiting for us to explore.’
print(s5[:len(s5)//2].rindex('a'))

# 7. Create ’42’ from ’91342391’ (remove trailing and leading characters)
s7 = "91342391"
print(s7.lstrip('913').rstrip('391'))

# 8. Create ’Warning’ from ’–== Warning! ==–’
s8 = "-== Warning! ==-"
print(s8.lstrip('-== ').rstrip(' ==-'))

# 9. Create ’–== Error’ from ’–== Error! ==–’
s9 = "-== Error! ==-"
print(s9.rstrip("! ==-"))
print(s9[0:s9.index("!")])

# 10. Create ’Success! ==–’ from ’–== Success! ==–’
s10 = "-== Success! ==-"
print(s10.lstrip("-== "))

# 11. Replace all ’dog’ with ’cat’ in ’Changing your dog for a bird? Some dog-lover you are.’
s11 = "Changing your dog for a bird? Some dog-lover you are."
print(s11.replace('dog', 'cat'))

# 12. Replace the first ’o’ with ’a’ in ’Being bold has some uses.’
s12 = "Being bold has some uses"
print(s12.replace('o', 'a', 1))

# 13. Create ’–== ERROR! ==–’ from ’–== Error! ==–’
s13 = "-== Error ==-"
print(s13.upper())

# 14. Create ’Abraham Lincoln’ from ’abraham lincoln’
s14 = "abraham lincoln"
print(s14.capitalize())


# 15. Create ’readable’ from ’rEaDaBlE’
s15= "rEaDaBlE"
print(s15.lower())

# 16. Create ’First word is capitalized’ from ’first word is capitalized’
s16 = "first word is capitalized"
print(s16.capitalize())

# 17. How many ’o’ are there in ’a loooooooooooooooooooong word?’
s17 = "a loooooooooooooooooooong word?"
print(s17.count('o'))

# 18. How many zeros in godzillion? (Let godzillion be 100000000000000000000000000000000000000000)
s18 = "100000000000000000000000000000000000000000"
print(s18.count('0'))

# 19. How many ’n’ are there in the first half of the string ’Something out of nothing? I really doubt we can do it anytime soon..’
s19 = "Something out of nothing? I really doubt we can do it anytime soon.."
print(s19[:len(s19)//2].count('n'))

# 20. Replace all ’0’ except the first with ’9’ in godzillion (see definition above).
print(s18[:2] + s18[2:].replace('0', '9'))

# 21. From ’what,if,we,have,no,choice?....’ create ’What if we have no choice?’
s21 = "what,if,we,have,no,choice?...."
print(s21.replace(',', ' ').capitalize().replace('.', ''))
