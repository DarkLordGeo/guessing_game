# everything written below is written by begineer , feel free to share advices , thanks.


# outputing list of choices
print("1","Animals")
print("2","Food")
print("3","Colors")
# options that user should choose
options = {
    "1" : "Animals",
    "2" : "Food",
    "3" : "Colors",
}
# answers
user_answer = "tiger"
user_answer2 ="burger"
user_answer3 ="white"
# hints
hint_1 = "It's a large cat with distinctive orange fur and black stripes."
hint_2 = "It's a sandwich consisting of a grilled or fried meat patty, typically beef, served in a sliced bun with various toppings and condiments."
hint_3 = "Mix of all the colors "

# using while loop

while True:
    user_choice = input("Choose category you want to play: ")

    # if user choice equals to 1 meaning that user is choosing option 1
    # then if they match we get ouputs

    if user_choice == "1":
        print("Okay, guess the animal")
        print("Type 'h' for hint")

# here i defined amount of max attempts 
# so while attempts are less then max_attempts i.e 3 then it will continue to print given input
        
        # main logic for the whole operation
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            user_input = input("Answer: ")
            if user_input.lower() == 'h':
                print("Hint:", hint_1)
            elif user_input.lower() == "tiger":
                print("YOU WIN!")
                break
            # if we get correct answer loop breaks and
            else:
                attempts += 1
                if attempts < max_attempts:
                    print("Sorry, try again please :( ...")
                    # this will continue untill it will be less or equal
        else:
            print("Sorry, you've reached the maximum number of attempts:  ")
            # here goes else if anything goes wrong

    # if user choice equals to 2 meaning that user is choosing option 2
    # then if they match we get ouputs

    # similar logic to the food
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
   
    # similar logic to the color aswell
    
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
           
    # the 'q' will stop the loop and break it 
    if user_choice == 'q':
        print("Quitting game..")
        break      
    
      
     
