# 🃏 Blackjack Game in Python

## 📌 Project Overview
This is a simple *text-based Blackjack game* written in Python. It allows a single user to play against a computer-controlled dealer. The goal is to get as close to 21 as possible without going over.

---

## 🎯 Game Rules
- Each player starts with *two cards*.
- Card values:
  - Numbers 2–10 → Face value
  - Jack, Queen, King → 10
  - Ace → 11 or 1 (auto-adjusted)
- A *Blackjack* is a hand with two cards: Ace + 10.
- The dealer draws cards until the total is *17 or more*.
- You can:
  - 'y' → Take another card
  - 'n' → Pass your turn

---

## 🧠 Game Logic
- Uses Python’s built-in random module to simulate a deck.
- Cards are stored in lists for user and dealer.
- Aces switch from 11 to 1 to avoid busting.
- Winner is decided based on final scores and Blackjack conditions.

---

## 🖥 Requirements
- Python 3.x
- No external libraries needed

---

## 🧾 How to Run
1. Save the code below as blackjack.py
2. Open terminal or VS Code
3. Run the command:
   ```bash
   python black_jack.py
