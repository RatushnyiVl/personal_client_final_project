from pathlib import Path

APP_DIR = Path.home() / ".personal_assistant"
APP_DIR.mkdir(parents=True, exist_ok=True)

DATA_FILE = APP_DIR / "assistant_data.pkl"
CONTACTS_CSV_FILE = APP_DIR / "contacts.csv"
NOTES_CSV_FILE = APP_DIR / "notes.csv"
