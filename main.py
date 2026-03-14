from handlers.command_handler import CommandHandler


def main():
    handler = CommandHandler()

    print("Вітаємо у персональному помічнику!")

    while True:
        user_input = input("Введіть команду: ").strip()
        result = handler.handle(user_input)
        print(result)

        if user_input.lower() in {"вихід", "закрити"}:
            break


if __name__ == "__main__":
    main()
