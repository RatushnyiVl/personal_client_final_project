from personal_assistant.exceptions import ValidationError
from personal_assistant.models.address import Address
from personal_assistant.models.birthday import Birthday
from personal_assistant.models.email import Email
from personal_assistant.models.name import Name
from personal_assistant.models.phone import Phone


class Record:

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.email: Email | None = None
        self.address: Address | None = None
        self.birthday: Birthday | None = None

    # Додає телефон
    def add_phone(self, phone: str) -> None:
        phone_obj = Phone(phone)

        if any(item.value == phone_obj.value for item in self.phones):
            raise ValidationError("Такий номер телефону вже існує.")

        self.phones.append(phone_obj)

    # Видаляє телефон
    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)

        if phone_obj is None:
            raise ValidationError("Номер телефону не знайдено.")

        self.phones.remove(phone_obj)

    # Редагує телефон
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone_obj = self.find_phone(old_phone)

        if phone_obj is None:
            raise ValidationError("Старий номер телефону не знайдено.")

        new_phone_obj = Phone(new_phone)

        if any(item.value == new_phone_obj.value for item in self.phones if item.value != old_phone):
            raise ValidationError("Такий номер телефону вже існує.")

        phone_obj.value = new_phone_obj.value

    # Шукає телефон
    def find_phone(self, phone: str) -> Phone | None:
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    # Встановлює email
    def set_email(self, email: str) -> None:
        self.email = Email(email)

    # Встановлює адресу
    def set_address(self, address: str) -> None:
        self.address = Address(address)

    # Встановлює день народження 
    def set_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    # Повертає рядкове представлення 
    def __str__(self) -> str:
        phones_str = ", ".join(phone.value for phone in self.phones) if self.phones else "немає"
        email_str = self.email.value if self.email else "не вказано"
        address_str = self.address.value if self.address else "не вказано"
        birthday_str = str(self.birthday) if self.birthday else "не вказано"

        return (
            f"Ім'я: {self.name.value} | "
            f"Телефони: {phones_str} | "
            f"Email: {email_str} | "
            f"Адреса: {address_str} | "
            f"День народження: {birthday_str}"
        )
