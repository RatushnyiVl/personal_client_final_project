import csv

from exceptions import StorageError


class CsvClient:
    _instance = None

    # Єдиний екземпляр
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Запусуємоу CSV-файл
    def export_contacts(self, contacts, file_path) -> None:
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "phones", "email", "address", "birthday"])

                for record in contacts:
                    writer.writerow([
                        record.name.value,
                        ";".join(phone.value for phone in record.phones),
                        record.email.value if record.email else "",
                        record.address.value if record.address else "",
                        str(record.birthday) if record.birthday else "",
                    ])
        except OSError as error:
            raise StorageError(f"Не вдалося експортувати контакти у CSV: {error}") from error

    # Запусуємо notes у  CSV-файл
    def export_notes(self, notes, file_path) -> None:
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "text", "tags"])

                for note in notes:
                    writer.writerow([
                        note.id,
                        note.text,
                        ";".join(tag.value for tag in note.tags),
                    ])
        except OSError as error:
            raise StorageError(f"Не вдалося експортувати нотатки у CSV: {error}") from error

