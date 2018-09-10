def Spacehip_Building():

    #### Static variables to be used in this function ####
    startwith_cans = int(input("How many cans do you have in supply?\n>"))
    cans = int(input("How many cans can you add to the wall in a given week?\n>"))
    number_of_weeks = int(input("How many weeks is this project going to run?\n>")) + 1
    total_cans = 0


    #### Run this if cans is greater than startwith_cans ####
    if(cans > startwith_cans or cans < 0):
        print("\nDOOD -- I only have %s cans!..." % (startwith_cans))
        print("\nTRY again using a whole number that is greater than 0 and less than %s!\n" % (startwith_cans))

    #### Run this if cans is less than startwith_cans ####
    else:
        for week in range(1, number_of_weeks):

            #### Dynamic variables to be used within the for loop ####
            total_cans += cans
            weeks = number_of_weeks - 1
            cans_left = startwith_cans - total_cans
            years_left = (cans_left / total_cans)
            weeks_left = (52 * years_left)

            #### Print the following everytime through the loop ####
            print("\nIn week %s I was able to convert %s cans to add to my ship wall." % (week, cans))
            print("I only need %s more cans to complete the job.\n" % (cans_left))

            #### Matches when all cans are not used within number_of_weeks ####
            if(cans_left > 0 and week == weeks):
                print("There are still cans needed to complete the ship wall!")
                print("After 1 year I still need %s cans." % (cans_left))
                print("At this rate I will still need %s weeks or %s years to complete my ship wall." % (int(weeks_left), int(years_left)))

            #### Updates cans to be the amount of cans left, so that all cans are used ####
            elif(cans_left <= cans and cans_left > 0):
                cans = cans_left

            #### Matches when all cans are used ####
            elif(cans_left == 0):
                print("Great job!\nNo more cans!\n")
                print("I was able to complete the ship wall in under 1 year -- inside %s weeks\nand used %s out of %s cans." % (week, total_cans, startwith_cans))
                print("\nWhat does my ship need next?")
                break

#### Calls the function, so it can be ran, and gives an argument for cans ####
#### Try a different number to get different results ####
Spacehip_Building()
