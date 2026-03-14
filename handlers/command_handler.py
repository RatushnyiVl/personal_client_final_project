from handlers.parser import parse_input
from services.contact_service import ContactService
from services.note_service import NoteService
from storage.file_repository import FileRepository
from utils.decorators import input_error


class CommandHandler:
    # Ініціалізація всіх команд
    def __init__(self):
        self.repository = FileRepository()
        contacts, notes = self.repository.load_all()

        self.contact_service = ContactService(contacts)
        self.note_service = NoteService(notes)

        self.commands = {
            "привіт": self.hello,
            "допомога": self.help_command,
            "додати-контакт": self.add_contact,
            "додати-телефон": self.add_phone,
            "додати-email": self.add_email,
            "додати-адресу": self.add_address,
            "додати-день-народження": self.add_birthday,
            "змінити-телефон": self.edit_phone,
            "змінити-email": self.edit_email,
            "змінити-адресу": self.edit_address,
            "змінити-день-народження": self.edit_birthday,
            "видалити-контакт": self.delete_contact,
        }

    # обробка команд
    def handle(self, user_input: str) -> str:
        command, args = parse_input(user_input)

        if not command:
            return "Введіть команду."

        handler = self.commands.get(command)

        if handler is None:
            return "Невідома команда. Введіть 'допомога', щоб побачити список команд."

        return handler(args)


    def hello(self, args: list[str]) -> str:
        return "Чим можу допомогти?"

    # вивести хелпер
    def help_command(self, args: list[str]) -> str:
        pass

    # Додає контакт
    @input_error
    def add_contact(self, args: list[str]) -> str:
        return self.contact_service.add_contact(args[0])

    # Додає телефон
    @input_error
    def add_phone(self, args: list[str]) -> str:
        return self.contact_service.add_phone(args[0], args[1])

    # Додає email
    @input_error
    def add_email(self, args: list[str]) -> str:
        return self.contact_service.add_email(args[0], args[1])

    # Додає адресу
    @input_error
    def add_address(self, args: list[str]) -> str:
        return self.contact_service.add_address(args[0], " ".join(args[1:]))

    # Додає день народження
    @input_error
    def add_birthday(self, args: list[str]) -> str:
        return self.contact_service.add_birthday(args[0], args[1])

    # Редагує телефон
    @input_error
    def edit_phone(self, args: list[str]) -> str:
        return self.contact_service.edit_phone(args[0], args[1], args[2])

    # Редагує email
    @input_error
    def edit_email(self, args: list[str]) -> str:
        return self.contact_service.edit_email(args[0], args[1])

    # Редагує адресу
    @input_error
    def edit_address(self, args: list[str]) -> str:
        return self.contact_service.edit_address(args[0], " ".join(args[1:]))

    # Редагує день народження
    @input_error
    def edit_birthday(self, args: list[str]) -> str:
        return self.contact_service.edit_birthday(args[0], args[1])

    # Видаляє контакт
    @input_error
    def delete_contact(self, args: list[str]) -> str:
        return self.contact_service.delete_contact(args[0])



