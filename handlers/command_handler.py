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
            "видалити-телефон": self.delete_phone,
            "знайти-контакт": self.find_contact,
            "показати-контакт": self.show_contact,
            "показати-контакти": self.show_contacts,
            "дні-народження": self.birthdays,
            "додати-нотатку": self.add_note,
            "змінити-нотатку": self.edit_note,
            "видалити-нотатку": self.delete_note,
            "додати-тег": self.add_tag,
            "видалити-тег": self.remove_tag,
            "знайти-нотатку": self.find_note,
            "знайти-тег": self.find_tag,
            "показати-нотатки": self.show_notes,
            "сортувати-нотатки": self.sort_notes,
            "зберегти": self.save,
            "експорт-csv": self.export_csv,
            "вихід": self.exit_app,
            "закрити": self.exit_app,
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
        return (
            "Доступні команди:\n"
            "привіт\n"
            "допомога\n"
            "додати-контакт <ім'я>\n"
            "додати-телефон <ім'я> <телефон>\n"
            "додати-email <ім'я> <email>\n"
            "додати-адресу <ім'я> <адреса>\n"
            "додати-день-народження <ім'я> <DD.MM.YYYY>\n"
            "змінити-телефон <ім'я> <старий_телефон> <новий_телефон>\n"
            "змінити-email <ім'я> <новий_email>\n"
            "змінити-адресу <ім'я> <нова_адреса>\n"
            "змінити-день-народження <ім'я> <DD.MM.YYYY>\n"
            "видалити-контакт <ім'я>\n"
            "видалити-телефон <ім'я> <телефон>\n"
            "знайти-контакт <запит>\n"
            "показати-контакт <ім'я>\n"
            "показати-контакти\n"
            "дні-народження <кількість_днів>\n"
            "додати-нотатку <текст>\n"
            "змінити-нотатку <id> <новий_текст>\n"
            "видалити-нотатку <id>\n"
            "додати-тег <id> <тег>\n"
            "видалити-тег <id> <тег>\n"
            "знайти-нотатку <запит>\n"
            "знайти-тег <тег>\n"
            "показати-нотатки\n"
            "сортувати-нотатки\n"
            "зберегти\n"
            "експорт-csv\n"
            "закрити / вихід"
        )

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

    # Видаляє телефон
    @input_error
    def delete_phone(self, args: list[str]) -> str:
        return self.contact_service.delete_phone(args[0], args[1])

    # Шукає контакт
    @input_error
    def find_contact(self, args: list[str]) -> str:
        return self.contact_service.find_contact(" ".join(args))

    # Показує один контакт
    @input_error
    def show_contact(self, args: list[str]) -> str:
        return self.contact_service.show_contact(args[0])

    # Показує всі контакти
    def show_contacts(self, args: list[str]) -> str:
        return self.contact_service.show_all_contacts()

    # Показує найближчі дні народження
    @input_error
    def birthdays(self, args: list[str]) -> str:
        return self.contact_service.upcoming_birthdays(int(args[0]))

    # Додає нотатку
    @input_error
    def add_note(self, args: list[str]) -> str:
        return self.note_service.add_note(" ".join(args))

    # Редагує нотатку
    @input_error
    def edit_note(self, args: list[str]) -> str:
        return self.note_service.edit_note(int(args[0]), " ".join(args[1:]))

    # Видаляє нотатку
    @input_error
    def delete_note(self, args: list[str]) -> str:
        return self.note_service.delete_note(int(args[0]))

    # Додає тег
    @input_error
    def add_tag(self, args: list[str]) -> str:
        return self.note_service.add_tag(int(args[0]), args[1])

    # Видаляє тег
    @input_error
    def remove_tag(self, args: list[str]) -> str:
        return self.note_service.remove_tag(int(args[0]), args[1])

    # Шукає нотатку
    @input_error
    def find_note(self, args: list[str]) -> str:
        return self.note_service.find_notes(" ".join(args))

    # Шукає нотатки за тегом
    @input_error
    def find_tag(self, args: list[str]) -> str:
        return self.note_service.find_notes_by_tag(args[0])

    # Показує всі нотатки
    def show_notes(self, args: list[str]) -> str:
        return self.note_service.show_all_notes()

    # Сортує нотатки за тегами
    def sort_notes(self, args: list[str]) -> str:
        return self.note_service.sort_notes_by_tags()

    # Зберігає всі дані
    def save(self, args: list[str]) -> str:
        self.repository.save_all(
            self.contact_service.contact_book,
            self.note_service.notes_book,
        )
        return "Дані успішно збережено."

    # Експортує дані у CSV
    def export_csv(self, args: list[str]) -> str:
        self.repository.save_all(
            self.contact_service.contact_book,
            self.note_service.notes_book,
        )
        self.repository.export_all_to_csv()
        return "Дані успішно експортовано у CSV."

    # Завершує роботу програми
    def exit_app(self, args: list[str]) -> str:
        self.repository.save_all(
            self.contact_service.contact_book,
            self.note_service.notes_book,
        )
        return "До побачення!"
