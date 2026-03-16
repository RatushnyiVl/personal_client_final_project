class AssistantError(Exception):
    pass


class ValidationError(AssistantError):
    pass


class ContactNotFoundError(AssistantError):
    pass


class NoteNotFoundError(AssistantError):
    pass


class StorageError(AssistantError):
    pass
