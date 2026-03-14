import pickle

from exceptions import StorageError


class PickleClient:
    _instance = None

    # Створює єдиний об'єкт клієнта
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Зберігає дані у pickle файл
    def save(self, data, file_path) -> None:
        try:
            with open(file_path, "wb") as file:
                pickle.dump(data, file)
        except OSError as error:
            raise StorageError(f"Не вдалося зберегти дані: {error}") from error

    # Завантажує дані з файлу
    def load(self, file_path):
        try:
            with open(file_path, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
        except (OSError, pickle.PickleError) as error:
            raise StorageError(f"Не вдалося завантажити дані: {error}") from error
