from personal_assistant.exceptions import NoteNotFoundError
from personal_assistant.models.note import Note


class NotesBook:
    def __init__(self):
        self.notes: dict[int, Note] = {}
        self._next_id = 1

    def add_note(self, text: str) -> Note:
        note = Note(self._next_id, text)
        self.notes[self._next_id] = note
        self._next_id += 1
        return note

    def find_note(self, note_id: int) -> Note:
        note = self.notes.get(note_id)

        if note is None:
            raise NoteNotFoundError("Нотатку не знайдено.")

        return note

    def delete_note(self, note_id: int) -> None:
        if note_id not in self.notes:
            raise NoteNotFoundError("Нотатку не знайдено.")

        del self.notes[note_id]

    def search(self, query: str) -> list[Note]:
        normalized = query.strip().lower()
        return [note for note in self.notes.values() if normalized in note.text.lower()]

    # Шукає нотатки за тегом
    def search_by_tag(self, tag: str) -> list[Note]:
        return [note for note in self.notes.values() if note.has_tag(tag)]

    # Повертає всі нотатки
    def get_all_notes(self) -> list[Note]:
        return list(self.notes.values())

    # Сортує нотатки за тегами
    def sort_by_tags(self) -> list[Note]:
        return sorted(
            self.notes.values(),
            key=lambda note: ",".join(sorted(tag.value for tag in note.tags))
        )
