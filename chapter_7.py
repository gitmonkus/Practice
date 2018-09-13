import time

def moon_weight():
    weight = int(input("How much do you weigh?\n> "))
    years = int(input("How many years are you going to be on the moon?\n> "))
    increase = int(input("You put the cookies in there, How many times in a year?\n> "))

    for year in range(1, years + 1):
        weight = weight + increase
        print("Afer year" , year , "of eating cookies, you weigh" , weight , "lbs")
        #time.sleep(3)
        if (year == years):
            print("\n\nSHOVE SOME FU$#%&@ LETTUCE IN THERE!\n\n")

moon_weight()


