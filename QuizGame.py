# Quiz Game

class Quiz:
    
    def jeneralKnowledge(self):
        point = 0
        print("\n-*-*-*-*-*-*-*-* Jeneral Quiz -*-*-*-*-*-*-*-*")
        print("Q.1 Which animal has no heart? \n1) Ant \n2) Giraffe \n3) Jellyfish")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 3:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.2 What is tomato? \n1) Vegetable \n2) Fruit \n3) Nut")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.3 How many minutes in one day? \n1) 1440 \n2) 1200 \n3) 720")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 1:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.4 Which planet has the most moons? \n1) Jupiter \n2) Saturn \n3) Neptune")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.5 What is 12+12-13 ? \n1) 9 \n2) 11 \n3) 13")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.6 Which bird can't fly? \n1) Penguin \n2) Chicken \n3) Ostrich")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 1:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.7 Which country invented paper? \n1) China \n2) Egypt \n3) USA")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 1:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.8 What is the currency of Japan? \n1) Won \n2) Yen \n3) Doller")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()
        print(f"You got {point} point ,Well Done !")
    
    def coddingQuiz(self):
        point = 0
        print("\n-*-*-*-*-*-*-*-* Codding Quiz -*-*-*-*-*-*-*-*")
        print("Q.1 What will be the output of print(2**3**2)? \n1) 512 \n2) 64 \n3) 8")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 1:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.2 Which keyword is used to define a function in Python? \n1) func \n2) def \n3) define")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.3 What is the output of print(bool('False'))? \n1) False \n2) True \n3) Error")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.4 Which of these is an immutable data type? \n1) List \n2) Dictionary \n3) Tuple")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 3:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.5 What will be the output of print(type([]))? \n1) list \n2) dict \n3) set")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 1:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()
        print(f"You got {point} point ,Well Done !")

    def funnyQuestion(self):
        point = 0
        print("\n-*-*-*-*-*-*-*-* Jeneral Quiz -*-*-*-*-*-*-*-*")
        print("Q.1 What runs but never walks? \n1) A car \n2) Water \n3) Time")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.2 What has many keys but can’t open a door? \n1) Piano \n2) Monkey \n3) Keyboard")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 1:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.3 What gets wetter as it dries? \n1) Sponge \n2) Towel \n3) Soap")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.4 Which month has 28 days? \n1) February \n2) All months \n3) Only leap year month")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 2:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()

        print("Q.5 What can you catch but not throw? \n1) Cold \n2) Ball \n3) Fish")
        user_answer = int(input("Your answer (Option:1,2,3): "))
        if user_answer == 1:
            print("Right ✅")
            point += 1
        else:
            print("Wrong ❎")
        print()
        print(f"You got {point} point ,Well Done !")


# game starting

print("\n-*-*-*-*-*-*-*-* Welcome to the Quize Game -*-*-*-*-*-*-*-*")
print()

print("This game is made only for enjoyment and gaining knowledge.\nLet's begin.....!")
print("There are three different types of quizzes in this game, you can choose any quiz pattern according to your interest.")
print()

quizpattern = Quiz()
while True:
    user_choice = int(input("Choose any one quiz pattern, \n1.Jeneral Knowledge \n2.Codding Quiz \n3.Funny Question \nEnter you choice(1/2/3):"))
    if user_choice == 1:
        quizpattern.jeneralKnowledge()
    elif user_choice == 2:
        quizpattern.coddingQuiz()
    elif user_choice == 3:
        quizpattern.funnyQuestion()
    else:
        print("you enter wrong option!")
    print()
    other = input("Will you try playing again ?,If yes, enter \"yes\", otherwise \"no\": ").strip().lower()
    if other != "yes":
        break

print("\n-*-*-*-*-*-*-*-* Thank you for being a part of the Quiz Game -*-*-*-*-*-*-*-*\n")
