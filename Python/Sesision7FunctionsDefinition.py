#library of functions
def greeting():
    print("Hello Team")

def greeting_to_someone(name,number):
    #print a string
    print("Hello,"+ name + str(number))

def greeting_to_someone_with_return(name):
    #print a string
    return  f"Hello,"+ name + "!"

#calculate the taxes from salary
# if salary is <= 100000 then tax is 10%
# if salary is > 100000 then tax is 20%
def calculate_tax(salary):
    if salary <= 100000:
        return salary * 0.1 # if salary is <= 100000 then tax is 10%
    else:
        return salary * 0.2 # if salary is > 100000 then tax is 20%


