print("HeLLo Team!")

name = "Anna"
age = 22
print(f"Hello, {name}!")
print(f"Hello {name}, who is {age} years old")
print("Hello, {name}!")
#Variable names and types
sName = "Anna"
iAge = 22
fPi = 3.14
sname_of_fav_rest = "ABC"
print (sName,iAge,fPi,sname_of_fav_rest)
print (f"{sName},  age {iAge}, like to go to {sname_of_fav_rest} to celebrate {fPi} Day!")

print (type(sName),type(iAge),type(fPi),type(sname_of_fav_rest))

# index 0, 1, 2, 3
iIndex = 0
print("Index right now is ", iIndex, type(iIndex))
iIndex += 1   #iIndex = iIndex + 1
print("Index right now is ", iIndex, type(iIndex))
iIndex = iIndex + 1
print("Index right now is ", iIndex, type(iIndex))
iIndex += 1
print("Index right now is ", iIndex, type(iIndex))

#calculations of different variable
#calculate total price for the purchase
fPrice_of_first_item = 1.23
fPrice_of_second_item = 4.56
iQuanitity_of_first_item = 5
iQuanitity_of_second_item = 8
fTotal_price = fPrice_of_first_item*iQuanitity_of_first_item+ fPrice_of_second_item*iQuanitity_of_second_item
print (type(fTotal_price),type(fPrice_of_first_item),type(iQuanitity_of_first_item))
print(fTotal_price)
print(f"The total price is {fTotal_price}")
print(sName +" paid " + str(fTotal_price) + " for the purchase")
