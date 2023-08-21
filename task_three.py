import os.path


def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(f"Заметка {note_name} создана.")


def create_note():
    note_name = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    build_note(note_text, note_name)


def read_note():
    note_name_read = input('Введите название заметки: ')
    print(os.path.isfile('note_name_read.txt'))
    if os.path.isfile('note_name_read.txt'):
        note_text = open('note_name_read.txt', 'r')
    else:
        print('Заметка с таким названием не найдена')


read_note()

