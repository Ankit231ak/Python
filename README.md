# 🔐 Password Strength Checker (Python)

This is a simple terminal-based **Password Strength Checker** written in Python. It evaluates a password based on five criteria and provides feedback to the user.

---

## ✅ Features

- Checks if password is at least **8 characters** long.
- Ensures presence of:
  - At least one **lowercase** letter
  - At least one **uppercase** letter
  - At least one **digit**
  - At least one **special character** (e.g. !@#$...)

- Gives strength rating:
  - 🔴 Weak
  - 🟡 Moderate
  - 🟢 Strong

- Interactive: You can enter multiple passwords until you type `q` to quit.

---

## 📜 Example Output

```
(q to quit) Enter your password: Hello123
❌ Add at least one special character
--------------------------------
🟡 Your password is Moderate
```

---

## 🧠 How it Works

The script calculates a **strength score (0–5)**:
- 1 point for each rule satisfied
- Based on score, shows strength level

---

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Save the script as `password_checker.py`.
3. Run the script in your terminal:

```bash
python password_checker.py
```

4. Start entering passwords to test their strength.

---

## ❌ To Quit
Type `q` and press Enter.

---
