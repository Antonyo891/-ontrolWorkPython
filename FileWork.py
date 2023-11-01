from collections import OrderedDict
import json


def save(notes:OrderedDict):
    with open("notes.json", "w", encoding="utf-8") as fh:
        try:
            fh.write(json.dumps(notes, ensure_ascii=False))
            print("Заметки сохранены корректно")
        except:
            print("Сохранение завершено ошибкой")

def load():
    # global notes
    with open("notes.json", "r", encoding="utf-8") as fh:
        try:
            notes = json.load(fh)
            print("Заметки успешно загружены")
        except:
            print("Загрузка завершилась ошибкой")
    return notes