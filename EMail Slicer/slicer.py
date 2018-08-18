# get user email address
email = input("What is your EMail address ? : ").strip()

# slice out user name
user_name = email[:email.index('@')]

# slice domain name
domain_name = email[email.index('@') + 1:]

# format message
message = "Your UserName is {} and your domain name is {} ".format(user_name, domain_name)

# display output
print(message)