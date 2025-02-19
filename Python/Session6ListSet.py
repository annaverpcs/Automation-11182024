#list
numbers = [1,5,7,10,5]
prices = [2.5,1.6,10,5.6]
fruits = ["apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","last banana"]
bFlags = [True, False, False]
mixedList = [12,"QA Automation Testing Class", 11.10,True]

#fruits = ["apple","banana","orange"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[-2])
print(fruits[::-1])

print("-"*50)
#numbers = [1,5,7,10,5]
print(numbers)
print(numbers[0])
print(numbers[1:4])
print(numbers[:4])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])

print("-"*50)
numbers[4] = 20
print(numbers)
print(numbers[::-1])

numbers.append(50) #add 1 element
print(numbers)
print(numbers[::-1])

numbers.extend([100,200])  #extend 1 or multiple elements
print(numbers)
print(numbers[::-1])

del numbers[3]   #delete element by index
print(numbers)
print(numbers[::-1])

numbers.remove(100) #remove element by value
print(numbers)
print(numbers[::-1])

print("-"*50)

#prices = [2.5,1.6,10,5.6]
maxElement = max(prices)
print(maxElement)

print("-"*50)
print(fruits)
print(f"there are {len(fruits)} elements in fruits list")
less_fruits = fruits[len(fruits)-1]
print(less_fruits)
fruits.remove(fruits[len(fruits) - 5])
print(fruits)
print("-"*50)
#tuples
bestFruits = ("apple","banana","orange")
print(bestFruits)
print(bestFruits[0])
print(f"I like {bestFruits[0]}. and dislike {bestFruits[1]}.")
print("-"*50)
list_of_tuples = [("apple",5,1.5),("berry",4,4.5),("banana",5,2.6)]
print(list_of_tuples[-1])
print(list_of_tuples[-1][0])

#(('John', 5000), ('Jane', 5500), ('Jack', 6000))
#find and print out the employee with the highest salary of the month
employees =[('John', 5000), ('Jane', 5500), ('Jack', 6000)]
max_salary = max(employees, key = lambda employees: employees[1])
min_salary =min(employees, key = lambda emp: emp[1])
print(f"Max salary has {max_salary}")
print(f"Min salary has {min_salary}")