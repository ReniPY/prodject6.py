def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(symbol.isupper() and symbol.isalpha() for symbol in password)


def main():
    checks = [
        has_digit,
        is_very_long,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    password = input("Введите пароль: ")

    count = 0
    for check in checks:
        if check(password):
            count += 2
    print(f"Рейтинг этого пароля: {count}")


if __name__ == "__main__":
    main()
