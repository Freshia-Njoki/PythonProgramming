# Data type classification that specifies which type of value a variable is
number = 100  # int
second = 56.45  # float
text = "Hello there"  # str
isPythonInteresting = True  # bool

# storing multiple values
cars = ["toyota", "nissan", "vw"]  # List-ordered and changeable
fruits = ("banana", "oranges", "apples")  # tuple - unordered and unchangeable
countries = {"Kenya", "Tanzania", "Tunisia", "Algeria"}  # set - unordered and unchangeable
details = {
    "firstname": "Freshia",
    "age": 20,
    "course": "web development",
    "nationality": "kenyan"
}  # Dictionary: key-value pair


print(second)
print(text)
print(cars)
print(countries)
print(details["firstname"])
print(details["age"])
print(details.get("age"))

# Determine the datatype

print(type(number))
print(type(second))
print(type(text))
print(type(isPythonInteresting))
print(type(cars))
print(type(fruits))
print(type(countries))
print(type(details))


# typecasting

# this is the process of converting one datatype to another

print(float(number))
print(int(round(second)))