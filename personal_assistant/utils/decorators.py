from functools import wraps

from personal_assistant.exceptions import AssistantError


def input_error(func):
    # Декоратор який обробляє помилки під час виконання
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssistantError as error:
            return str(error)
        except ValueError as error:
            return str(error)
        except IndexError:
            return "Недостатньо аргументів для команди."
        except KeyError:
            return "Сутність не знайдено."

    return inner
