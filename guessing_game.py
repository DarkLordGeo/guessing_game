# damn!
print("1","Animals")
print("2","Food")
print("3","Colors")

options = {
    "1" : "Animals",
    "2" : "Food",
    "3" : "Colors",
}

user_answer = "tiger"
user_answer2 ="burger"
user_answer3 ="white"

hint_1 = "It's a large cat with distinctive orange fur and black stripes."
hint_2 = "It's a sandwich consisting of a grilled or fried meat patty, typically beef, served in a sliced bun with various toppings and condiments."
hint_3 = "Mix of all the colors "


while True:
    user_choice = input("Choose category you want to play: ")

    

    if user_choice == "1":
        print("Okay, guess the animal")
        print("Type 'h' for hint")

        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            user_input = input("Answer: ")
            if user_input.lower() == 'h':
                print("Hint:", hint_1)
            elif user_input.lower() == "tiger":
                print("YOU WIN!")
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print("Sorry, try again please :( ...")
        else:
            print("Sorry, you've reached the maximum number of attempts:  ")
    elif user_choice == "2":
        print("Okay, guess the food")
        print("Type 'h' for hint")

        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            user_input = input("Answer: ")
            if user_input.lower() == 'h':
                print("Hint:", hint_2)
            elif user_input.lower() == "burger":
                print("YOU WIN!")
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print("Sorry, try again please :( ...")
    elif user_choice == "3":
        print("Okay, guess the color")
        print("Type 'h' for hint")

        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            user_input = input("Answer: ")
            if user_input.lower() == 'h':
                print("Hint:", hint_3)
            elif user_input.lower() == "white":
                print("YOU WIN!")
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print("Sorry, try again please :( ...")
           

    if user_choice == 'q':
        print("Quitting game..")
        break      
    
      
     
