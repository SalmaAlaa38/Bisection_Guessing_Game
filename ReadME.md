# 🎯 Bisection Guessing Game

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

</p>

An interactive desktop application that demonstrates the **Bisection (Binary Search) Algorithm** through a number guessing game.

The user secretly thinks of a number, and the application efficiently finds it by repeatedly dividing the search interval in half based on the user's feedback.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Algorithm](#-algorithm)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Example Walkthrough](#-example-walkthrough)
- [Complexity Analysis](#-complexity-analysis)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

# 📌 Overview

This project was developed to visualize one of the most fundamental searching algorithms in Computer Science:

> **Bisection (Binary Search)**

Instead of checking every possible number one by one, the application continuously halves the search space until it finds the user's number.

This project is intended for students learning:

- Algorithms
- Python
- Tkinter GUI Development
- Event-Driven Programming
- Object-Oriented Programming (future version)

---

# ✨ Features

- ✅ Interactive desktop interface
- ✅ Binary Search implementation
- ✅ Displays current guess
- ✅ Remaining interval visualization
- ✅ Attempt counter
- ✅ Inconsistent answer detection
- ✅ Restart functionality
- 🔄 Planned OOP architecture
- 🔄 Guess history
- 🔄 Statistics dashboard
- 🔄 Custom search range

---

# 🖼 Demo

```
+-------------------------------------------+

        Bisection Guessing Game

Think of a number between 1 and 100

My Guess

              50

Attempts: 1

Possible Range: 1 - 100

[ Higher ] [ Lower ] [ Correct ]

        Start New Game

+-------------------------------------------+
```

*(Replace this section with screenshots or GIFs once available.)*

---

# 🧠 Algorithm

The application uses the **Binary Search Algorithm**.

Each guess is calculated as:

```python
guess = (low + high) // 2
```

Depending on the user's response:

- Higher → `low = guess + 1`
- Lower → `high = guess - 1`
- Correct → End game

The search interval is reduced by half after every guess.

---

# 📂 Project Structure

```
bisection-guessing-game/
│
├── main.py
├── ReadME.md
└── LICENSE
```

Future OOP version:

```
bisection-guessing-game/
│
├── main.py
├── game.py
├── gui.py
├── assets/
└── README.md
```

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone https://github.com/SalmaAlaa38/Bisection_Guessing_Game.git
```

## Navigate to the project

```bash
cd Bisection_Guessing_Game
```

## Run

```bash
python main.py
```

No external dependencies are required.

---

# 🎮 Usage

1. Think of a number between **1** and **100**.
2. Click **Start Game**.
3. Respond to each guess using:
   - **Higher**
   - **Lower**
   - **Correct**
4. Watch the application narrow the search interval until it finds your number.

---

# 📚 Example Walkthrough

Suppose the secret number is **73**.

| Attempt | Guess | Response | Remaining Range |
|----------|------:|----------|-----------------|
| 1 | 50 | Higher | 51 – 100 |
| 2 | 75 | Lower | 51 – 74 |
| 3 | 62 | Higher | 63 – 74 |
| 4 | 68 | Higher | 69 – 74 |
| 5 | 71 | Higher | 72 – 74 |
| 6 | 73 | Correct | ✓ |

---

# 📈 Complexity Analysis

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |
| Space Complexity | O(1) |

Example:

| Range | Maximum Guesses |
|--------|----------------:|
| 1 – 100 | 7 |
| 1 – 1,000 | 10 |
| 1 – 1,000,000 | 20 |

---

# 🛣 Future Improvements

- Object-Oriented Architecture
- Modern UI with PySide6
- Dark Mode
- Guess History
- Search Tree Visualization
- Search Interval Animation
- Custom Difficulty Levels
- Unit Testing
- Executable Packaging
- Sound Effects

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the project and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Salma Selem**

Software Developer | AI Engineer | Backend Developer

Passionate about building intelligent software systems, algorithm visualization tools, and AI-powered applications.