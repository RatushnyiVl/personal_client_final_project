from models.notes_book import NotesBook


class NoteService:
    def __init__(self, notes_book: NotesBook):
        self.notes_book = notes_book

 