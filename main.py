# Ex1 - String 
# Enter text and display it one by one
text = input("Enter Text : ")
for i in range(len(text)):
    print(text[i])

# Ex2 - String
# Enter text and display number of letter
text = input("Enter Text : ")
for i in range(len(text)):
    print(i)

# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter
text = input("Enter Text : ")
result = "Yes"
for i in range(len(text)):
    if text[i] == text[i].lower():
        result = "No"
print(result)
    

# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)
text = input("Enter Text : ")
result = 0
letter = ""
for i in range(len(text)):
    if text[i] == " ":
        letter += ""
    else:
        letter += text[i]
        result += int(text[i])
print(letter)
print("Total :",result)

# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 
text = input("Enter Text : ")
result_all = 0
result_even = 0
letter_even = 0
letter_odd = 0
lastindex = len(text) - 1
letter_recvers = ""
for i in range(len(text)):
    letter_recvers += text[lastindex -i]
    result_all += int(text[i])
    if i % 2 == 0:
        letter_even += 1
        result_even += int(text[i])
    else:
        letter_odd += 1
print("letter even:", letter_even)
print("letter odd", letter_odd)
print("Total :",result)
print("Letter revers", letter_recvers)

# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"
number = int(input("Enter number: "))
if number % 2 == 1:
    print("Odd")
else:
    print("Even")

# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
isfound_number = False
while not isfound_number:
    number = int(input("Enter number : "))
    if number >= 10 and number <=20:
        print("Continue")
    else:
        isfound_number = True
print("Out of range")

# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8
text = "9394884039"
number_eight = 0
first_index_of_eight = 0
isfound = False
for i in range(len(text)):
    if text[i] == "8":
        number_eight += 1
        if text[i] == "8" and not isfound:
            first_index_of_eight = i
        isfound = True
print(number_eight)
print(first_index_of_eight)
    


# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"
text = "3 4 5 6"
no_space = ""
total_x_two = 0
for i in range(len(text)):
    if text[i] != " ":
        no_space += text[i] + " "
        total_x_two += int(text[i]) * 2
        print(total_x_two)
    else:
        no_space += ""
print(no_space)
    


# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
print("Please enter your number : ")
bigest_number = 0
smailest_number = 0
for i in range(5):
    number = int(input("Enter number : "))
    if bigest_number == 0 and smailest_number == 0:
        bigest_number = number
        smailest_number = number
    else:
        if number > bigest_number:
            bigest_number = number
        if number < smailest_number:
            smailest_number = number
print("Bigest number : ", bigest_number)
print("Smaillest number : ", smailest_number)

