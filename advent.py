import tkinter as tk
from tkinter import messagebox

class TextAdventureGame:
    def __init__(self, master):
        self.master = master
        master.title("Text Adventure Game")

        self.story_text = tk.Label(master, text="Welcome to the Adventure Game!")
        self.story_text.pack()

        self.choice_button = tk.Button(master, text="Start Adventure", command=self.start_adventure)
        self.choice_button.pack()

        self.player_inventory = []

    def start_adventure(self):
        self.update_story("You wake up in a mysterious forest.")
        self.update_choices(["Explore the Forest", "Rest by the River"], [self.explore_forest, self.rest_by_river])

    def explore_forest(self):
        self.update_story("As you explore, you find a hidden cave.")
        self.update_choices(["Enter the Cave", "Continue Exploring"], [self.enter_cave, self.continue_exploring])

    def rest_by_river(self):
        self.update_story("You rest by the river and regain your energy.")
        self.update_choices(["Continue Exploring", "Build a Shelter"], [self.continue_exploring, self.build_shelter])

    def enter_cave(self):
        self.update_story("Inside the cave, you discover a magical crystal.")
        self.update_choices(["Take the Crystal", "Leave the Cave"], [self.take_crystal, self.leave_cave])

    def continue_exploring(self):
        self.update_story("You venture deeper into the forest.")
        self.show_endings()

    def build_shelter(self):
        self.update_story("You build a shelter and spend the night safely.")
        self.show_endings()

    def take_crystal(self):
        self.player_inventory.append("Magical Crystal")
        self.update_story("You take the magical crystal. It has been added to your inventory.")
        self.show_endings()

    def leave_cave(self):
        self.update_story("You decide to leave the dark cave.")
        self.show_endings()

    def show_endings(self):
        # Determine the ending based on player choices and inventory
        ending_message = "Game Over\n\n"
        if "Magical Crystal" in self.player_inventory:
            ending_message += "Congratulations! You found the magical crystal and completed your quest!"
        else:
            ending_message += "Unfortunately, your journey ends here. Better luck next time."

        # Display the ending message in a messagebox
        messagebox.showinfo("Game Over", ending_message)
        self.master.destroy()

    def update_story(self, text):
        self.story_text.config(text=text)

    def update_choices(self, choices, functions):
        for button in self.choice_button.winfo_children():
            button.destroy()

        for i, choice in enumerate(choices):
            tk.Button(self.master, text=choice, command=functions[i]).pack()

# Create the main window
root = tk.Tk()
game = TextAdventureGame(root)
root.mainloop()
