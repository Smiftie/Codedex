def picks():
    picks = []
    total_picks = 7 #Total Selection
    while len(picks) < total_picks:
        selection = int(input("Enter the number you wish to selection for the lottery between 1-35: "))
        if selection >= 1 and selection <= 35:
            picks.append(selection)
            continue
        elif selection in picks:
            print("You have already entered this number. Please use a different number.")
            continue
        else:
            print("You have selected an invalid number. Please try again.")
            continue
    
    print(f'You have selected these numbers for the lottery: {picks}.')
    return picks
    
def agreement(picks):    
    agreement = input("Do you wish to go ahead with these numbers (Y/N)? ")
    if agreement == "Y" or agreement == "Yes" or agreement == "y" or agreement == "yes":
        print("Your numbers are now locked in. Good Luck!")
        return picks
    elif agreement == "N" or agreement == "No" or agreement == "n" or agreement == "no":
        picks = []
        print("Your selection will be cleared. Please re-run the program.")
