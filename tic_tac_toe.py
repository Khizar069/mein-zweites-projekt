import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [None] * 9
        self.buttons = []
        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.window, text="", font=("Arial", 24), height=2, width=5,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def on_click(self, index):
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Spiel beendet", f"Spieler {self.current_player} gewinnt!")
                self.reset_game()
            elif None not in self.board:
                messagebox.showinfo("Spiel beendet", "Unentschieden!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        win_patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None:
                return True
        return False
    
    def reset_game(self):
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    TicTacToe()