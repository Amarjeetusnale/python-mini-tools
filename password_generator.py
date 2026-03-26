import secrets
import string


def strong_password(length=12):
    """
    Generate a strong random password.

    Args:
        length (int): Minimum length = 4

    Returns:
        str: Secure password
    """
    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation
    password += [secrets.choice(characters) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def main():
    print("🔐 Strong Password Generator")

    try:
        length = int(input("Enter password length: "))
        password = strong_password(length)
        print(f"\n✅ Strong Password: {password}")
    except ValueError as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()