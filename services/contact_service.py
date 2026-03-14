from exceptions import ContactNotFoundError
from models.contact_book import ContactBook
from models.record import Record


class ContactService:
    # Ініціалізує сервіс для роботи з контактами
    def __init__(self, contact_book: ContactBook):
        self.contact_book = contact_book

    # Додає новий контакт
    def add_contact(self, name: str) -> str:
        if self.contact_book.find(name):
            return "Контакт вже існує."

        record = Record(name)
        self.contact_book.add_record(record)
        return "Контакт успішно додано."

    # Додає телефон до контакту
    def add_phone(self, name: str, phone: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.add_phone(phone)
        return "Телефон успішно додано."

    # Додає email до контакту
    def add_email(self, name: str, email: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.set_email(email)
        return "Email успішно додано."

    # Додає адресу до контакту
    def add_address(self, name: str, address: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.set_address(address)
        return "Адресу успішно додано."

    # Додає день народження до контакту
    def add_birthday(self, name: str, birthday: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.set_birthday(birthday)
        return "День народження успішно додано."

    # Редагує телефон контакту
    def edit_phone(self, name: str, old_phone: str, new_phone: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.edit_phone(old_phone, new_phone)
        return "Телефон успішно оновлено."

    # Редагує email контакту
    def edit_email(self, name: str, new_email: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.set_email(new_email)
        return "Email успішно оновлено."

    # Редагує адресу контакту
    def edit_address(self, name: str, new_address: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.set_address(new_address)
        return "Адресу успішно оновлено."

    # Редагує день народження контакту
    def edit_birthday(self, name: str, new_birthday: str) -> str:
        record = self.contact_book.find(name)

        if record is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        record.set_birthday(new_birthday)
        return "День народження успішно оновлено."

    # Видаляє контакт
    def delete_contact(self, name: str) -> str:
        if self.contact_book.find(name) is None:
            raise ContactNotFoundError("Контакт не знайдено.")

        self.contact_book.delete(name)
        return "Контакт успішно видалено."
