from datetime import datetime

from exceptions import ValidationError
from models.field import Field


class Birthday(Field):
    DATE_FORMAT = "%d.%m.%Y"

    # Сеттер з валідатором 
    @Field.value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValidationError("Дата народження має бути рядком.")

        try:
            parsed_date = datetime.strptime(new_value.strip(), self.DATE_FORMAT).date()
        except ValueError as error:
            raise ValidationError("Некоректний формат дати. Використовуйте DD.MM.YYYY.") from error

        self._value = parsed_date

    def __str__(self):
        return self.value.strftime(self.DATE_FORMAT)
