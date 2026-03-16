from personal_assistant.exceptions import ValidationError
from personal_assistant.models.field import Field


class Name(Field):
    # сеттер з валідацією
    @Field.value.setter
    def value(self, new_value):
        if not isinstance(new_value, str) or not new_value.strip():
            raise ValidationError("Ім'я не може бути порожнім.")
        self._value = new_value.strip()
