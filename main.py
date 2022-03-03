# Regular Expressions are used to do advanced "Find (and Replace)" in strings
# "pattern matching" is at its core
import re

testString = "digital physics is an interesting topic"

# ^ is used to search for a pattern at the start of a string
# This is Test Pattern: https://www.youtube.com/watch?v=HcLDzcmkSqI
testPattern = "^digital"

# search for pattern in string
# returns a match object
# span is a tuple of where the pattern was found
results = re.search(testPattern,testString)
print("search results:", results)

# $ is used to search a pattern at the end of a string
# returns None because the pattern is not at the end of the test string
p2 = "digital$"
results2 = re.search(p2,testString)
print("search results:", results2)

# "Quantifiers" ? + *

# ? finds 0 or 1 occurrence of the preceding character
st = "color"
st2 = "colour"

p3 = "colou?r"
print("search results:", re.search(p3,st))
print("search results:", re.search(p3,st2))

# + finds 1 or more occurrences of the preceding character
p4 = "colou+r"
print("search results:", re.search(p4,st))
print("search results:", re.search(p4,st2))
print(re.search(p4,"colouuuuur"))

# "Metacharacters" - .
# [] is a way to specify a set of possible values for a character, like [0145] for matching on 0, 1, 4, or 5
# - is a range like [a-n] or [1-9]
# ^ used inside [] means Not, like [^a-n] would match on o, p, q...
# don't confuse ^ when it is used outside for searching at the beginning of a string

# find first occurrence of two successive characters corresponding to the numbers '00' to '59'
p5 = "[0-5][0-9]"
print(re.search(p5,"0"))
print(re.search(p5,"00"))
print(re.search(p5,"44"))
print(re.search(p5,"59"))
print(re.search(p5,"60"))
print(re.search(p5,"4453"))

# "find all" returns a list
# note that 44 and 53 are found but 45 is not; it seems like a character can only be found in one instance
print("find all patterns that match, not just the first:", re.findall(p5, "4453"))

p6 = "[a-z]"
p7 = "[a-zA-Z]"
print("find all lower case letters:", re.findall(p6, "Digital"))
print("find all letters:", re.findall(p7, "Digital"))

# Special Sequences
# \d is the same as [0-9]
# \w is the same as [0-9a-zA-Z_] (Question: would using commas hurt the syntax?)
p8 = '\d'
p9 = '\w'

print("find all numbers:", re.findall(p8, "Digital Physics 2"))
print("find all letters and numbers and underscores:", re.findall(p9, "Digital Physics_2!"))

print()
print("*****interactive portion*****")
print()

# Password Validation example:
# Criteria:
# At least 8 characters
# Allowed characters:
# uppercase letters A-Z
# lowercase letters a-z
# numbers 0-9
# special characters @#$%*&+=
# Note regarding {}: {8,15} means between 8 and 15 characters
p10 = "[A-Za-z0-9@#$%*&+=]{8,}"
pwd = input("enter a test password of at least 8 characters:")

# "full match" returns an object iff the full string matches the pattern
# note: there is a flag parameter that was ignored here
if re.fullmatch(p10, pwd):
    print("your password matched the RegEx pattern, and therefore was good enough to pass the easy test")
else:
    print("your password did not match the RegEx pattern, and therefore was not sufficient for the easy test")

# Password Validation example2:
# Criteria:
# 8-15 characters in length
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# only alphanumeric

# assertions test whether a string meets some criteria
# a look ahead assertion looks to see if a criteria is met after a certain point in the string
# (?= is the start of a positive lookahead group
# (?=.* means is there a match of 0 or more (*) of the preceding element ., where . is any character but a line break
# should we use ^ at the beginning and $ at the end? what is the role of . before the {}?
# when should we use raw strings r""?
p11 = "(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}"
pwd2 = input("enter a test password with upper & lowercase, numbers:")

if re.fullmatch(p11, pwd2):
    print("your password matched the RegEx pattern, and therefore was good enough to pass the harder test")
else:
    print("your password did not match the RegEx pattern, and therefore was not sufficient for the harder test")

# User Input Validation examples

print()
print("*****end of interactive portion*****")
print()

print("Validate Time Inputs:")
# Create a time format checker that verifies if the user input should be further processed by a backend application
test_list = ['18:29', '23:15', '123', 'ab:de', '18:299', '99:99']
p12 = "[0-9]{2}:[0-9]{2}"

print([re.fullmatch(p12,string) for string in test_list])

# Create a better pattern that will work for matching only input times of 00:00 and 23:59
# | is OR so include () around it's arguments
p13 = "([01][0-9]|2[0-3]):[0-5][0-9]"

print([re.fullmatch(p13,string) for string in test_list])

print("Validate Email Inputs:")
test_list_emails = ['philadelphiaphilms@gmail.com', 'alice@bob.org', 'info_99.us@yahoo.com', 'alice@', "bob@gmail.comm"]
# \w alphanumeric
# | or
# + one or more of the preceding elements
# different pattern variations to test:
# p14 = "^(\w|\.|\_)+[@]\w+[.]\w{2,3}$"
# p14 = "^(\w|\.|\_)+@\w+.\w{2,3}$"
p14 = "^[\w._]+@\w+.\w{2,3}$"

print([re.fullmatch(p14,string) for string in test_list_emails])

print("Validate User Names:")
test_list_names = ["alice", "bob", "eve_eve", "eve2"]
p15 = "^[A-Za-z_.]+$"

print([re.fullmatch(p15,string) for string in test_list_names])

print("? and Non-Greedy Returns:")
# ? is the "Option" regex sometimes used to denote 0 or 1 occurrences like in the "u?" in "color/colour" pattern example
# ? can be used in combination with other special characters
# *? can get the non-greedy return if we want the 0 occurrence case (not the 'or more' case) of the element before the *
test_sentence = "peter piper picked a peck of pickled peppers."
# this pattern corresponds to strings that start with p have an e in the middle and then have an r at the end (greedy return length)
print(re.findall("p.*e.*r", test_sentence))
# this pattern stops when it matches and then starts searching the rest of the string (remember how 45 didn't show up before?)
print(re.findall("p.*?e.*?r", test_sentence))

# a pattern that finds strings starting with "digital", having at most 30 characters in between, and ends with "physics"
test_phrase = "For $10, any digital toy model physics lover can purchase the movie, or for $2.99 you can rent it. $3.14159 test."
p16 = "digital(.{1,30})physics"
print(re.match(p16, test_phrase))

# a pattern that will find all references to dollars $ with optional decimal amounts
# \$ means the actual character $, not the special character $; similarly, \. means the actual character ., not the special operator
# clean-up from returned list afterwards
p17 = "(\$[0-9]+(\.[0-9]*)?)"
print(re.findall(p17, test_phrase))

print("Find and Replace:")
# ?! is a Negative lookahead
# Find and Replace Digital Physics w/ DP unless it is in quotes
text = """
Douglas Hofstadter once wrote about the difference between objects and their names.
I think he tried to emphasize that there is a difference between, say, the science of Digital Physics 
and the linguistic reference/pointer to 'Digital Physics'... Or to take a more physical example, the difference
between the city of brotherly love (and all of what constitutes it) and a mere reference to it in the term "Philadelphia"
... or something along those lines. 
It reminded me of "real" numbers in mathematics and how most of them can't even be properly referenced or summarized."""
p18 = "Digital Physics(?!')"
print(re.sub(p18, "DP", text))

# the +? returns the non-greedy 1 case (and not the "or more" case) associated with +
p18 = "From:.+?@"
p19 = "From:.+@"
test_string2 = "From: alice@yahoo.com, bob@gmail.com, shirley"
print(re.findall(p18, test_string2))
print(re.findall(p19, test_string2))