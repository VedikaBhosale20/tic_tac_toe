import tkinter as tk
from tkinter import messagebox

# --- Game Setup ---
root = tk.Tk()
root.title("🎮 Fun Tic Tac Toe")
root.geometry("420x500")
root.resizable(False, False)
root.configure(bg="#fef6e4")

current_player = "X"
emojis = {"X": "❌", "O": "⭕"}
colors = {"X": "#ff6b6b", "O": "#4dabf7"}
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# --- Turn Label ---
turn_label = tk.Label(root, text="Player ❌'s Turn", font=("Helvetica", 16, "bold"), bg="#fef6e4", fg="#333")
turn_label.pack(pady=10)

# --- Win Check Function ---
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    if all(cell != "" for row in board for cell in row):
        return "Draw"
    return None

# --- Button Click Handler ---
def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=emojis[current_player], fg=colors[current_player], state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "😐 It's a Draw!")
            else:
                messagebox.showinfo("Game Over", f"🎉 Player {emojis[winner]} Wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"Player {emojis[current_player]}'s Turn")

# --- Reset Game ---
def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    turn_label.config(text="Player ❌'s Turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# --- Game Board UI ---
frame = tk.Frame(root, bg="#fef6e4")
frame.pack()

for i in range(3):
    for j in range(3):
        btn = tk.Button(
            frame, text="", font=("Arial", 32), width=4, height=2,
            bg="#fff", activebackground="#e3f2fd",
            command=lambda i=i, j=j: on_click(i, j)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

# --- Restart Button ---
restart_btn = tk.Button(root, text="🔁 Restart", font=("Helvetica", 14, "bold"), bg="#ffd6a5", command=reset_game)
restart_btn.pack(pady=20)

# --- Start the Game ---
root.mainloop()
