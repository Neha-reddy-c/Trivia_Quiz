# 🧠 Trivia Quiz Game

A modular, command-line **Trivia Quiz Game** built in Python using Object-Oriented Programming (OOP) principles. The project separates data management, object modeling, and game execution into dedicated modules, creating a clean, maintainable, and extensible codebase.

Each session dynamically selects a randomized set of questions from a larger dataset, providing a fresh experience every time the game is played.

---

## 🚀 Features

* **Dynamic Randomization:** Randomly selects 10 unique questions from the complete question bank for every playthrough.
* **Object-Oriented Design:** Uses separate classes and modules to maintain clear responsibilities and improve maintainability.
* **Interactive CLI Experience:** Provides immediate feedback after each answer while tracking the player's score in real time.
* **Safe Game Flow:** Prevents out-of-range errors through controlled iteration and question management.
* **Easy Customization:** Add, remove, or replace questions in `data.py` without changing the core game logic.

---

## 📂 Project Structure

```text
Trivia_Quiz/
├── main.py       # Application entry point and controller
├── question.py   # Question data model
├── brain.py      # Quiz engine and gameplay logic
├── data.py       # Raw trivia question dataset
└── README.md
```

| File          | Description                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `main.py`     | Initializes the question bank, converts raw dictionaries into `Question` objects, and runs the main game loop.         |
| `question.py` | Defines the `Question` class used to represent each trivia item.                                                       |
| `brain.py`    | Contains the `QuizBrain` engine responsible for randomization, score tracking, user interaction, and game progression. |
| `data.py`     | Stores the complete trivia dataset as a list of dictionaries containing questions and answers.                         |

---

## 🏗️ Technical Architecture

### 1. Data Model (`question.py`)

Each trivia question is represented as an object with two properties:

```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
```

---

### 2. Game Engine (`brain.py`)

The `QuizBrain` class manages gameplay and application state.

#### Core Methods

* `__init__()`
  Receives the full question list and randomly selects up to 10 unique questions for the current session.

* `still_go()`
  Determines whether additional questions remain.

* `next_question()`
  Displays the current question, collects user input, and advances the game state.

* `check_ans()`
  Compares answers case-insensitively, updates the score, and provides immediate feedback.

---

## 🛠️ Installation & Execution

### Prerequisites

* Python 3.x

### Clone the Repository

```bash
git clone https://github.com/Neha-reddy-c/Trivia_Quiz.git
cd Trivia_Quiz
```

### Run the Game

```bash
python main.py
```

---

## 🎮 How to Play

1. Start the application to generate a randomized set of 10 questions.
2. Read each statement carefully.
3. Type `True` or `False` (case-insensitive).
4. Receive instant feedback and view your updated score.
5. Complete all rounds to see your final results.

---

## 💡 Customization

The game is designed for easy expansion.

To add more trivia questions, simply edit the `question_data` list inside `data.py`. Since the application dynamically builds `Question` objects and randomly samples from the dataset, no additional changes are required elsewhere in the codebase.

You can also import datasets from external sources such as Open Trivia Database (OpenTDB) to create themed or larger quizzes.

---

## 🎯 Concepts Demonstrated

* Object-Oriented Programming (OOP)
* Classes and Objects
* Separation of Concerns
* Modular Project Design
* Dynamic Data Processing
* Random Sampling
* User Input Validation
* State Management
* Command-Line Interface (CLI) Development
