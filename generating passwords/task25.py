import secrets
import string

counter = 0


def generate_password(length: int):
    global counter
    counter += 1
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(all_chars) for _ in range(length))
    return password


def generate_special_password(length: int):
    while True:
        password = generate_password(length)
        if (
            any(character.isupper() for character in password)
            and any(character.islower() for character in password)
            and any(character.isdigit() for character in password)
            and any(character in string.punctuation for character in password)
        ):
            break
    return password


print(generate_special_password(5))
print(f"quantity attempts: {counter}")
