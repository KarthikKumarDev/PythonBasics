films_dictionary = {
    "Thuppaki" :{ "Age" : 3, "Rating": 9, "Protagonist": "Vijay", "Seats" : 50 },
    "Ayan" :{ "Age" : 18, "Rating": 7.5, "Protagonist": "Surya", "Seats" : 50 },
    "Charlie" :{ "Age" : 18, "Rating": 9.5, "Protagonist": "Dulquer Salman", "Seats" : 50 }
}

while True:

    print(films_dictionary)
    movie_choice = input("What film do you want to watch ?: ").strip().title()

    if movie_choice in films_dictionary:

        user_age = int(input("How old are you?: ").strip())
        
        if user_age >= films_dictionary[movie_choice]["Age"] :

            if films_dictionary[movie_choice]["Seats"] > 0:
                print("It's movie time !!!")
                films_dictionary[movie_choice]["Seats"] = films_dictionary[movie_choice]["Seats"] -1 
            else :
                print("Uh oh ! No Seats left, Please choose a different movie !")
        else :
            print("Uh oh !, Please choose a different movie !")
        
    else :
        print("We dont have that film yet !!!")