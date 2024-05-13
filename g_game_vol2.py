

print("\nHello player , this game has 3 category with 3 different levels")
print("\nType 1-3 category you want to play")

# level 1 lists

questions1  = [
    "Question:  What is the largest mammal on Earth? ",
    "Question: What is the fastest land animal?",
    "Question: What is a young dog called?"

]

hints1 = [
    "Hint: It's an aquatic animal known for its immense size.",
    "Hint: It's a wild cat known for its distinctive spots",
    "Hint: It's what puppies are.",
]

answers1 = [ 
    "Blue whale",
    "Cheetah",
    "Puppy"
 ]



# level 2 list

questions2 = [
    "Question: What bird is known for its ability to mimic human speech?",
    "Question: What bird is the national symbol of the United States?",
    "Question: What bird is known for its distinctive call that sounds like laughter?"
]

hints2 = [
    "Hint: It's a colorful bird native to tropical regions. ",
    "Hint: It's a large bird of prey known for its keen eyesight.",
    "Hint: It's a small bird with vibrant plumage often found in rainforests."
]


answers2 = [
    "Parrot",
    "Bald Eagle",
    "Kookaburra"
]




# level 3 lists



question3 = [
    "Question: What is the main ingredient in guacamole?",
    "Question: What is the Italian word for 'dough'?",
    "Question: What is the most consumed meat worldwide?"
]

hints3 = [
    "Hint: This ingredient has a creamy texture and is often used to make a popular Mexican dip.",
    "Hint: This word refers to the mixture of flour, water, and other ingredients used to make bread, pasta, and pizza.",
    "Hint: This meat is commonly associated with various cuisines around the world and is versatile in cooking methods."
]

answers3 = [
    "Avocado",
    "Pasta",
    "Chicken"
]

# exit command 

exit_command = "q"

def play_level(questions, hints, answers):
    print("\nNow you have to choose level")
    level_input = int(input("\nChoose level: "))
    if 1 <= level_input <= 3:
        print(f"\nOkay you are playing level {level_input}")
        print("\n")
        print(questions[level_input - 1])
        print("\n")
        print(hints[level_input - 1]) 
        print("\n")
        answer_input = input("Answer: ")
        if answer_input.lower() == answers[level_input - 1].lower():
            print("Congrats, you got the answer")
        else:
            print("Sorry, wrong answer.")
    else:
        print("Invalid level choice")

def play_category():
    while True:
        user_input = input("\nEnter a number or 'q' to quit: ")
        if user_input.lower() == exit_command:
            return False
        elif user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= 3:
                print(f"\nYou are playing category {user_input}")
                return user_input
            else:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

categories = [questions1, questions2, question3]
hints = [hints1, hints2, hints3]
answers = [answers1, answers2, answers3]

category = play_category()
if category:
    while True:
        play_level(categories[category - 1], hints[category - 1], answers[category - 1])
        choice = input("Do you want to play another level in this category? (y/n): ")
        if choice.lower() != 'y':
            break
