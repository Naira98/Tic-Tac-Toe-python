# 🎮 Tic-Tac-Toe Python Game

A classic **Tic-Tac-Toe game** built in Python! This project offers a **simple, command-line interface** for two players, designed with **Object-Oriented Programming (OOP)** for clean and easy-to-understand code.

---

## ✨ Features

- **Two-Player Gameplay:** Challenge a friend in a local multiplayer match.
- **Winner Starts Next Game:** The player who wins a round gets the first move in the subsequent game, adding a strategic element to consecutive matches.
- **Clear Win/Draw Conditions:** Accurately detects wins along rows, columns, and diagonals, as well as draws.
- **Command-Line Interface:** Play directly in your terminal.
- **Object-Oriented Design:** The game logic, board, and players are encapsulated using OOP principles, making the code easy to understand, maintain, and extend.

---

## 🎥 Demo Video

Watch a short video demonstration of the Tic-Tac-Toe Game in action:
<video src="https://github.com/user-attachments/assets/77eac456-2767-4f40-9854-6e7a917aba91" controls autoplay loop muted width="100%"></video>

---
## ▶️ How to Play

### Requirements

To run this game, you only need Python installed on your system.

- Python 3.x

### Running the Game

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Naira98/Tic-Tac-Toe-python.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Tic-Tac-Toe-python
    ```
3.  **Run the game:**
    ```bash
    python3 main.py
    ```

---

## 🏗️ Project Structure & OOP Principles

The project is structured to demonstrate good OOP practices:

- **Board Class:** Manages the game board's state, including placing markers, checking for valid moves, and displaying the board.
- **Player Class:** Represents a player, storing their name and symbol.
- **Game Class:** Orchestrates the entire game flow, handling player turns, checking for win/draw conditions, and managing game resets.
- **Menus Class:** Handles the display of menus and user interactions for game options (e.g., starting a new game, exiting).
- **Utils Class:** Contains utility functions that support various parts of the game, such as display formatting or clear terminal, keeping the main classes focused on their core responsibilities.

This separation of concerns makes the code more robust and easier to debug or enhance.

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
