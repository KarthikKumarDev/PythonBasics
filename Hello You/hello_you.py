# Get user input for "Name"
name = input('What is your name ? ')

print(name)

# Get user input for "Age"
age = int(input('How old are you ? '))

print(age)
print(type(age)) 

# Get user input for "City"
city = input('Where do you come from ? ')

print(city)

# Get user input for "Interest"
interest = input('What do you like ? ')

print(interest)

# Create output text
message = "Your name is {} and you are {} years old. You live in {} and you love {}"

output = message.format(name, age, city, interest)

# Print output to screen
print(output)
