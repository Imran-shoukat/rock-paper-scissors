import tkinter as tk
import random

# Game choices
ROCK = 1
PAPER = 2
SCISSORS = 3

NAMES = {
    ROCK: "Rock",
    PAPER: "Paper",
    SCISSORS: "Scissors"
}

# Each choice beats the value mapped to it
RULES = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}


def gui():
    """Create and configure the game interface."""
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")
    root.resizable(False, False)

    player_choice = tk.IntVar(value=ROCK)
    computer_choice = tk.StringVar(value="Waiting...")
    result_set = tk.StringVar(value="Choose your move and click Play!")

    player_score = tk.IntVar(value=0)
    computer_score = tk.IntVar(value=0)

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid(row=0, column=0)

    # Column headings
    tk.Label(
        frame, text="Player", font=("Arial", 12, "bold")
    ).grid(row=0, column=0, padx=15, pady=5)

    tk.Label(
        frame, text="Computer", font=("Arial", 12, "bold")
    ).grid(row=0, column=2, padx=15, pady=5)

    # Player choices
    choices_frame = tk.Frame(frame)
    choices_frame.grid(row=1, column=0, sticky="w")

    for row, (choice, name) in enumerate(NAMES.items()):
        tk.Radiobutton(
            choices_frame,
            text=name,
            variable=player_choice,
            value=choice
        ).grid(row=row, column=0, sticky="w")

    # Computer's move
    tk.Label(
        frame,
        textvariable=computer_choice,
        width=12
    ).grid(row=1, column=2)

    # Play button
    tk.Button(
        frame,
        text="Play",
        width=12,
        command=lambda: game(
            player_choice,
            computer_choice,
            result_set,
            player_score,
            computer_score
        )
    ).grid(row=2, column=1, padx=10, pady=10)

    # Scores
    tk.Label(frame, text="Player Score:").grid(
        row=3, column=0, sticky="w", pady=5
    )
    tk.Label(
        frame, textvariable=player_score
    ).grid(row=4, column=0)

    tk.Label(frame, text="Computer Score:").grid(
        row=3, column=2, sticky="w", pady=5
    )
    tk.Label(
        frame, textvariable=computer_score
    ).grid(row=4, column=2)

    # Game result
    tk.Label(
        frame,
        textvariable=result_set,
        wraplength=350,
        justify="center"
    ).grid(row=5, column=0, columnspan=3, pady=15)

    root.mainloop()


def game(
    player_choice,
    computer_choice,
    result_set,
    player_score,
    computer_score
):
    """Play one round of Rock, Paper, Scissors."""
    player = player_choice.get()
    computer = random.randint(ROCK, SCISSORS)

    computer_choice.set(NAMES[computer])

    result(
        player,
        computer,
        result_set,
        player_score,
        computer_score
    )


def result(
    player,
    computer,
    result_set,
    player_score,
    computer_score
):

    if player == computer:
        result_set.set("It's a tie!")
    elif RULES[player] == computer:
        result_set.set("You win this round!")
        player_score.set(player_score.get() + 1)
    else:
        result_set.set("The computer wins this round!")
        computer_score.set(computer_score.get() + 1)


if __name__ == "__main__":
    gui()