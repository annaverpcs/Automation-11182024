#loops
# 1+2+3+4+5+ ... 20
#for loop
summary = 0
for i in range(1,20):
    #summary += i
    summary = summary +i
    print(f"Summary for each {i} step: {summary}")
print(f"Total summary is: {summary}")

print("-"*50)
# while loop
summary = 0
i=1
while i<20:
    summary = summary + i
    print(f"Summary for each {i} step: {summary}")
    i+=1
print(f"Total summary is: {summary}")

print("-"*50)
#increment =2, summary of only odd numbers
summary = 0
for i in range(1,20,2):
    #summary += i
    summary = summary +i
    print(f"Summary for each {i} step: {summary}" )
print(f"Total summary is: {summary}")
print("-"*50)

#while loop that count down to zero
count = 10
while count >=0:
    print(f"Count is: {count}")
    count -=1
print (f"Final count is: {count}")
print("-"*50)
#nested loops: printout multiplication table
# i * j = i*j
print("multiplication table")
for i in range(1,6):
    for j in range (1,6):
        print(f"{i} * {j} = {i*j}")
    print("-" * 10)

#break and continue
print("-"*50)

for i in range(1,6):
    if i==4:
        print("Exiting the loop when i=4")
        break
    print(i)

print("-"*50)
summary =0
for i in range(1,20):
    summary = summary + i
    if  summary>=50:
        print("Exiting the loop when summary is greater than 50")
        break
    print(i)

print("-"*50)

for i in range(1,6):
    if i==4:
       continue
    print(i)

print("-"*50)
summary =0
for i in range(1,20):
    summary = summary + i
    if  summary>=50:
        print(i)
        print("Exiting the loop when summary is greater than 50")
        continue
