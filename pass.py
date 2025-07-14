def password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        print("❌ Password is too short (min 8 characters)")

    if any(i.islower() for i in password):
        strength += 1
    else:
        print("❌ Add at least one lowercase letter")

    if any(i.isupper() for i in password):
        strength += 1
    else:
        print("❌ Add at least one uppercase letter")
    
    if any(i.isdigit() for i in password):
        strength += 1
    else:
        print("❌ Add at least one number")
        
    special_ch = "!@#$%^&*()_+-={}[]|:;\"'<>,.?/~`"
    if any(i in special_ch for i in password):
        strength += 1
    else:
        print("❌ Add at least one special character")

    return strength

while True:
    password = input("(q to quit) Enter your password: ")
    if password == "q":
        break
    strength = password_strength(password)
    print("--------------------------------")


    if strength <= 2:
        print("🔴 Your password is Weak")
    elif strength == 3 or strength == 4:
        print("🟡 Your password is Moderate")
    elif strength == 5:
        print("🟢 Your password is Strong")
