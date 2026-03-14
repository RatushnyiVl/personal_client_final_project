from datetime import datetime

from exceptions import ValidationError
from models.tag import Tag


class Note:

    def __init__(self, note_id: int, text: str):
        self.id = note_id
        self.text = ""
        self.tags: list[Tag] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.set_text(text)

    # сетить текст 
    def set_text(self, text: str) -> None:
        if not isinstance(text, str) or not text.strip():
            raise ValidationError("Текст нотатки не може бути порожнім.")

        self.text = text.strip()
        self.updated_at = datetime.now()

    # Редакт текст 
    def edit_text(self, new_text: str) -> None:
        self.set_text(new_text)

    # Додаємо 
    def add_tag(self, tag: str) -> None:
        tag_obj = Tag(tag)

        if any(item.value == tag_obj.value for item in self.tags):
            return

        self.tags.append(tag_obj)
        self.updated_at = datetime.now()

    def remove_tag(self, tag: str) -> None:
        normalized = tag.strip().lower()
        original_length = len(self.tags)
        self.tags = [item for item in self.tags if item.value != normalized]

        if len(self.tags) == original_length:
            raise ValidationError("Тег не знайдено.")

        self.updated_at = datetime.now()

    # Перевіряє наявність
    def has_tag(self, tag: str) -> bool:
        normalized = tag.strip().lower()
        return any(item.value == normalized for item in self.tags)

    def __str__(self) -> str:
        tags_str = ", ".join(tag.value for tag in self.tags) if self.tags else "немає"
        return f"[{self.id}] {self.text} | Теги: {tags_str}"
