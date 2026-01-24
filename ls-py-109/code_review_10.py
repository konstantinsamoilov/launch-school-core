
def yes_no_response(string):
    while True:
        print(string)
        input_string = input(string).strip().lower()

        if input_string in ("y", "yes"):
            print("Here we go again!")
            return

        elif input_string in ("n", "no"):
            print("Okay. See you later.")
            return

        else:
            print("You goofed! That is not a valid answer.")

yes_no_response("Do you want to continue? (y/n) ") 
yes_no_response("Are you absolutely sure? (yes/no) ")
print("All done.")