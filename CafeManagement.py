# Cafe Management project

import pandas as pd
menu = {
    "Ice-cream" : {"vanilla":100, 
                 "Chocolate":80, 
                 "strawberry":65, 
                 "mint chocolate chip":90, 
                 "cookies and cream":110, 
                 "butter pecan":95},
    "Pizza" : {"Margherita Pizza":285,
               "Sicilian Pizza":300,
               "Detroit pizza":335,
               "Chicago Pizza":175,
               "Veggie Pizza":225},
    "Pav-bhaji" : {"Regular Pav Bhaji":200,
                   "Pavbhaji with butter":300},
    "Coffee" : {"Coffee":50,
                "Cold coffee":150,
                "Chocolate hote coffee":250},
    "Tea" : {"Masala Chai":15,
             "Cutting Chai":20}
}

print()
print("*************** Welcome to Cafe Delight ***************")
print()

print("Please have a seat Sir/Ma'am.")
print("Here is a menu:")
print()

# Menu list

df_icecream = pd.DataFrame(list(menu["Ice-cream"].items()),columns=["Item","Price"])
print("<========== Ice-Cream ==========>")
print(df_icecream.to_string(index=False))
print()

df_Pizza = pd.DataFrame(list(menu["Pizza"].items()),columns=["Item","Price"])
print("<============ Pizza ============>")
print(df_Pizza.to_string(index=False))
print()

df_Pavbhaji = pd.DataFrame(list(menu["Pav-bhaji"].items()),columns=["Item","Price"])
print("<========== Pav-bhaji ==========>")
print(df_Pavbhaji.to_string(index=False))
print()

df_Coffee = pd.DataFrame(list(menu["Coffee"].items()),columns=["Item","Price"])
print("<=========== Coffee ============>")
print(df_Coffee.to_string(index=False))
print()

df_Tea = pd.DataFrame(list(menu["Tea"].items()),columns=["Item","Price"])
print("<============= Tea =============>")
print(df_Tea.to_string(index=False))
print()

# After 5 to 10 min
price = 0

while True:
    item = input("What would you like to order? , Sir/Ma'am! ").lower()
    if item == "icecream" or item == "ice-cream" or item == "ice cream":
        print("We have these flavors:")
        for flavor in menu["Ice-cream"]:
            print(flavor)
        print()
        flavor_choice = input("Which flavor do you want? ").lower()

    # check if flavor exists
        if flavor_choice in [f.lower() for f in menu["Ice-cream"]]:
        # find actual name and price
            for f, p in menu["Ice-cream"].items():
               if f.lower() == flavor_choice:
                price += p
                print(f"\n✅ Great choice! {f.title()} costs ₹{p}.")
                break

        else:
            print("Sorry, that flavor is not available.")

    elif item == "pizza":
        print("We have these flavors:")
        for flavor in menu["Pizza"]:
            print(flavor)
        print()
        flavor_choice = input("Which pizza flavor do you want? ").lower()

        if flavor_choice in [f.lower() for f in menu["Pizza"]]:
           for f,p in menu["Pizza"].items():
               price += p
               print(f"\n✅ Great choice! {f.title()} costs ₹{p}.")
               break
        else:
            print("Sorry, that flavor is not available.")

    elif item == "pav-bhaji" or item == "pavbhaji" or item == "pav bhaji":
        print("We have these flavors:")
        for flavor in menu["Pav-bhaji"]:
           print(flavor)
        print()

        flavor_choice = input("Which type of Pav-bhaji do you want? ").lower()

        if flavor_choice in [f.lower() for f in menu["Pav-bhaji"]]:
            for f,p in menu["Pav-bhaji"].items():
                if f.lower() == flavor_choice:
                    price += p
                    print(f"\n✅ Great choice! {f.title()} costs ₹{p}.")
                    break
        else:
            print("Sorry, that flavor is not available.")

    elif item == "coffee":
        print("We have these flavors:")
        for flavor in menu["Coffee"]:
            print(flavor)
        print()

        flavor_choice = input("Which type of coffee do you want? ").lower()

        if flavor_choice in [f.lower() for f in menu["Coffee"]]:
            for f,p in menu["Coffee"].items():
                if f.lower() == flavor_choice:
                    price += p
                    print(f"\n✅ Great choice! {f.title()} costs ₹{p}.")
                    break
        else:
            print("Sorry, that flavor is not available.")

    elif item == "tea":
        print("We have these flavors:")
        for flavor in menu["Tea"]:
            print(flavor)
        print()

        flavor_choice = input("Which type of tea do you want? ").lower()

        if flavor_choice in [f.lower() for f in menu["Tea"]]:
            for f,p in menu["Tea"].items():
                if f.lower() == flavor_choice:
                    price += p
                    print(f"\n✅ Great choice! {f.title()} costs ₹{p}.")
                    break
        else:
            print("Sorry, that flavor is not available.")
    else:
        print("Sorry,That item is not available on our menu !")

    another = input("would you like to order another one? , Sir/Ma'am! ").lower()
    if another != "yes":
        break



print("\nYour total bill is: ₹", price)
print("Thank you for visiting Cafe Delight ! ")
