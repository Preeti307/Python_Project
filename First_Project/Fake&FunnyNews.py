# Fake and Funny news

import random

print("\n----- Welcome to in my funny and fake news world -----\n")

subjects = ["A cat in Delhi","School principal","Scientists","A cow","A student"]
actions = ["opened a YouTube channel","banned homework","discovered","won a dance competition","invented a pillow"]
things_place = ["to teach humans how to sleep 18 hours a day.","after his own son complained about it on Instagram.","that coffee can now power Wi-Fi routers!","after learning steps from YouTube Shorts.","that automatically says “5 more minutes!” every morning."]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    thing_place = random.choice(things_place)

    headline = f"Breaking news {subject} {action} {thing_place}"
    print("\n",headline)

    save_file = input("\nDo you want to save fake and funny headings? (Yes/No) :").strip().lower()
    if save_file == "yes":
        with open("FakeNews.txt","a") as file:
            file.write(headline + "\n")
            file.close()
            print("Your headline successfully stored in FakeNews file !")

    user_input = input("\nDo you want another headline? (Yes/No) :").strip().lower()
    if user_input == "no":
        break


print("====== Thanku for creating fake and funny news :) =====\n")