#set
#from Python.Sesision7FunctionsDefinition import greeting, greeting_to_someone, greeting_to_someone_with_return
from Python.Sesision7FunctionsDefinition import *

set1 = {'A','B','C','D','E'}
set2 = {'A','W','C','Z','F'}
print(set1)
print(set2)
set1.add('G')
print(set1)
set1.remove('G')
print(set1)
print("Union of set1 and set2", set1|set2)
print("Difference from set1 and set2", set1 - set2)
print("Difference from set2 and set1", set2 - set1)

print("-"*50)
#Identify missed tests and print out them
allTests = {"login_test","signup_test","regression", "boundary","logout_test"}
executedTests ={"login_test","logout_test"}
missedTests = allTests - executedTests
print(missedTests)

#usage of functions that have been stored in Sesision7FunctionsDefinition.py
print("-"*50)
greeting()
greeting_to_someone("Anna",5)
print(greeting_to_someone_with_return("Team") + greeting_to_someone_with_return("World"))

print("-"*50)
#calculate the tax
tax = calculate_tax(90000)
print(tax)
print(calculate_tax(80000))
print("-"*50)

monthlySalaries = (1000,50000,1000000,500000,400000,88888,5689898989,1246545465456)
totalSalary = sum(monthlySalaries)
print(totalSalary)
print(calculate_tax(totalSalary))
