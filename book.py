name = input("enter your name ")
print("welcome", name,)

answer = input("you are on a dirt road, it has come to end and you can go left or right, which way would you like to go")

if answer == "left":
    answer = input("you come to river,type walk to walk and swim to swim ")
    if answer == "walk":
        print("you can walk")
    elif answer == "swim":
        print("you can swim")
    else:
        print("not a valid option. you lose")
elif answer == "right":
    answer = input("welcome to GTA game page, select car for car and mission for mission? ")
    if answer == "mission":
        print("enter in the mission")
    elif answer == "car":
        answer = input("which company you like it? ")
        if answer == "bmw":
            print("great one")
        elif answer == "audi":
            print("own it")
        else:
            print("not in option")
    else:
        print("better luck next time")
else:
    print("not a valid option. you lose")
