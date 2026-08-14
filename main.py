import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


if __name__ == "__main__":
    password = "Rikkei@123"

    hashed_password = hash_password(password)
    print(hashed_password)
    print(verify_password("Rikkei@123", hashed_password))
    print(verify_password("Rikkei@456", hashed_password))
