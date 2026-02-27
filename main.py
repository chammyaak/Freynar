# main.py (обновленный)
def create_note(title, content):
    return {"title": title, "content": content}

def view_notes(notes):
    for note in notes:
        print(f"Title: {note['title']}\nContent: {note['content']}\n")

def edit_note(notes, note_index, new_title, new_content):
    # Изменяет заметку по индексу
    if 0 <= note_index < len(notes):
        notes[note_index]['title'] = new_title
        notes[note_index]['content'] = new_content
    else:
        print("Invalid note index.")

# Начальные данные
notes = []
note1 = create_note("Первая заметка", "Это просто тестовая заметка.")
notes.append(note1)
view_notes(notes)

# Редактируем первую заметку
edit_note(notes, 0, "Обновленная заметка", "Новый контент заметки.")
view_notes(notes)
