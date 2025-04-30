import requests
import tkinter as tk
import random
class GUI:
    def __init__(self, window):
        self.window = window
        window.title = "Wordle"
        # wordlist = [
        #     "Brisk", "Broad", "Broom", "Brush", "Caper", "Chore", "Chunk", "Class", "Clasp", "Clear",
        #     "Climb", "Clock", "Clone", "Clove", "Cloud", "Cluck", "Crave", "Crate", "Crave", "Cream",
        #     "Crown", "Creak", "Crimp", "Crush", "Dance", "Daisy", "Dealt", "Douse", "Dodge", "Drill",
        #     "Drink", "Drove", "Drop", "Earth", "Elbow", "Elate", "Eject", "Enjoy", "Elfin", "Enter",
        #     "Extra", "Elms", "Fable", "Feast", "Flick", "Flame", "Flute", "Frost", "Frame", "Frown",
        #     "Gloom", "Globe", "Graft", "Grate", "Grasp", "Grown", "Guard", "Gravy", "Grind", "Guilt",
        #     "Gushy", "Haste", "Hedge", "Honey", "Hush", "Human", "House", "Hilly", "Herds", "Knots",
        #     "Knock", "Knees", "Know", "Lapse", "Lapse", "Laugh", "Lease", "Lemon", "Lodge", "Light",
        #     "Lunar", "Ledge", "Mirth", "Mourn", "Money", "Moose", "Mouse", "Mirth", "Nudge", "Nurse",
        #     "Noise", "Niece", "Nasty", "Nines", "Noisy", "Oasis", "Ovals", "Opium", "Oiled", "Peach",
        #     "Patch", "Plumb", "Place", "Plead", "Pluck", "Pride", "Prize", "Prism", "Proud", "Proxy",
        #     "Quick", "Quake", "Quiet", "Quota", "Ratio", "Reach", "Race", "Rinse", "Riper", "Raise",
        #     "Rally", "Risky", "Road", "Rover", "Round", "Scene", "Scope", "Scale", "Snare", "Slink",
        #     "Shore", "Smile", "Stage", "Stare", "Stump", "Stint", "Storm", "Sweet", "Sweep", "Steep",
        #     "Taper", "Track", "Tramp", "Treat", "Tenth", "Trunk", "Twirl", "Twine", "Unite", "Union",
        #     "Utile", "Usher", "Vogue", "Viper", "Vicar", "Vigor", "Video", "Vowel", "Wager", "Watch",
        #     "Whisk", "Wipes", "Write", "Wiped", "Whale", "Wreak", "Yikes", "Yawns", "Youth", "Zebra",
        #     "Zeroes", "Zesty", "Zippy", "Zingy", "Twist"]
        responce = requests.get("https://random-word-api.herokuapp.com/word?length=5")
        self.word = responce.text.upper()[2:-2:]
        blank = []
    
        WIN_WIDTH = 700
        WIN_HEIGHT = 800

        self.frame = tk.Frame(master = self.window, width = WIN_WIDTH, height = WIN_HEIGHT, bg = "#191919")
        self.frame.pack()

        SQUARE = 100
    
        SQUARE_PADDING = 7
        GAME_WIDTH = SQUARE * 5
        GAME_HEIGHT = SQUARE * 6
        self.gamesquare = [[], [], [], [], [], []]
        self.gridrow = 0

        self.gridframe = tk.Frame(master = self.frame, width = GAME_WIDTH, height = GAME_HEIGHT, bg = "#808080")
        self.gridframe.place(x = (WIN_WIDTH / 2) - (GAME_WIDTH / 2), y = 50)
        for row in range(len(self.gamesquare)):
            for col in range(6):
                self.gamesquare[row].append(tk.Frame(master = self.gridframe, width= SQUARE - SQUARE_PADDING * 2, height= SQUARE - SQUARE_PADDING * 2, bg= "#cccccc"))
                self.gamesquare[row][col].place(x = SQUARE * col + SQUARE_PADDING, y = SQUARE * row + SQUARE_PADDING)


        self.lettersquare = [[], [], [], [], [], []]
        for row in range(len(self.lettersquare)):
            for col in range(6):
                self.lettersquare[row].append(tk.Label(master = self.gamesquare[row][col], text = " ", bg = "#cccccc"))
                self.lettersquare[row][col].place(x=33, y = 33)

        PLAYER_WIDTH = 200
        PLAYER_HEIGHT = 75

        self.playerframe = tk.Frame(master= self.frame, width= PLAYER_WIDTH, height= PLAYER_HEIGHT, bg= "#999999")
        self.playerframe.place(x = (WIN_WIDTH/2) - (PLAYER_WIDTH/2), y = 651)

        self.guess = tk.StringVar()
        self.guessbox = tk.Entry(master= self.playerframe, textvariable= self.guess, font= ("calibre", 20))
        self.guessbox.place(x = 0, y = 10)

    

        self.confirm = tk.Button(master=self.playerframe, text= "bozo", command=self.checkGuess)
        self.confirm.place(x= 163, y= 46 )
    def updateGrid(self, r, c, letter, color):
        targetsquare = self.gamesquare[r][c]
        targetsquare.configure(bg = color)

        targetletter = self.lettersquare[r][c]
        targetletter.configure(text = letter, bg = color)
        
    def checkGuess(self):
        guess = self.guess.get()
        self.guessbox.delete(0, "end")
        if len(guess) != 5:
            return
        
        for i in range(len(guess)):
            letter = guess[i].upper()

            if letter in self.word:
                if letter == self.word[i]:
                    self.updateGrid(self.gridrow, i, letter, "#76d636")
                else:
                    self.updateGrid(self.gridrow, i, letter, "#ffc933")
            else: 
                self.updateGrid(self.gridrow, i, letter, "#666666")
        self.gridrow += 1


root = tk.Tk()
gui = GUI(root)
root.mainloop()

gui.updateGrid(2, 3, "G" "#ff00ff")
