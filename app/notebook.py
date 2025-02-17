# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.



from datetime import datetime
from typing import List


class Note:

    def __init__(self, code:str, title:str, text:str, importance:str,):
        self.code:str = code
        self.title:str = title
        self.text:str = text
        self.importance:str = importance
        self.creation_date = datetime.now()
        self.tags = []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        while any(note.code == code for note in self.notes):
            code += 1
        new_note = Note(code, title, text, importance)
        self.notes.append(new_note)
        return code

    def delete_note(self, code: int):
        self.notes = [note for note in self.notes if note.code != code]

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes if note.importance in (Note.Hihg, Note.Medium)]

    def notes_by_tag(self, tag: str) -> List[Note]:
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        tag_counts = {}
        for note in self.notes:
            for tag in note.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        if not tag_counts:
            return ""

        max_count = 0
        most_frequent_tag = ""
        for tag, count in tag_counts.items():
            if count > max_count:
                max_count = count
                most_frequent_tag = tag
            elif count == max_count and tag < most_frequent_tag:
                most_frequent_tag = tag
        return most_frequent_tag



