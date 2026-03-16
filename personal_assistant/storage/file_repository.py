from personal_assistant.config import CONTACTS_CSV_FILE, DATA_FILE, NOTES_CSV_FILE
from personal_assistant.models.contact_book import ContactBook
from personal_assistant.models.notes_book import NotesBook
from personal_assistant.storage.csv_client import CsvClient
from personal_assistant.storage.pickle_client import PickleClient


class FileRepository:

    def __init__(self):
        self.pickle_client = PickleClient()
        self.csv_client = CsvClient()

    # Завантажує всі дані з pickle файлу
    def load_all(self) -> tuple[ContactBook, NotesBook]:
        data = self.pickle_client.load(DATA_FILE)

        if data is None:
            return ContactBook(), NotesBook()

        contacts = data.get("contacts", ContactBook())
        notes = data.get("notes", NotesBook())
        return contacts, notes

    # Зберігає всі дані у pickle файл
    def save_all(self, contacts: ContactBook, notes: NotesBook) -> None:
        payload = {
            "contacts": contacts,
            "notes": notes,
        }
        self.pickle_client.save(payload, DATA_FILE)

    # з pickle файлу у CSV
    def export_all_to_csv(self) -> None:
        data = self.pickle_client.load(DATA_FILE)

        if data is None:
            contacts = ContactBook()
            notes = NotesBook()
        else:
            contacts = data.get("contacts", ContactBook())
            notes = data.get("notes", NotesBook())

        self.csv_client.export_contacts(contacts.data.values(), CONTACTS_CSV_FILE)
        self.csv_client.export_notes(notes.get_all_notes(), NOTES_CSV_FILE)
        