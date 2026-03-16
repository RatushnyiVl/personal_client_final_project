import re

from personal_assistant.exceptions import ValidationError
from personal_assistant.models.field import Field


class Email(Field):
    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    # Валідує та встановлює email
    @Field.value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValidationError("Email має бути рядком.")

        normalized = new_value.strip()

        if not self.EMAIL_PATTERN.fullmatch(normalized):
            raise ValidationError("Некоректний формат email.")

        self._value = normalized
