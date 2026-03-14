def parse_input(user_input: str) -> tuple[str, list[str]]:
    # Розбиваємо команда + args
    parts = user_input.strip().split()

    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args
