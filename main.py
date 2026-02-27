# main.py
from notes_storage import save_notes_to_file, load_notes_from_file

def create_note(title, content):
    """Создает новую заметку"""
    return {"title": title, "content": content}

def view_notes(notes):
    """Отображает все заметки"""
    if not notes:
        print("Нет заметок.")
    for note in notes:
        print(f"Title: {note['title']}\nContent: {note['content']}\n")

def edit_note(notes, note_index, new_title, new_content):
    """Редактирует заметку по индексу"""
    if 0 <= note_index < len(notes):
        notes[note_index]['title'] = new_title
        notes[note_index]['content'] = new_content
    else:
        print("Invalid note index.")

# Загружаем заметки из файла при запуске
notes = load_notes_from_file()

# Пример создания и редактирования заметок
note1 = create_note("Первая заметка", "Это просто тестовая заметка.")
notes.append(note1)
view_notes(notes)

# Редактируем первую заметку
edit_note(notes, 0, "Обновленная заметка", "Новый контент заметки.")
view_notes(notes)

# Сохраняем заметки в файл
save_notes_to_file(notes)
