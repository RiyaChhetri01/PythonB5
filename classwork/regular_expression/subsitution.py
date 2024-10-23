#replacing the word
import re
pattern = r"cat"

text = "The cat sat on the mat."
result = re.sub(pattern, "dog", text)
print("After substitution:", result)

#write a function that takes a string with email and return it with bold tag
#we have one text string we have to bold that particular word whenever it will occur
test="this is my email riyachhetri1234@hmail.com"

def bold_word(test):
    pattern_email = r"[\w.]+@[\S]*"
    match= re.search(pattern_email,test)
    replace =f"<b>{match.group()}<b>"
    replaced_string=re.sub(pattern_email,replace,test)
    return replaced_string

replaced_string = bold_word(test)

print("after replacement")
print(f"\n\n{replaced_string}\n\n")

#compiling regular expression 
pattern = re.compile(r"\d+")

text = "123 apples, 456 bananas"
matches = pattern.findall(text)
print("Matches:", matches)




#The re.split() function used the pattern r"\d.\s" to split the string 
# at each point where it found a number followed by a dot and space, l
# eaving only the portions of text that follow each pattern in the resulting list.
test="""
1.riya 
2.hxyxd 
3.manpreet"""
pattern=r"\d.\s"
splittedList = re.split(pattern,test)
print(splittedList)

