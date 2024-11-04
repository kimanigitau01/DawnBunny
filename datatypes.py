number = 25 # Int
second = 56.78 # float
tex = "Hello there" # string
isPythonInteresting = True

print(number)
print(second)
print(tex)
print(isPythonInteresting)

# Dta structures - multiple values stores in a single variable
cars = ["Toyota", "Nissan", "VW"] #list - ordered and changeable
fruits = ("banana", "orange" , "apple") # Tuple - ordered but unchangeable
countries = {"kenya", "tunisia", "Algeria"} # Set - unordered amd unchangeable
student = {
    "firstname" : "Mary",
    "age" : 22,
    "course" : "Software engineering",
    "nationality" : "Ugandan"
} # Dictionary - Key and value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["firstname"])

#determine data type
print(type(student))
print(type(cars))
print(type(fruits))
print(type(countries))

print("\n")
#typecasting - process of converting from one data type to another
print(int(second))
print(float(number))
print(str(isPythonInteresting))
print(type(str(isPythonInteresting)))
print(type(isPythonInteresting))

