def cs_service_bot():
    response = input("Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer? \n [1] New Customer \n [2] Existing Customer \n")
    #response = input("Please enter the number corresponding to your choice \n")
    if response == "1":
        new_customer()
    elif response == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection. \n")
        cs_service_bot()

def existing_customer():
    response = input("What kind of support do you need? \n [1] Television Support \n [2] Internet Support \n [3] Speak to a support representative \n")
    #response = input("Please enter the number corresponding to your choice ")
    if response == "1":
        television_support()
    elif response == "2":
        internet_support()
    elif response == "3":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection. \n")
        existing_customer()
    
def new_customer():
    response = input("We're excited to have you join the DNS family, how can we help you? \n [1] Sign up for service. \n [2] Schedule a home visit. \n [3] Speak to a sales representative. \n")
    #response = input("Please enter the number corresponding to your choice ")
    if response == "1":
        sign_up()
    elif response == "2":
        home_visit()
    elif response == "3":
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection. \n")
        new_customer()
    
def television_support():
    response = input("What is the nature of your problem? \n [1] I can't access certain channels. \n [2] My picture is blurry. \n [3] I keep losing service. \n [4] Other issues. \n")
    #response = input("Please enter the number corresponding to your choice ")
    if response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative. \n")
        did_that_help()
    elif response == "2":
        print("Try adjusting the antenna above your television set. \n")
        did_that_help()
    elif response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again. \n")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection. \n")
        television_support()

def internet_support():
    response = input("What is the nature of your problem? \n [1] I can't connect to the internet. \n [2] My connection is very slow. \n [3] I can't access certain sites. \n [4] Other issues. \n")
    #response = input("Please enter the number corresponding to your choice ")
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz. \n")
        did_that_help()
    elif response == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth. \n")
        did_that_help()
    elif response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites. \n")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection. \n")
        television_support()

def did_that_help():
    response = input("Did the solution solve your problem? \n [1] Yes \n [2] No \n")
    #response = input("Were we helpful?")
    if response == "1":
        print("Thank you! Have a GREAT day! \n")
    elif response == "2":
        print("Your time is very important to us.  Whom would you like to speak to? \n [1] Live representative \n [2] Schedule a home visit \n")
        second_response = input("Please enter the number corresponding to your choice. \n ")
        if second_response == "1":
            live_rep("support")
        elif second_response == "2":
            home_visit("support")
        else:
            print("Sorry, we didn't understand your selection. \n")
            television_support()
            
def sign_up():
    response = input("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for. \n [1] Bundle Deal (Internet + Cable) \n [2] Internet \n [3] Cable \n")
    #response = input("What are you signing up for?")
    if response == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service. \n")
        home_visit("new_install") 
    elif response == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service. \n")
        home_visit("new_install") 
    elif response == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service. \n")
        home_visit("new_install") 
    else:
        print("Sorry, we didn't understand your selection. \n")
        sign_up()
          
def home_visit(purpose = "none"):
    if purpose == "none":
        response = input("What is the purpose of the service? \n [1] New service installation. \n [2] Existing service repair. \n [3] Location scouting for unserviced region. \n")
        #response = input("what is your choice?")
        if response == "1":
            home_visit("new_install")
        elif response == "2":
            home_visit("support")
        elif response == "3":
            home_visit("scout")
    else:
            visit_date = input("Please enter a date below in the following format of mm-dd-yyyy when you are available for a technician to come to your home and %s \n" % purpose)
            print("Wonderful! A technician will come visit you on %s. Please be available between the hours of 1:00 am and 11:00 pm. \n" % visit_date)
            return visit_date

def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience. \n")
    elif purpose == "support":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience. \n")
    else:
        return "Function not working as expected!!!!  Fix it!!!! \n"
    
    
cs_service_bot()



    
    
    
    
    
    
    
    
    