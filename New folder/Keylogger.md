# Keylogger using pynput

This is a simple keylogger built with Python using the `pynput` library. It listens for keyboard events and logs them to a file named `k.txt`.

## 🔧 How It Works

- Logs all key presses to `k.txt`
- Handles special keys like `Enter`, `Tab`, `Backspace`, `Shift`, etc.
- Stops logging when the `Esc` key is pressed

## 📦 Requirements

- Python 3.x
- `pynput` library

Install `pynput` with:

```bash
pip install pynput
