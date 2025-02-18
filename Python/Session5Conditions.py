#if - else statements

number = -10
is_positive = number > 0
is_less_then_100 = number < 100
if number >0:
    print("it is positive")
else:
    print("it is negative")

if is_positive:
    print("it is positive")
else:
    print("it is negative")
print ("-"*50)
# verify that number is in the range 0-100
if is_positive and is_less_then_100:
    print("the number is in the range of 0 and 100")
else:
    print("the number is not in the range of 0 and 100")
print ("-"*50)
#test results: A =100%, B - 90-99%, C - 75-89%, D - 74 and less
print("Please input your test score. Test results are based on this rules: A =100%, B - 90-99%, C - 75-89%, D - 74 and less")
score = int(input("Enter your test score "))
text = int(input())
print(f"Your test score is {score}")
print(f"the value of the text {text}")
if score ==100:
    print("Your grade is A")
elif score >=90 and score <= 99:
    print("Your grade is B")
elif score >= 75 and score <= 89:
    print("Your grade is C")
else:
    print("Your grade is D")

print ("-"*50)
# Printout that string is long if it has more than 100 char , short if string is in range of 5-99 and very short if less then 5
#sSentence = "Please input your test score. Test results are based on this rules: A =100%, B - 90-99%, C - 75-89%, D - 74 and less"
sSentence = input("Enter your sentence: ")
length_of_the_string = len(sSentence)
print(f"The length of the sSentence is {length_of_the_string}")
if length_of_the_string >=100:
    print("the sentence is long")
elif length_of_the_string >= 5 and length_of_the_string < 100:
    print("the sentence is short")
else:
    print("the sentence is very short")