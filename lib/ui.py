def prompt(options, status = [], msg = None, inline_msg = None):
    """
    Prompts user to choose between the provided options given as [(str, function), ...], where function has arity 0.
    Active statuses can optionally be provided as a string array [str, ...].
    The prompt message and inline prompt message can optionally be set.
    """
    
    #Attempt input until input is valid
    while True:
        #If there are active statuses, show them
        if (len(status) != 0):
            print("STATUS", end="\n  ")
            print("\n  ".join(status))

        #Prompt and show options
        print("\n" + ("Choose an option:" if msg == None else msg))
        for i, option in enumerate(options):
            print(f"  {i + 1}) {option[0]}")

        #Ask user for input
        raw_input = input('\n' + ("> " if inline_msg == None else inline_msg))
        #Print empty line for readability
        print()

        #Parse input
        try:
            #Attempt parsing raw input to string
            parsed_input = int(raw_input)
            
            #If input is a valid option, break out of loop
            #NOTE: Not an off by one error, input is shifted by one
            if 0 < parsed_input <= len(options):
                #Shift parsed input back by one to zero-index
                parsed_input -= 1
                break

        except ValueError:
            pass
        
        #Input was invalid, output error and reattempt input
        print("Invalid option - press enter to try again...")
        input()


    #Valid option was chosen, call option function
    options[parsed_input][1]()
