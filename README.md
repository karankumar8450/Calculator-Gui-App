# Calculator-Gui-App
Console + Tkinter GUI calculator in Python that handles full multi-operator expressions, not just two numbers.
# Python Calculator (Console + GUI)

A calculator built in Python that parses and evaluates full multi-operator expressions like `2+3+4-4*46`, instead of taking just two numbers at a time.

---

## Features

- Handles multi-digit numbers and multiple operators in one expression
- Left-to-right evaluation (no BODMAS yet)

  - **GUI version** — built with Tkinter, button-based interface
- Handles invalid expressions and division by zero gracefully

---

## How to Run

--- ''' python calculator_gui.py'''

## Example

Input: `2+3+4-4*46`

Step by step: `2+3=5`, `5+4=9`, `9-4=5`, `5*46=230`

Output: `230`

---

## Built With

- Python 3
- Tkinter (for GUI)

---

## What I Learned

- String parsing — breaking an expression into numbers and operators character by character
- Using a temporary buffer to collect multi-digit numbers
- Tkinter basics — grid layout, event handling, lambda functions for button clicks
- Debugging indentation issues that silently break loop logic

---

## Author

**Karan** — learning Python for ML/AI
