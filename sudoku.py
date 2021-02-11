print("Hello friends! Welcome to my sudoku generator. Enjoy!")

difficulty = input("Please Input Your Difficulty (Easy, Medium, Hard): ")

def sudoku_diff():
    if difficutly.lower() == "easy":
        print("E")
    elif difficulty.lower() == "medium":
        print("M")
    elif difficulty.lower() == "hard":
        print("H")
    else:
        print("Invalid Entry! \n Please start the program again. Goodbye. ")
        quit()
