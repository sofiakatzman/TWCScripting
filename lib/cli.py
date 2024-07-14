import sys
import importlib

# import helper functions
sys.path.append('./helper_functions')
semrushAnalytics = importlib.import_module('semrushAnalytics')
fetchATRecords = importlib.import_module('fetchATRecords')
# application flow functions
def greeting():
    print("")
    print("                Hello! Welcome to TWC Script Manager!")
    print("                Please use number keys to navigate.")

def goodbye():
    print("")
    return print("Goodbye!")

def reroute():
    reroute_choice = 0
    while reroute_choice !=1:  
        print(f'''
            
                Would you like to stay in this module?
                --------------------------------------
                    1 : YES
              
                    2 : NO - GO TO MAIN MENU 
              
        ''')

        reroute_choice = int(input("                    > : "))

        if reroute_choice == 1:
            print("")

        if reroute_choice == 2:
            print("")
            main()

# main application menu
def main():
    choice = 0
    while choice != 5:
        print("MAIN MENU:")
        print("---------")
        print('''
                What would you like to do? 
                --------------------------------------
                    1 : RUN <SEMRUSH REPORTING SCRIPT> 

                    0 : EXIT

        ''')

        choice = int(input("                    > : ")) 

#=> 1 - enter semrush scripting menu
        if choice == 1:
            fetchATRecords()
        
#=> 0 - close app if choice = 0
        if choice == 0:
            return 




if __name__ == "__main__":
    greeting()
    main()
    goodbye()

