import secrets
import string


MINIMUM_LENGTH = 8


def generate_password(length: int) -> str:
    """Return a cryptographically secure password of the requested length."""
    if length < MINIMUM_LENGTH:
        raise ValueError(f"Password length must be at least {MINIMUM_LENGTH}.")

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:
    print("PASSWORD GENERATOR")

    try:
        length = int(input("Enter the password length: "))
        password = generate_password(length)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
