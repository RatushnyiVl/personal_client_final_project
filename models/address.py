from exceptions import ValidationError
from models.field import Field


class Address(Field):
    
    @Field.value.setter
    def value(self, new_value):
        if not isinstance(new_value, str) or not new_value.strip():
            raise ValidationError("Адреса не може бути порожньою.")
        self._value = new_value.strip()
