from collections import UserDict
from datetime import date, timedelta

from models.record import Record


class ContactBook(UserDict):
    # Додає контакт до книги
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    # Шукає контакт за ім'ям
    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    # Видаляє контакт за ім'ям
    def delete(self, name: str) -> None:
        del self.data[name]

    # Пошук за ім'ям, телефоном, email або адресою
    def search(self, query: str) -> list[Record]:
        normalized = query.strip().lower()
        results = []

        for record in self.data.values():
            if normalized in record.name.value.lower():
                results.append(record)
                continue

            if record.email and normalized in record.email.value.lower():
                results.append(record)
                continue

            if record.address and normalized in record.address.value.lower():
                results.append(record)
                continue

            if any(normalized in phone.value for phone in record.phones):
                results.append(record)

        return results

    # Повертає список найближчих днів народження
    def get_upcoming_birthdays(self, days: int) -> list[dict]:
        today = date.today()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday = record.birthday.value
            congratulation_date = birthday.replace(year=today.year)

            if congratulation_date < today:
                congratulation_date = congratulation_date.replace(year=today.year + 1)

            days_diff = (congratulation_date - today).days

            if 0 <= days_diff <= days:
                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                    }
                )

        return upcoming_birthdays
