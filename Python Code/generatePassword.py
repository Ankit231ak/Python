import random
import string

try:
    import pyperclip
    clipboard = True
except ImportError:
    clipboard = False

def generatePassword(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.SystemRandom().choice(chars) for i in range(length))
    return password

password = generatePassword()
print("Your new strong password is: ", password)

if clipboard:
    pyperclip.copy(password)
    print("Password copied to clipboard")
else:
    print("Install pyperclip to copy password automatically (pip install pyperclip)")
