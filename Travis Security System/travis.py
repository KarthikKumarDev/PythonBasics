known_users_list = ['Karthik', 'Ameer', 'Kannan', 'Bala']

print(len(known_users_list))

while True:
    print("Hi ! My name is Travis")
    name = input("What is your name ?").strip().capitalize()
    if name in known_users_list:
        print("Welcome " + name + " !")
        removal_preference = input("Would you like to be removed from the system (y/n) ?").lower()

        if removal_preference == "y":
            print(known_users_list)
            known_users_list.remove(name)
            print("Removed")
            print(known_users_list)

    else:
        print("I don't think I have met you yet {}".format(name))
        add_flag = input("Would you like to be added to the system (y/n) ?: ").strip().lower()
        if add_flag == 'y':
            known_users_list.append(name)
        else :
            print("See you around then {} !".format(name) )