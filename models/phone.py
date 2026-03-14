import re

from exceptions import ValidationError
from models.field import Field


class Phone(Field):
    PHONE_PATTERN = re.compile(r"")

    # Перевіряє та встановлює номер телефону
    @Field.value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValidationError("Номер телефону має бути рядком.")

        normalized = new_value.strip()

        if not self.PHONE_PATTERN.fullmatch(normalized):
            raise ValidationError("Номер телефону має містити рівно 10 цифр.")

        self._value = normalized
