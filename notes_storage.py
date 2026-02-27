# notes_storage.py
import json

def save_notes_to_file(notes, filename="notes.json"):
    """Сохраняет список заметок в JSON файл"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def load_notes_from_file(filename="notes.json"):
    """Загружает список заметок из JSON файла, если файл существует"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []  # Если файл не найден, возвращаем пустой список
    return notes
