from exceptions import ValidationError
from models.notes_book import NotesBook


class NoteService:
    def __init__(self, notes_book: NotesBook):
        self.notes_book = notes_book

     # Додає нову нотатку
    def add_note(self, text: str) -> str:
        note = self.notes_book.add_note(text)
        return f"Нотатку успішно додано. ID: {note.id}."

    # Редагує нотатку
    def edit_note(self, note_id: int, new_text: str) -> str:
        note = self.notes_book.find_note(note_id)
        note.edit_text(new_text)
        return "Нотатку успішно оновлено."

    # Видаляє нотатку
    def delete_note(self, note_id: int) -> str:
        self.notes_book.delete_note(note_id)
        return "Нотатку успішно видалено."

    # Додає тег до нотатки
    def add_tag(self, note_id: int, tag: str) -> str:
        note = self.notes_book.find_note(note_id)
        note.add_tag(tag)
        return "Тег успішно додано."

    # Видаляє тег з нотатки
    def remove_tag(self, note_id: int, tag: str) -> str:
        note = self.notes_book.find_note(note_id)
        note.remove_tag(tag)
        return "Тег успішно видалено."

    # Шукає нотатки за текстом
    def find_notes(self, query: str) -> str:
        if not query.strip():
            raise ValidationError("Пошуковий запит не може бути порожнім.")

        results = self.notes_book.search(query)

        if not results:
            return "Нотатки не знайдено."

        return "\n".join(str(note) for note in results)

    # Шукає нотатки за тегом
    def find_notes_by_tag(self, tag: str) -> str:
        results = self.notes_book.search_by_tag(tag)

        if not results:
            return "Нотатки за тегом не знайдено."

        return "\n".join(str(note) for note in results)

    # Повертає всі нотатки
    def show_all_notes(self) -> str:
        notes = self.notes_book.get_all_notes()

        if not notes:
            return "Книга нотаток порожня."

        return "\n".join(str(note) for note in notes)

    # Повертає нотатки, відсортовані за тегами
    def sort_notes_by_tags(self) -> str:
        notes = self.notes_book.sort_by_tags()

        if not notes:
            return "Книга нотаток порожня."

        return "\n".join(str(note) for note in notes)
