word = "lumpy"
running = True
while running:
    validGuess = False
    guess = ""
    
    while not validGuess:
        print("You Will Guess A Five Letter Word... Or Else")
        guess = input()
        validGuess = len(guess) == 5

    colors = ""
    for i in range (len(guess)):
        if guess[i] in word:
            if guess[i] == word[i]:
                colors += "G"
            else:
                colors += "Y"
        else:
            colors += "_"

    print(guess.upper())
    print(colors)


    if guess == word:
        print("You Win! The Word Was", word)  
        running = False